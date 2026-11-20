#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""print_config_tools.py — PrintConfig.cpp 元数据提取 / 键页注入 / 版式迁移 / 对账审计

用法:
  print_config_tools.py extract <fork 的 PrintConfig.cpp 路径> [--out docs/data/print_config_metadata.json]
  print_config_tools.py inject <页面.md ...> | --group <目录> | --all [--dry-run] [--json <路径>]
  print_config_tools.py migrate <页面.md ...> | --group <目录> | --all [--fold] [--dry-run] [--json <路径>]
  print_config_tools.py audit [--json <路径>]

子命令:
  extract  解析 fork PrintConfig.cpp（剥注释、def=new_def 双起点、宽松字段匹配），
           输出键→元数据 JSON（含 meta.source_commit 溯源与统计；label/sidetext=单位）。
           运行时动态键（非字符串字面量键名）跳过并计数；
           filament_* 循环派生键按源键克隆并标 derived=true。
  inject   在 wiki/settings 键页的 [Type] 行与 [CLI Example] 行之间内插
           [Default]/[Unit]/[Range]/[Aliases]（存在才注入，Default 必注入，fork 无键则 —）。
           幂等：已有 [Default(s)] 行的小节跳过。
  migrate  既有键页版式迁移（2026-11-20 裁决）：重建脚本行（[Range] 剥内嵌单位、
           [Unit] 行独立注入）；元数据块与正文间补空行；--fold 时把首个 UI 标签
           标题折进 Location 第 4 段。幂等；镜像小节（Variable 键≠页主干）不动。
  audit    对账：页内已有元数据行 vs JSON 值漂移、Unit 行缺失/漂移、[Range] 残留
           单位、Choice 页缺 [Options]、页键在 JSON 缺失、有 [Type] 而无 [Default] 的页。

退出码: 0 正常; 1 extract 校验失败 / inject 或 audit 发现问题。
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
DEFAULT_JSON = os.path.join(REPO_ROOT, "docs", "data", "print_config_metadata.json")

# ---------------------------------------------------------------------------
# C++ 预处理：剥注释（保留换行，行号近似不变）
# ---------------------------------------------------------------------------

def strip_comments(text):
    out = []
    i, n = 0, len(text)
    state = "code"
    while i < n:
        c = text[i]
        nxt = text[i + 1] if i + 1 < n else ""
        if state == "code":
            if c == "/" and nxt == "/":
                state = "line"; out.append(" "); i += 2; continue
            if c == "/" and nxt == "*":
                state = "block"; out.append(" "); i += 2; continue
            if c == '"':
                state = "str"; out.append(c); i += 1; continue
            if c == "'":
                state = "chr"; out.append(c); i += 1; continue
            out.append(c); i += 1
        elif state == "line":
            if c == "\n":
                state = "code"; out.append("\n")
            i += 1
        elif state == "block":
            if c == "*" and nxt == "/":
                state = "code"; out.append(" "); i += 2; continue
            if c == "\n":
                out.append("\n")  # 保行号
            i += 1
        elif state in ("str", "chr"):
            if c == "\\":
                out.append(text[i:i + 2]); i += 2; continue
            if (state == "str" and c == '"') or (state == "chr" and c == "'"):
                state = "code"
            out.append(c); i += 1
    return "".join(out)


def string_values(expr):
    """取 C++ 表达式里的字符串字面量；相邻字面量拼接（多行 tooltip 拼接）；解码 \\uXXXX 转义。"""
    lits = re.findall(r'"((?:[^"\\]|\\.)*)"', expr)
    if not lits:
        return None
    s = "".join(lits)
    s = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), s)
    s = re.sub(r'\\x([0-9a-fA-F]{2})', lambda m: chr(int(m.group(1), 16)), s)
    return s


# ---------------------------------------------------------------------------
# extract
# ---------------------------------------------------------------------------

# 两种定义起点：def = this->add("key", coType) / new_def("key", coType, ...)
RE_DEF = re.compile(
    r'(?:\bdef\b\s*=\s*|\bauto\s+\w+\s*=\s*def\s*=\s*)?this\s*->\s*add\s*\(\s*"([a-z0-9_]+)"\s*,\s*(\w+)'
    r'|\bnew_def\s*\(\s*"([a-z0-9_]+)"\s*,\s*(\w+)'
)
# 动态键（非字面量键名）：统计用
RE_ADD_ANY = re.compile(r'this\s*->\s*add(?:_nullable)?\s*\(\s*([^,\s]+)')

SKIP_INTS = {"INT_MIN", "INT_MAX"}


def parse_block(block, enum_display=None):
    """从单个键定义块提取元数据字段（宽松匹配，容忍无空格/tab/对齐写法）。"""
    # 块截断：块边界只认字面量键名 add，动态键（def = this->add(非字面量)）不算边界，
    # 其后 def->xxx 赋值属于其它键，须先截掉。切点锚定下一个 def = this->add
    # （含 auto 别名 = def = add 形式，不能锚任意 def = 否则别名形式会被拦腰截断）（2026-11-20）
    cuts = [m.start() for m in re.finditer(
        r'(?:\bauto\s+\w+\s*=\s*)?\bdef\s*=\s*this\s*->\s*add', block)]
    if len(cuts) > 1:
        block = block[:cuts[1]]

    def field(name, call=False):
        # call=True: 方法调用形式 def->name(...)，如 set_default_value
        pat = (r'def\s*->\s*%s\s*\(\s*(.*?)\)\s*;' if call
               else r'def\s*->\s*%s\s*=\s*(.*?);') % name
        # C++ 语义：同字段重复赋值取末次生效值（源码存在 max=0 后紧跟 max=20 的笔误写法，
        # 取首值会把死代码行当真值，2026-11-20 修复）
        hits = re.findall(pat, block, re.S)
        return hits[-1].strip() if hits else None

    rec = {}
    lab = field("label")
    rec["label"] = string_values(lab) if lab else None
    rec["sidetext_raw"] = field("sidetext")
    st = string_values(rec.pop("sidetext_raw") or "")
    rec["sidetext"] = st if st else None
    for lim in ("min", "max"):
        v = field(lim)
        if v is None or v in SKIP_INTS:
            rec[lim] = None
        else:
            try:
                rec[lim] = int(v, 0)
            except ValueError:
                rec[lim] = None  # 标识符/动态边界（如 -max_temp），无法展示
    m = field("mode")
    rec["mode"] = {"comSimple": "Simple", "comAdvanced": "Advanced",
                   "comDevelop": "Developer"}.get(m, m)
    al = field("aliases")
    rec["aliases"] = re.findall(r'"([a-z0-9_]+)"', al) if al else []
    cli = field("cli")
    rec["nocli"] = bool(cli and "nocli" in cli)
    rec["cli"] = None if (cli is None or rec["nocli"] or cli.strip() in ('""', "")) else string_values(cli)
    for ev in ("enum_values", "enum_labels"):
        vals = re.findall(
            r'%s\s*\.\s*(?:push_back|emplace_back)\s*\(\s*("[^"]*"|[A-Za-z_]\w*)\s*\)' % ev, block)
        rec[ev] = [v.strip('"') for v in vals]
    rec["default"] = parse_default(field("set_default_value", call=True) or "", enum_display)
    rec.pop("sidetext_raw", None)
    return rec


def parse_default(expr, enum_display=None):
    """set_default_value(new ConfigOptionXxx{...}/(...)) → 字面值串。"""
    if not expr:
        return None
    m = re.search(r'new\s+[\w:]+\s*(?:<[^>]*>)?\s*(?:\{(.*)\}|\((.*)\))\s*$', expr, re.S)
    inner = (m.group(1) if m and m.group(1) is not None else m.group(2)) if m else expr.strip()
    inner = (inner or "").strip()
    # 剥本地化宏壳 L("...") → "..."（全文件唯一处：filament_vendor 默认 "(Undefined)"，
    # 2026-11-20 修复——此前宏壳漏进 JSON 与键页）
    inner = re.sub(r'\bL\(\s*("(?:[^"\\]|\\.)*")\s*\)', r'\1', inner)
    if inner == "":
        return ""  # 显式空默认
    if len(inner) >= 2 and inner[0] == '"' and inner[-1] == '"':
        return inner[1:-1]  # 整串字符串字面量（含逗号/换行），原样保留不拆分
    parts = [p.strip() for p in inner.split(",")]
    norm = []
    for p in parts:
        if len(p) >= 2 and p[0] == p[-1] == '"':
            p = p[1:-1]
        if re.fullmatch(r"-?\d+(?:\.\d+)?f", p):
            p = p[:-1]  # 60.0f → 60.0
        if p.endswith(".") and p[:-1].lstrip("-").replace(".", "", 1).isdigit():
            p = p[:-1]  # 60. → 60
        norm.append(p)
    out = ", ".join(norm)
    # 点类型嵌套：Vec2d(a, b), … → a×b, …
    if "Vec2d" in out:
        pts = re.findall(r"Vec2d\(\s*([^)]*)\)", out)
        if pts:
            out = ", ".join("×".join(x.strip() for x in pt.split(",")) for pt in pts)
    # FloatOrPercent{v, is_percent} → v% / v
    out = re.sub(r"FloatOrPercent\s*\{\s*(-?[\d.]+)\s*,\s*(true|false)\s*\}",
                 lambda m_: m_.group(1).rstrip(".") + ("%" if m_.group(2) == "true" else ""), out)
    # 单值括号形式 ConfigOptionFloatOrPercent(100, true) → 100%
    m_fp = re.fullmatch(r"(-?[\d.]+),\s*(true|false)", out)
    if m_fp:
        out = m_fp.group(1).rstrip(".") + ("%" if m_fp.group(2) == "true" else "")
    # 枚举常量默认值 → 用户可见枚举串（s_keys_map_* 静态映射）
    if enum_display:
        out = re.sub(r"\(\s*int\s*\)\s*([A-Za-z_]\w*)",
                     lambda m_: enum_display.get(m_.group(1), m_.group(1)), out)
        out = re.sub(r"\bint\s*\(\s*([A-Za-z_]\w*)\s*\)",
                     lambda m_: enum_display.get(m_.group(1), m_.group(1)), out)
        if re.fullmatch(r"[A-Za-z_]\w*", out or ""):
            out = enum_display.get(out, out)
    return out


def cmd_extract(args):
    src = os.path.abspath(args.src)
    if not os.path.isfile(src):
        print("[FAIL] 文件不存在: %s" % src); return 1
    text = open(src, encoding="utf-8", errors="replace").read()
    stripped = strip_comments(text)
    # PrintConfig.hpp 宏声明补位（((ConfigOptionXxx, key)) 序列；默认值多由预设驱动）
    hpp = os.path.abspath(args.hpp or os.path.join(os.path.dirname(src), "PrintConfig.hpp"))
    hpp_macro_keys = []
    if os.path.isfile(hpp):
        htext = strip_comments(open(hpp, encoding="utf-8", errors="replace").read())
        hpp_macro_keys = [(t, k, k.lower()) for t, k in
                          re.findall(r'\(\(\s*(ConfigOption[\w<>:]*?)\s*,\s*([A-Za-z0-9_]+)', htext)]

    keys, dynamic_skips, stats = {}, [], {"min": 0, "max": 0, "sidetext": 0,
                                          "label": 0, "aliases": 0, "enum_rows": 0, "nocli": 0}
    # 枚举常量 → 用户可见枚举串（s_keys_map_* 静态映射，用于默认值翻译）
    enum_display = {}
    for tbl in re.findall(r's_keys_map_\w+\s*=\s*\{(.*?)\};', stripped, re.S):
        for disp, const in re.findall(r'\{\s*"([^"]*)"\s*,\s*(\w+)\s*\}', tbl):
            enum_display[const] = disp
    starts = [(m.start(), m.group(1) or m.group(3), m.group(2) or m.group(4))
              for m in RE_DEF.finditer(stripped)]
    for idx, (pos, key, cotype) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(stripped)
        rec = parse_block(stripped[pos:end], enum_display)
        rec.update({"type": cotype,
                    "line": stripped[:pos].count("\n") + 1,
                    "derived": False})
        for f in ("min", "max", "sidetext", "nocli"):
            if rec[f] is not None and rec[f] is not False and rec[f] != "":
                stats[f] += 1
        if rec.get("label"):
            stats["label"] += 1
        if rec["aliases"]:
            stats["aliases"] += 1
        stats["enum_rows"] += len(rec["enum_values"])
        keys[key] = rec

    # 动态键计数（this->add 首参非字符串字面量；含 #define new_def 宏体 1 处）
    for m in RE_ADD_ANY.finditer(stripped):
        if not m.group(1).startswith('"'):
            dynamic_skips.append(m.group(1))

    # hpp 宏补位：仅补 cpp 未定义的键（machine limits 族等，默认值由预设提供）
    hpp_filled = []
    for ctype, declared, key in hpp_macro_keys:
        if key in keys:
            continue
        rec_h = {"type": ctype, "mode": None, "default": None, "label": None,
                 "min": None, "max": None, "sidetext": None, "aliases": [],
                 "enum_values": [], "enum_labels": [], "nocli": False,
                 "cli": None, "line": None, "derived": False,
                 "source": "hpp_macro"}
        if declared != key:
            rec_h["declared_as"] = declared  # 如 required_nozzle_HRC
        keys[key] = rec_h
        hpp_filled.append(key)

    # filament_* 循环派生键：按源键克隆（min/max/sidetext/type 同源键）
    loop = re.search(r'for\s*\(\s*const\s+char\s*\*\s*opt_key\s*:\s*\{(.*?)\}\s*\)', stripped, re.S)
    derived = 0
    if loop:
        for base in re.findall(r'"([a-z0-9_]+)"', loop.group(1)):
            src_rec = keys.get("filament_" + base)
            if src_rec and src_rec.get("derived"):
                continue
            b = keys.get(base)
            if not b:
                print("[WARN] 派生源键未找到: %s" % base); continue
            keys["filament_" + base] = {
                "type": b["type"], "mode": b["mode"], "default": None,
                "label": b.get("label"), "min": b["min"], "max": b["max"],
                "sidetext": b["sidetext"],
                "aliases": [], "enum_values": b["enum_values"],
                "enum_labels": b["enum_labels"], "nocli": b["nocli"], "cli": b["cli"],
                "line": b["line"], "derived": True}
            derived += 1

    # 溯源
    fork_root = os.path.abspath(os.path.join(src, "..", "..", ".."))
    try:
        commit = subprocess.run(["git", "-C", fork_root, "rev-parse", "HEAD"],
                                capture_output=True, text=True, timeout=10
                                ).stdout.strip() or "unknown"
    except Exception:
        commit = "unknown"

    doc = {"meta": {
        "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "source_file": "src/libslic3r/PrintConfig.cpp",
        "source_commit": commit,
        "stats": dict(stats, total_keys=len(keys), derived_keys=derived,
                      hpp_macro_keys=len(hpp_filled),
                      dynamic_skipped=len(dynamic_skips),
                      dynamic_skip_names=sorted(set(dynamic_skips))),
        "notes": ["动态键(非字面量键名)已跳过: project_schema.config_key / 宏体 OPT_KEY / add_nullable 循环",
                  "filament_* 派生键由循环源键克隆(derived=true, default 未克隆)",
                  "line 为剥注释后文本的近似行号"]},
        "keys": dict(sorted(keys.items()))}

    out = os.path.abspath(args.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print("extracted %d keys -> %s" % (len(keys), out))
    print("stats: %s" % json.dumps(doc["meta"]["stats"], ensure_ascii=False))
    print("source_commit: %s" % commit)
    return 0


# ---------------------------------------------------------------------------
# inject
# ---------------------------------------------------------------------------

RE_TYPE_LINE = re.compile(r'^\[Type\]')
RE_CLI_LINE = re.compile(r'^\[CLI Example\]')
RE_VAR_LINE = re.compile(r'^\[Variables?\]')
RE_MODE_LINE = re.compile(r'^\[Modes?\]')
RE_HAS_DEFAULT = re.compile(r'^\[Defaults?\]')
RE_KEY_TOKEN = re.compile(r'`([a-z0-9_]+)`')
RE_EOL = re.compile(r'(\r?\n)$')
RE_UNIT_LINE = re.compile(r'^\[Units?\]')
# 脚本生成行（migrate 的重建对象；[Options] 为手写行，不属于）
RE_OWNED_LINE = re.compile(r'^\[(Default|Unit|Range|Aliases)s?\]')
# 元数据家族行（含手写 [Mode]/[Variable]/[Type]/[Options]/[CLI Example]）
RE_META_FAMILY = re.compile(r'^\[(Mode|Variable|Type|Default|Unit|Range|Options|Aliases|CLI Example)s?\]')
# 元数据行固定顺序（2026-11-20 裁决：全库一致，缺省跳过）
FIELD_ORDER = ["mode", "variable", "type", "default", "unit", "range",
               "aliases", "options", "cli example"]
RE_FIELD_NAME = re.compile(r'^\[([^\]]+)\]')


def canon_field(name):
    """元数据行名 → 固定顺序索引；非元数据行（如正文里的 [gcode_macro M106]）返回 None。"""
    n = name.lower()
    if n in FIELD_ORDER:
        return FIELD_ORDER.index(n)
    if n.endswith("s") and n[:-1] in FIELD_ORDER:  # Variables/Defaults 等复数镜像行
        return FIELD_ORDER.index(n[:-1])
    return None


def page_files(args):
    if args.all or args.group:
        root = os.path.join(REPO_ROOT, "wiki", "settings")
        base = args.group
        if base:
            p = os.path.join(REPO_ROOT, base) if os.path.isdir(os.path.join(REPO_ROOT, base)) \
                else os.path.join(root, base)
            root = p
        for dirpath, _, files in os.walk(root):
            for fn in sorted(files):
                if fn.endswith(".md") and not fn.endswith("_overview.md"):
                    yield os.path.join(dirpath, fn)
    else:
        for p in args.pages:
            yield p


def rel_prefix(page_path):
    """页面到 wiki/ 的 ../ 前缀（键页恒为 wiki/settings/<tab>/<分组>/，即 ../../../）。"""
    rel = os.path.relpath(os.path.dirname(os.path.abspath(page_path)),
                          os.path.join(REPO_ROOT, "wiki"))
    return "../" * (rel.count(os.sep) + 1)


def fmt_num(v):
    return str(v)


def range_str(rec):
    lo, hi = rec.get("min"), rec.get("max")
    if lo is None and hi is None:
        return None
    core = ("%s–%s" % (fmt_num(lo), fmt_num(hi)) if lo is not None and hi is not None
            else ("≥ %s" % fmt_num(lo) if lo is not None else "≤ %s" % fmt_num(hi)))
    return "`%s`" % core  # 单位不内嵌（2026-11-20 裁决：单位独立为 [Unit] 行）


def build_lines(keyset, meta, prefix):
    """按小节键列表构造 [Default]/[Unit]/[Range]/[Aliases] 行（Markdown 源，不含换行）。"""
    link_d = "(%sgeneral_settings/option_type.md#default-value)" % prefix
    link_u = "(%sgeneral_settings/option_type.md#unit)" % prefix
    link_r = "(%sgeneral_settings/option_type.md#range)" % prefix
    link_a = "(%sgeneral_settings/option_type.md#aliases)" % prefix
    lines = []
    found = [k for k in keyset if k in meta]

    def val(k):
        """— no static default = fork 有键但 def 未设默认（预设/代码提供）；— = fork 未见此键。"""
        if k not in meta:
            return "—"
        d = meta[k].get("default")
        if d is None:
            return "— no static default"
        return d if d != "" else "(empty)"

    # 2026-11-19 约定：键页元数据只保留本键自己的值（单数行），不捆绑同小节其他键
    k = keyset[0] if keyset else None
    if k in meta:
        v = val(k)
        lines.append("[Default]%s: `%s`." % (link_d, v)
                     if not v.startswith("—") else "[Default]%s: %s." % (link_d, v))
        u = meta[k].get("sidetext")
        if u:
            lines.append("[Unit]%s: `%s`." % (link_u, u))
        r = range_str(meta[k])
        if r:
            lines.append("[Range]%s: %s." % (link_r, r))
    else:
        lines.append("[Default]%s: —." % link_d)
    als = sorted({a for k in found for a in meta[k].get("aliases", [])})
    if als:
        lines.append("[Aliases]%s: %s." % (link_a, ", ".join("`%s`" % a for a in als)))
    return lines


def inject_page(path, meta, dry_run):
    with open(path, encoding="utf-8", newline="") as f:
        text = f.read()
    eol = "\r\n" if "\r\n" in text else "\n"
    lines = text.split(eol)
    prefix = rel_prefix(path)
    stem = os.path.splitext(os.path.basename(path))[0]

    inserts, skipped = [], 0
    for i, ln in enumerate(lines):
        if not RE_TYPE_LINE.match(ln):
            continue
        # 幂等：小节内已有 [Default(s)]；扫描以空行/下一标签行为界，防跨小节误判
        j = i + 1
        while (j < len(lines) and lines[j].strip()
               and not RE_CLI_LINE.match(lines[j]) and not RE_TYPE_LINE.match(lines[j])
               and not RE_MODE_LINE.match(lines[j]) and not RE_VAR_LINE.match(lines[j])):
            if RE_HAS_DEFAULT.match(lines[j]):
                skipped += 1; break
            j += 1
        else:
            # 2026-11-19 约定：恒取本页自己的键（文件名主干），不再沿用小节键列表
            keys = [stem]
            new = build_lines(keys, meta, prefix)
            inserts.append((i + 1, [l + "  " for l in new]))

    if not inserts:
        return False, skipped
    for pos, new in reversed(inserts):
        lines[pos:pos] = new
    out = eol.join(lines)
    if dry_run:
        print("[DRY] %s: +%d 行" % (os.path.relpath(path, REPO_ROOT),
                                    sum(len(x[1]) for x in inserts)))
    else:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(out)
        print("[OK] %s: +%d 行" % (os.path.relpath(path, REPO_ROOT),
                                   sum(len(x[1]) for x in inserts)))
    return True, skipped


def cmd_inject(args):
    meta = json.load(open(args.json, encoding="utf-8"))["keys"]
    changed = 0
    total_skip = 0
    for p in page_files(args):
        did, skipped = inject_page(p, meta, args.dry_run)
        total_skip += skipped
        changed += 1 if did else 0
    print("--\n%s %d 页（幂等跳过小节 %d 处）" % ("将修改" if args.dry_run else "已修改",
                                              changed, total_skip))
    return 0


# ---------------------------------------------------------------------------
# migrate（2026-11-20 版式裁决：Unit 行拆分 / 正文空行分隔 / --fold 标签折进 Location）
# ---------------------------------------------------------------------------

def section_var_key(lines, i):
    """[Type] 行（下标 i）向上找 [Variable] 行的键名；无 Variable 行返回 None。"""
    for b in range(i - 1, max(i - 7, -1), -1):
        l0 = lines[b]
        if RE_VAR_LINE.match(l0):
            kt = RE_KEY_TOKEN.search(l0)
            return kt.group(1) if kt else None
        if l0.strip() and not RE_META_FAMILY.match(l0):
            break
    return None


def migrate_page(path, meta, dry_run, fold):
    with open(path, encoding="utf-8", newline="") as f:
        text = f.read()
    eol = "\r\n" if "\r\n" in text else "\n"
    lines = text.split(eol)
    prefix = rel_prefix(path)
    stem = os.path.splitext(os.path.basename(path))[0]
    rel = os.path.relpath(path, REPO_ROOT)
    stats = {"sections": 0, "units": 0, "blanks": 0, "folds": 0, "reorders": 0}

    # ---- A. 重建脚本行：[Range] 剥内嵌单位、[Unit] 独立成行 -----------------
    out, i, n = [], 0, len(lines)
    while i < n:
        ln = lines[i]
        out.append(ln)
        i += 1
        if not RE_TYPE_LINE.match(ln):
            continue
        if section_var_key(lines, i - 1) not in (None, stem):
            continue  # 镜像小节（非本页主干键），原样保留
        # 窗口：[Type] 之后到边界（CLI/Mode/Variable/Type/标题/引用/空行）为止
        j = i
        while j < n:
            l2 = lines[j]
            if (RE_CLI_LINE.match(l2) or RE_MODE_LINE.match(l2) or RE_VAR_LINE.match(l2)
                    or RE_TYPE_LINE.match(l2) or not l2.strip()
                    or l2.startswith("#") or l2.startswith(">")):
                break
            j += 1
        window = [lines[k] for k in range(i, j) if not RE_OWNED_LINE.match(lines[k])]
        new = [l + "  " for l in build_lines([stem], meta, prefix)]
        cand = new + window
        orig = lines[i:j]
        if cand == orig:
            out.extend(orig)  # 幂等：重建结果与现状一致，不计修改
        else:
            stats["units"] += sum(1 for l in new if RE_UNIT_LINE.match(l))
            out.extend(cand)
            stats["sections"] += 1
        i = j
    lines = out

    # ---- A2. 元数据行固定顺序重排（缺省跳过；正文里的 [gcode_macro …] 不动）--
    out, i, n = [], 0, len(lines)
    while i < n:
        m2 = RE_FIELD_NAME.match(lines[i])
        if not m2 or canon_field(m2.group(1)) is None:
            out.append(lines[i])
            i += 1
            continue
        j = i
        run = []
        while j < n:
            m3 = RE_FIELD_NAME.match(lines[j])
            if not m3 or canon_field(m3.group(1)) is None:
                break
            run.append((canon_field(m3.group(1)), lines[j]))
            j += 1
        if [k for k, _ in run] != sorted(k for k, _ in run):
            out.extend(l for _, l in sorted(run, key=lambda t: t[0]))  # 稳定排序
            stats["reorders"] += 1
        else:
            out.extend(l for _, l in run)
        i = j
    lines = out

    # ---- B. 元数据块与正文之间补空行（家族行连续段落后首个非家族行前）-------
    out, i, n = [], 0, len(lines)
    while i < n:
        out.append(lines[i])
        if RE_META_FAMILY.match(lines[i]):
            j = i
            while j + 1 < n and RE_META_FAMILY.match(lines[j + 1]):
                j += 1
            out.extend(lines[i + 1:j + 1])
            if j + 1 < n and lines[j + 1].strip():
                out.append("")
                stats["blanks"] += 1
            i = j + 1
        else:
            i += 1
    lines = out

    # ---- C. --fold：首个 UI 标签标题折进 Location 第 4 段 --------------------
    if fold and "> Status:" not in text and any(RE_TYPE_LINE.match(l) for l in lines):
        hr = next((k for k, l in enumerate(lines) if l.strip() == "---"), None)
        if hr is not None:
            k = hr + 1
            while k < len(lines) and not lines[k].strip():
                k += 1
            m = re.match(r"^#{1,4}\s+(.+?)\s*$", lines[k]) if k < len(lines) else None
            if m:
                label = m.group(1)
                loc_i = next((x for x, l in enumerate(lines)
                              if l.startswith("> Location:")), None)
                low = label.lower()
                if (loc_i is not None and lines[loc_i].count("→") < 3
                        and "from fork" not in low and low != "basic information"):
                    lines[loc_i] += " → " + label
                    del lines[k]
                    # --- 之后保持恰好一个空行
                    if lines[hr + 1].strip():
                        lines.insert(hr + 1, "")
                    elif hr + 2 < len(lines) and not lines[hr + 2].strip():
                        del lines[hr + 2]
                    stats["folds"] += 1

    if not any(stats.values()):
        return stats
    if dry_run:
        print("[DRY] %s: %s" % (rel, stats))
    else:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(eol.join(lines))
        print("[OK] %s: %s" % (rel, stats))
    return stats


def cmd_migrate(args):
    meta = json.load(open(args.json, encoding="utf-8"))["keys"]
    agg = {"sections": 0, "units": 0, "blanks": 0, "folds": 0, "reorders": 0}
    pages = 0
    for p in page_files(args):
        st = migrate_page(p, meta, args.dry_run, args.fold)
        if any(st.values()):
            pages += 1
            for k in agg:
                agg[k] += st[k]
    print("--\n%s %d 页：重建小节 %d（[Unit] 行 %d）、补空行 %d、折标签 %d、行序重排 %d"
          % ("将修改" if args.dry_run else "已修改", pages,
             agg["sections"], agg["units"], agg["blanks"], agg["folds"],
             agg["reorders"]))
    return 0


# ---------------------------------------------------------------------------
# banner（Q5：fork 未实现小节加 WARNING 横幅）
# ---------------------------------------------------------------------------

def banner_page(path, meta, dry_run):
    with open(path, encoding="utf-8", newline="") as f:
        text = f.read()
    eol = "\r\n" if "\r\n" in text else "\n"
    lines = text.split(eol)
    rel = os.path.relpath(path, REPO_ROOT)

    inserts, skipped = [], 0
    for i, ln in enumerate(lines):
        if not RE_VAR_LINE.match(ln):
            continue
        keys = RE_KEY_TOKEN.findall(ln)
        if not keys:
            continue
        missing = [k for k in keys if k not in meta]
        if not missing:
            continue
        # 定位本小节 [Mode] 行（Mode 在 Variable 上一行）；无则用 Variable 行本身
        at = i
        for b in range(i - 1, max(i - 4, -1), -1):
            if RE_MODE_LINE.match(lines[b]):
                at = b; break
            if lines[b].strip() and not RE_VAR_LINE.match(lines[b]) and b < i - 1:
                break
        # 幂等：上方 5 行内已有"软件未收录"横幅（旧中文版文案亦认）
        if any(("Not available in this software version" in lines[x]
                or "fork 未实现" in lines[x])
               for x in range(max(0, at - 5), at)):
            skipped += 1; continue
        mk = "、".join("`%s`" % k for k in missing)
        if len(missing) == len(keys):
            body = ("%s is an upstream OrcaSlicer parameter not available in the current "
                    "software version; the content below is kept for reference." % mk)
        else:
            body = ("%s is an upstream OrcaSlicer parameter not available in the current "
                    "software version; the other parameters in this section work normally." % mk)
        blk = ["> [!WARNING] Not available in this software version", "> " + body, ""]
        # 确保横幅上方空行分隔
        if at > 0 and lines[at - 1].strip():
            blk.insert(0, "")
        inserts.append((at, blk))

    if not inserts:
        return False, skipped
    for pos, blk in reversed(inserts):
        lines[pos:pos] = blk
    out = eol.join(lines)
    if dry_run:
        print("[DRY] %s: +%d 横幅" % (rel, len(inserts)))
    else:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(out)
        print("[OK] %s: +%d 横幅" % (rel, len(inserts)))
    return True, skipped


def cmd_banner(args):
    meta = json.load(open(args.json, encoding="utf-8"))["keys"]
    changed, total_skip = 0, 0
    for p in page_files(args):
        did, skipped = banner_page(p, meta, args.dry_run)
        total_skip += skipped
        changed += 1 if did else 0
    print("--\n%s %d 页（幂等跳过 %d 处）" % ("将修改" if args.dry_run else "已修改",
                                          changed, total_skip))
    return 0


# ---------------------------------------------------------------------------
# audit
# ---------------------------------------------------------------------------

def norm(v):
    return re.sub(r"[\s,]+", "", str(v or "")).strip("`")


def cmd_audit(args):
    meta = json.load(open(args.json, encoding="utf-8"))["keys"]
    issues = {"no_default_line": [], "default_drift": [], "key_not_in_json": [],
              "choice_no_options": [], "mode_drift": [],
              "unit_missing": [], "unit_drift": [], "range_unit_leftover": [],
              "field_order": []}
    n_pages = n_sections = 0
    for p in page_files(argparse.Namespace(all=True, group=None, pages=None)):
        text = open(p, encoding="utf-8", newline="").read()
        rel = os.path.relpath(p, REPO_ROOT)
        lines = text.splitlines()
        stem = os.path.splitext(os.path.basename(p))[0]
        has_default_any = False
        for i, ln in enumerate(lines):
            if not RE_TYPE_LINE.match(ln):
                continue
            n_sections += 1
            keys = None
            for b in range(i - 1, max(i - 6, -1), -1):
                if RE_VAR_LINE.match(lines[b]):
                    keys = RE_KEY_TOKEN.findall(lines[b])
                    if keys:
                        break
            keys = keys or [stem]
            # Q4：Mode 值 vs fork 枚举（fork 无键的小节跳过，由 banner 处理）
            mval = None
            for b in range(i - 2, max(i - 8, -1), -1):
                if RE_MODE_LINE.match(lines[b]):
                    m = re.search(r'`([A-Za-z]+)`', lines[b])
                    mval = m.group(1) if m else None
                    break
            if mval:
                # 混合模式小节（fork 各键可见级不同）单行 Mode 无法表达，不报
                modes = {meta[k].get("mode") for k in keys
                         if k in meta and meta[k].get("mode")}
                if len(modes) == 1:
                    fm = modes.pop()
                    if fm != mval:
                        issues["mode_drift"].append(
                            "%s:%d %s 页标 %s / fork %s" % (rel, i + 1, ", ".join(keys), mval, fm))
            j = i + 1
            dline = None
            while j < len(lines) and not RE_CLI_LINE.match(lines[j]) and lines[j].strip():
                if RE_HAS_DEFAULT.match(lines[j]):
                    dline = lines[j]; break
                j += 1
            if dline is None:
                issues["no_default_line"].append("%s:%d" % (rel, i + 1))
            else:
                has_default_any = True
                # 取值部分（首个冒号后）拍平后等值比较——不能用整行子串匹配，
                # 否则 L(Undefined) 含子串 Undefined 会漏报宏壳类漂移（2026-11-20 修复）
                flat_line = re.sub(r"[\s,`'\"]+", "", dline.split(":", 1)[-1].strip().rstrip("."))
                for k in keys:
                    if k not in meta:
                        continue
                    exp = meta[k].get("default")
                    if exp in (None, ""):
                        continue
                    if re.sub(r"[\s,`'\"]+", "", str(exp)) != flat_line:
                        issues["default_drift"].append(
                            "%s:%d %s 期望 %s 实际 %s" % (rel, i + 1, k, exp, dline.strip()))
            for k in keys:
                if k not in meta:
                    issues["key_not_in_json"].append("%s (%s)" % (rel, k))
            # Unit 行对账 + [Range] 残留单位（口径：恒取本页主干键，镜像小节只查残留）
            uline = rline = None
            j2 = i + 1
            while j2 < len(lines) and lines[j2].strip() and not RE_CLI_LINE.match(lines[j2]):
                if RE_UNIT_LINE.match(lines[j2]):
                    uline = lines[j2]
                if lines[j2].startswith("[Range]"):
                    rline = lines[j2]
                j2 += 1
            if rline:
                mu = re.match(r"^\[Range\]\([^)]*\):\s*`[^`]*`(.*)$", rline)
                if mu and mu.group(1).strip().rstrip(".").strip():
                    issues["range_unit_leftover"].append("%s:%d %s" % (rel, i + 1, rline.strip()))
            if keys[0] == stem:
                st = meta.get(stem, {}).get("sidetext")
                if st and uline is None:
                    issues["unit_missing"].append("%s:%d %s sidetext=%s" % (rel, i + 1, stem, st))
                elif uline is not None and st:
                    got = re.sub(r"[\s`]+", "", uline.split(":", 1)[-1].rstrip(" ."))
                    if got != re.sub(r"\s+", "", st):
                        issues["unit_drift"].append(
                            "%s:%d 页 `%s` / fork `%s`" % (rel, i + 1, got, st))
            if "Choice" in ln:
                window = "\n".join(lines[i:i + 4])
                if "[Options]" not in window and "[Options]" not in "\n".join(lines[max(0, i - 1):i]):
                    issues["choice_no_options"].append("%s:%d" % (rel, i + 1))
        n_pages += 1
        if not has_default_any and any(RE_TYPE_LINE.match(l) for l in lines):
            pass
        # 元数据行固定顺序（页面级扫描：覆盖镜像小节与 Mode/Variable 残缺块）
        i2 = 0
        while i2 < len(lines):
            m2 = RE_FIELD_NAME.match(lines[i2])
            if not m2 or canon_field(m2.group(1)) is None:
                i2 += 1
                continue
            j2 = i2
            names = []
            while j2 < len(lines):
                m3 = RE_FIELD_NAME.match(lines[j2])
                if not m3 or canon_field(m3.group(1)) is None:
                    break
                names.append((canon_field(m3.group(1)), m3.group(1)))
                j2 += 1
            ks = [k for k, _ in names]
            if ks != sorted(ks) or len(set(ks)) != len(ks):
                issues["field_order"].append(
                    "%s:%d %s" % (rel, i2 + 1, " > ".join(n for _, n in names)))
            i2 = j2
    print("审计 %d 页 / %d 个 [Type] 小节" % (n_pages, n_sections))
    for k, v in issues.items():
        print("\n[%s] %d" % (k, len(v)))
        for row in v[:40]:
            print("  " + row)
        if len(v) > 40:
            print("  … 另 %d 条" % (len(v) - 40))
    return 0


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    e = sub.add_parser("extract", help="从 fork PrintConfig.cpp 提取元数据 JSON")
    e.add_argument("src", help="fork 仓库中 PrintConfig.cpp 的路径")
    e.add_argument("--hpp", help="PrintConfig.hpp 路径（默认取 src 同目录，用于宏声明补位）")
    e.add_argument("--out", default=DEFAULT_JSON)
    e.set_defaults(func=cmd_extract)

    j = sub.add_parser("inject", help="向键页内插 [Default]/[Unit]/[Range]/[Aliases]")
    j.add_argument("pages", nargs="*", help="页面路径")
    j.add_argument("--group", help="目录（如 wiki/settings/filament/cooling）")
    j.add_argument("--all", action="store_true", help="全部键页")
    j.add_argument("--dry-run", action="store_true")
    j.add_argument("--json", default=DEFAULT_JSON)
    j.set_defaults(func=cmd_inject)

    g = sub.add_parser("migrate", help="既有键页版式迁移（Unit 拆分/空行分隔/--fold 标签折叠）")
    g.add_argument("pages", nargs="*", help="页面路径")
    g.add_argument("--group", help="目录（如 wiki/settings/filament/cooling）")
    g.add_argument("--all", action="store_true", help="全部键页")
    g.add_argument("--fold", action="store_true", help="首个 UI 标签标题折进 Location 第 4 段")
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--json", default=DEFAULT_JSON)
    g.set_defaults(func=cmd_migrate)

    a = sub.add_parser("audit", help="页内元数据 vs JSON 对账")
    a.add_argument("--json", default=DEFAULT_JSON)
    a.set_defaults(func=cmd_audit)

    b = sub.add_parser("banner", help="fork 未实现小节加 WARNING 横幅（Q5）")
    b.add_argument("pages", nargs="*", help="页面路径")
    b.add_argument("--group", help="目录（如 wiki/settings/filament/cooling）")
    b.add_argument("--all", action="store_true", help="全部键页")
    b.add_argument("--dry-run", action="store_true")
    b.add_argument("--json", default=DEFAULT_JSON)
    b.set_defaults(func=cmd_banner)

    args = ap.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
