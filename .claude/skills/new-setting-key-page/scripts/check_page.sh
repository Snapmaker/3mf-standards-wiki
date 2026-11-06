#!/usr/bin/env bash
# check_page.sh — wiki/setting 键页面规范校验（只读，不修改任何文件）
#
# 用法:
#   check_page.sh <page.md> [更多页面...]   校验指定页面（全项检查）
#   check_page.sh --all                    审计 wiki/setting 全部键页面
#
# 退出码: 0 = 全部通过(允许有 WARN)  1 = 存在 FAIL  2 = 用法错误
#
# 检查项:
#   E1 文件名 snake_case（^[a-z0-9][a-z0-9_]*\.md$，仅对 wiki/ 页面强制；docs/ 的编号中文名是既有约定）
#   E2 文件名在 wiki/ 内全局唯一（AGENTS.md 孤儿页之外的全局唯一规则）
#   E3 Location 行（前 5 行内出现 "> Location: X → Y …"，仅对 wiki/setting 页面强制）
#   E4 孤儿页（repo 内没有任何 .md 链接指向它）
#   E5 一级标题 = 文件名主干（仅对 wiki/setting 页面强制）
#   E6 页内相对 .md 链接目标存在（AGENTS.md 预留目录降级为 WARN）

set -u

# scripts/ → skill 目录 → skills → .claude → 仓库根，共四级
REPO_ROOT=$(cd "$(dirname "$0")/../../../.." && pwd) || exit 2
CALL_DIR=$PWD
cd "$REPO_ROOT" || exit 2

RESERVED_ROOTS='wiki/general_settings|wiki/cli|wiki/developer_reference|wiki/print_prepare|wiki/calibration|wiki/guides|wiki/releases'

usage() { sed -n '2,8p' "$0" | sed 's/^# \{0,1\}//'; exit 2; }

# ---- 工具函数 ---------------------------------------------------------

# resolve <源文件所在目录(仓库相对)> <原始链接目标>
# 结果写入全局变量 RESOLVED（仓库相对规范化路径）；越出仓库根时返回 1。
# 不用命令替换回传，避免每条链接 fork 一次（Windows 上代价高）。
resolve() {
  local dir=$1 raw=${2//%20/ } seg
  RESOLVED=$dir
  local IFS=/
  for seg in $raw; do
    case $seg in
      ''|.) ;;
      ..) if [[ $RESOLVED == */* ]]; then RESOLVED=${RESOLVED%/*}; else RESOLVED=''; fi ;;
      *)  if [[ -z $RESOLVED ]]; then RESOLVED=$seg; else RESOLVED="$RESOLVED/$seg"; fi ;;
    esac
  done
  [[ $RESOLVED == .* || -z $RESOLVED ]] && return 1
  return 0
}

is_reserved() { [[ $1 =~ ^($RESERVED_ROOTS)(/|$) ]]; }

fail=0; warn=0; pass=0; AGG=0   # AGG=1 (--all): 预留目录 WARN 只在索引级各报一次
say_fail() { printf '[FAIL] %s: %s\n' "$1" "$2"; fail=$((fail+1)); }
say_warn() { printf '[WARN] %s: %s\n' "$1" "$2"; warn=$((warn+1)); }
say_pass() { pass=$((pass+1)); }

# ---- 链接索引：全仓库 md 的相对链接 → 仓库相对目标（单遍构建） ------
LINK_INDEX=$(mktemp) || exit 2
trap 'rm -f "$LINK_INDEX"' EXIT

# 注意: AGENTS.md 不入索引——其中的链接是反引号内的示例, 不是真链接
grep -roE --include='*.md' '\]\([^)]+\)' wiki docs 2>/dev/null \
| while IFS= read -r line; do
    src=${line%%:*}                 # 形如 wiki/setting/printer/printer_overview.md
    tgt=${line#*:}; tgt=${tgt#](}; tgt=${tgt%)}
    tgt=${tgt%%#*}                  # 去锚点
    case $tgt in ''|http*|//*|mailto:*) continue ;; esac
    [[ $tgt == *.md ]] || continue
    srcdir=${src%/*}; [[ $srcdir == "$src" ]] && srcdir=''
    resolve "$srcdir" "$tgt" || continue
    printf '%s\n' "$RESOLVED"
  done | sort -u > "$LINK_INDEX"

declare -A LINK_SET
while IFS= read -r l; do LINK_SET[$l]=1; done < "$LINK_INDEX"

# 文件名唯一性索引（一次构建）
declare -A NAME_COUNT
while IFS= read -r n; do NAME_COUNT[$n]=$(( ${NAME_COUNT[$n]:-0} + 1 )); done \
  < <(find wiki -name '*.md' -printf '%f\n')

# ---- 单页检查 ---------------------------------------------------------
# check_page <仓库相对路径>
check_page() {
  local p=$1 base stem
  base=${p##*/}
  stem=${base%.md}
  local in_setting=0
  [[ $p == wiki/setting/* ]] && in_setting=1

  # E1 文件名（仅 wiki/ 页面）
  if [[ $p == wiki/* ]]; then
    if [[ $base =~ ^[a-z0-9][a-z0-9_]*\.md$ ]]; then say_pass
    else say_fail "$p" "E1 文件名不符 snake_case: $base"; fi
  fi

  # E2 全局唯一
  if [[ ${NAME_COUNT[$base]:-0} -gt 1 ]]; then
    say_fail "$p" "E2 文件名在 wiki/ 内不唯一: $base"
  else say_pass; fi

  # E3 Location 行 / E5 标题（读前 5 行，兼容 CRLF）
  local l1= l= found_loc=0
  { read -r l1 || true; l1=${l1%$'\r'}
    for _ in 2 3 4 5; do read -r l || true; l=${l%$'\r'}
      [[ $l == '>'\ Location:* ]] && found_loc=1
    done
  } < "$p"
  if (( in_setting )); then
    if (( found_loc )); then say_pass; else say_fail "$p" "E3 前 5 行缺少 '> Location: …' 行"; fi
    if [[ $l1 == "# $stem" ]]; then say_pass; else say_fail "$p" "E5 一级标题('$l1')应为 '# $stem'"; fi
  fi

  # E4 孤儿页
  if [[ ${LINK_SET[$p]+set} ]]; then say_pass
  else say_fail "$p" "E4 孤儿页: 没有任何 .md 链接到它 (AGENTS.md 孤儿页规则)"; fi

  # E6 页内链接可达
  local n_ok=0 pdir=${p%/*}
  while IFS= read -r line; do
    local tgt=${line#*(}; tgt=${tgt%)}
    tgt=${tgt%%#*}
    resolve "$pdir" "$tgt" || continue
    [[ -f $RESOLVED ]] && { n_ok=$((n_ok+1)); continue; }
    if is_reserved "$RESOLVED"; then
      (( AGG )) || say_warn "$p" "E6 链接目标暂不存在(预留目录, AGENTS.md): $tgt"
    else
      say_fail "$p" "E6 链接目标不存在: $tgt"
    fi
  done < <(grep -oE '\]\([^)]+\.md[^)]*\)' "$p" 2>/dev/null)
  (( n_ok > 0 )) && say_pass
}

# ---- 入口 -------------------------------------------------------------
if [[ ${1:-} == '--all' ]]; then
  AGG=1
  total=0
  while IFS= read -r p; do
    ((total++))
    check_page "$p"
  done < <(find wiki/setting -name '*.md' ! -name '*_overview.md' | sort)
  # 索引级补查: 全部链接目标的存在性(预留目录降级)
  while IFS= read -r t; do
    [[ -f $t ]] && continue
    if is_reserved "$t"; then say_warn "$t" "E6 链接目标暂不存在(预留目录)"
    else say_fail "$t" "E6 链接目标不存在(被某页引用)"
    fi
  done < "$LINK_INDEX"
  printf -- '--\n审计 %d 个键页面: PASS %d  FAIL %d  WARN %d\n' "$total" "$pass" "$fail" "$warn"
  (( fail > 0 )) && exit 1
  exit 0
elif [[ $# -ge 1 && $1 != -* ]]; then
  for p in "$@"; do
    case $p in /*) ;; *) p="$CALL_DIR/$p" ;; esac
    p=${p#"$REPO_ROOT"/}
    [[ -f $p ]] || { printf '[FAIL] %s: 文件不存在\n' "$p"; exit 1; }
    check_page "$p"
  done
  printf -- '--\n校验 %d 个页面: PASS %d  FAIL %d  WARN %d\n' "$#" "$pass" "$fail" "$warn"
  (( fail > 0 )) && exit 1
  exit 0
else
  usage
fi
