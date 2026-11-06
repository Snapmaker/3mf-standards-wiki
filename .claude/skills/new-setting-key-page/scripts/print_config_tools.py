#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""print_config_tools.py — PrintConfig.cpp 元数据提取 / 键页注入 / 对账审计

用法:
  print_config_tools.py extract <fork 的 PrintConfig.cpp 路径> [--out docs/data/print_config_metadata.json]
  print_config_tools.py inject <页面.md ...> | --group <目录> | --all [--dry-run] [--json <路径>]
  print_config_tools.py audit [--json <路径>]

子命令:
  extract  解析 fork PrintConfig.cpp（剥注释、def=new_def 双起点、宽松字段匹配），
           输出键→元数据 JSON（含 meta.source_commit 溯源与统计）。
           运行时动态键（非字符串字面量键名）跳过并计数；
           filament_* 循环派生键按源键克隆并标 derived=true。
  inject   在 wiki/setting 键页的 [Type] 行与 [CLI Example] 行之间内插
           [Default]/[Range]/[Aliases]（存在才注入，Default 必注入，fork 无键则 —）。
           幂等：已有 [Default(s)] 行的小节跳过。
  audit    对账：页内已有元数据行 vs JSON 值漂移、Choice 页缺 [Options]、
           页键在 JSON 缺失、有 [Type] 而无 [Default] 的页。

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
    """取 C++ 表达式里的字符串字面量；相邻字面量拼接（多行 tooltip 拼接）。"""
    lits = re.findall(r'"((?:[^"\\]|\\.)*)"', expr)
    if not lits:
        return None
    return "".join(lits)


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
    def field(name, call=False):
        # call=True: 方法调用形式 def->name(...)，如 set_default_value
        pat = (r'def\s*->\s*%s\s*\(\s*(.*?)\)\s*;' if call
               else r'def\s*->\s*%s\s*=\s*(.*?);') % name
        m = re.search(pat, block, re.S)
        return m.group(1).strip() if m else None

    rec = {}
    lab = field("label")
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
                rec[lim] = v  # 非字面量（少见），保留原文
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
    if inner == "":
        return ""  # 显式空默认
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
                                          "aliases": 0, "enum_rows": 0, "nocli": 0}
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
        rec_h = {"type": ctype, "mode": None, "default": None,
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
                "min": b["min"], "max": b["max"], "sidetext": b["sidetext"],
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
RE_HAS_DEFAULT = re.compile(r'^\[Defaults?\]')
RE_KEY_TOKEN = re.compile(r'`([a-z0-9_]+)`')
RE_EOL = re.compile(r'(\r?\n)$')


def page_files(args):
    if args.all or args.group:
        root = os.path.join(REPO_ROOT, "wiki", "setting")
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
    """页面到 wiki/ 的 ../ 前缀（键页恒为 wiki/setting/<tab>/<分组>/，即 ../../../）。"""
    rel = os.path.relpath(os.path.dirname(os.path.abspath(page_path)),
                          os.path.join(REPO_ROOT, "wiki"))
    return "../" * (rel.count(os.sep) + 1)


def fmt_num(v):
    return str(v)


def range_str(rec):
    lo, hi, unit = rec.get("min"), rec.get("max"), rec.get("sidetext")
    if lo is None and hi is None:
        return None
    core = ("%s–%s" % (fmt_num(lo), fmt_num(hi)) if lo is not None and hi is not None
            else ("≥ %s" % fmt_num(lo) if lo is not None else "≤ %s" % fmt_num(hi)))
    return "`%s`%s" % (core, " %s" % unit if unit else "")


def build_lines(keyset, meta, prefix):
    """按小节键列表构造 [Default]/[Range]/[Aliases] 行（Markdown 源，不含换行）。"""
    link_d = "(%sgeneral_settings/option_type.md#default-value)" % prefix
    link_r = "(%sgeneral_settings/option_type.md#range)" % prefix
    link_a = "(%sgeneral_settings/option_type.md#aliases)" % prefix
    lines = []
    found = [k for k in keyset if k in meta]

    def val(k):
        """— 无静态默认值 = fork 有键但 def 未设默认（预设/代码提供）；— = fork 未见此键。"""
        if k not in meta:
            return "—"
        d = meta[k].get("default")
        if d is None:
            return "— 无静态默认值"
        return d if d != "" else "（空）"

    if len(keyset) > 1:
        pairs = ["`%s` (%s)" % (k, val(k)) for k in keyset]
        lines.append("[Defaults]%s: %s." % (link_d, ", ".join(pairs)))
        rngs = ["`%s` (%s)" % (k, range_str(meta[k])) for k in found if range_str(meta[k])]
        if rngs:
            lines.append("[Ranges]%s: %s." % (link_r, ", ".join(rngs)))
    else:
        k = keyset[0] if keyset else None
        if k in meta:
            v = val(k)
            lines.append("[Default]%s: `%s`." % (link_d, v)
                         if not v.startswith("—") else "[Default]%s: %s." % (link_d, v))
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
        # 幂等：Type 与 CLI 之间已有 [Default(s)]
        j = i + 1
        while j < len(lines) and not RE_CLI_LINE.match(lines[j]):
            if RE_HAS_DEFAULT.match(lines[j]):
                skipped += 1; break
            j += 1
        else:
            # 回溯找本小节 [Variable(s)] 行取键；找不到用文件名主干
            keys = None
            for b in range(i - 1, max(i - 6, -1), -1):
                if RE_VAR_LINE.match(lines[b]):
                    keys = RE_KEY_TOKEN.findall(lines[b])
                    if keys:
                        break
            if not keys:
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
# audit
# ---------------------------------------------------------------------------

def norm(v):
    return re.sub(r"[\s,]+", "", str(v or "")).strip("`")


def cmd_audit(args):
    meta = json.load(open(args.json, encoding="utf-8"))["keys"]
    issues = {"no_default_line": [], "default_drift": [], "key_not_in_json": [],
              "choice_no_options": []}
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
                for k in keys:
                    if k not in meta:
                        continue
                    exp = meta[k].get("default")
                    if exp in (None, ""):
                        continue
                    if ("`%s`" % norm(exp)) not in dline and norm(exp) not in dline:
                        issues["default_drift"].append(
                            "%s:%d %s 期望 %s 实际 %s" % (rel, i + 1, k, exp, dline.strip()))
            for k in keys:
                if k not in meta:
                    issues["key_not_in_json"].append("%s (%s)" % (rel, k))
            if "Choice" in ln:
                window = "\n".join(lines[i:i + 4])
                if "[Options]" not in window and "[Options]" not in "\n".join(lines[max(0, i - 1):i]):
                    issues["choice_no_options"].append("%s:%d" % (rel, i + 1))
        n_pages += 1
        if not has_default_any and any(RE_TYPE_LINE.match(l) for l in lines):
            pass
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

    j = sub.add_parser("inject", help="向键页内插 [Default]/[Range]/[Aliases]")
    j.add_argument("pages", nargs="*", help="页面路径")
    j.add_argument("--group", help="目录（如 wiki/setting/filament/cooling）")
    j.add_argument("--all", action="store_true", help="全部键页")
    j.add_argument("--dry-run", action="store_true")
    j.add_argument("--json", default=DEFAULT_JSON)
    j.set_defaults(func=cmd_inject)

    a = sub.add_parser("audit", help="页内元数据 vs JSON 对账")
    a.add_argument("--json", default=DEFAULT_JSON)
    a.set_defaults(func=cmd_audit)

    args = ap.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
