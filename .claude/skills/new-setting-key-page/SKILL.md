---
name: new-setting-key-page
description: 新增或更新 wiki/setting/ 下的设置参数键文档（printer/filament/process 三目录，每键一页）。当用户要求"加一个参数页 / 键文档 / 占位页"、"补某个参数的说明"、批量生成或修订设置键页面、或更新 *_overview.md 总览索引时使用。查询参数含义本身不需要本 skill，直接读对应页面即可。
---

# 新增/更新设置键文档

## 适用范围

- **适用**：在 `wiki/setting/{printer,filament,process}/<分组>/<键名>.md` 新建页面；修订既有键页内容；把 🚧 占位页补成完整页；更新对应 `*_overview.md` 索引。
- **不适用**：3mf 规范正文（`wiki/specification/`）、预设体系（`wiki/preset/`）、只是查某个参数是什么意思（直接读页面）。

## 输入清单（缺项先问用户，禁止编造）

| 输入 | 用途 | 缺失时 |
|---|---|---|
| 键名（config key，snake_case） | 文件名、标题、Variable 字段 | 问用户或从 `PrintConfig.cpp` 查证 |
| 所属 Tab + UI 分组 | 定位子目录、Location 三段路径 | 查对应 `*_overview.md` 的分组表 |
| 内容来源 | 决定 ✅ 完整页还是 🚧 占位页 | 查上游 wiki（见步骤 2） |

## 步骤

### 1. 定位

1. Tab → 顶层目录：printer / filament / process。
2. 分组 → 二级子目录（如 `basic_information/`、`extruder/`、`quality/`）。以对应 `*_overview.md` 的分组标题为准；没有合适分组时先停下来与用户确认，不要发明新目录。
3. 确认目标文件尚不存在（重名即重复键，先查 `PrintConfig.cpp` 确认真的是同一个键还是命名冲突）。

### 2. 判断页面类型

- 上游 OrcaSlicer wiki（https://github.com/OrcaSlicer/OrcaSlicer/wiki）对应 Tab 页收录了该键 → **完整页**：拷贝上游小节内容，保留四件套链接结构，索引标记 ✅。
- 上游未收录（fork 特有参数）→ **占位页**：从 fork 源码 `src/libslic3r/PrintConfig.cpp` 取该键的元数据（标签/类型/默认值/可见模式/tooltip），索引标记 🚧。fork 的 checkout 位置各人不同，不确定就问用户。
- 该键与既有页面共用同一 UI 区块（一个区块多个键）→ 在两页 Location 行下互加一行 `> 本小节同时涵盖：...`（参照 `wiki/setting/process/multimaterial/delta_temperature.md` 的写法），索引可用 🔗 交叉引用。

### 3. 生成页面

目录深度固定为 `wiki/setting/<tab>/<分组>/<键名>.md`，所以页内指向 `general_settings/` 等公共页的相对链接前缀恒为 `../../../`。

**模板 A —— 完整页**（样例：`wiki/setting/printer/basic_information/adaptive_bed_mesh_margin.md`）：

```markdown
# <键名>

> Location: <Tab> → <分组> → <UI 区块名>

---

## <UI 标签>

[Mode](../../../general_settings/option_mode.md): `<Simple|Advanced|Hidden>`.  
[Variable](../../../general_settings/built_in_placeholders_variables.md): `<键名>`.  
[Type](../../../general_settings/option_type.md#锚点): `<类型>`.  
[Default](../../../general_settings/option_type.md#default-value): `<默认值>`.  
[Range](../../../general_settings/option_type.md#range): `<min–max> <单位>`.  
[Aliases](../../../general_settings/option_type.md#aliases): `<历史键名>`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--kebab-case-键名=<示例值>`.  

<参数说明正文：拷贝/翻译上游内容，面向新人说人话>

> [!NOTE]
> <可选：注意事项，如与 Klipper 等固件的交互>
```

元数据三行（Default/Range/Aliases）**由脚本生成，不要手写**：Default 必有（fork 无此键显示 `—`，有键无静态默认显示 `— 无静态默认值`）；Range 仅 min/max 存在时注入；Aliases 仅存在时注入（fork 仅 `inner_wall_speed` 一处）。多键小节页用复数 `[Defaults]: `键1` (值), `键2` (—)`，顺序跟随 [Variables] 行。格式决策与 fork 缺键清单见 docs/09。

```markdown
# <键名>

> Location: <Tab> → <分组> → <UI 区块名>
> 状态：占位——上游 OrcaSlicer wiki 未收录，fork 特有参数，待补充。

## 基本信息（来自 fork `PrintConfig.cpp`）

- 标签：<tooltip/label 原文>
- 类型：<coFloat/…>
- 默认值：<值或 —>
- 可见模式：<简单/进阶>

> 工具提示原文：<tooltip>

（待补：参数作用、取值范围、与同类参数的关系、适用场景）
```

注意：`general_settings/`、`cli/`、`developer_reference/` 是 AGENTS.md 预留目录，链接暂时悬空属预期，校验按 WARN 处理，不要改成别的目标。

新页写完四件套后，跑单页注入补元数据行（幂等，已注入则跳过）：

```bash
python .claude/skills/new-setting-key-page/scripts/print_config_tools.py inject <页面路径>
```

数据源是 repo 内 `docs/data/print_config_metadata.json`；若其 `meta.source_commit` 落后于 fork 当前 HEAD，先重跑 `extract <fork>/src/libslic3r/PrintConfig.cpp` 再注入。

### 4. 更新总览页

在对应 `*_overview.md` 的正确分组列表末尾加一行：

```markdown
- ✅ [`<键名>`](<分组>/<键名>.md)（<UI 区块名>）
```

（完整页 ✅ / 占位页 🚧 / 交叉引用 🔗。）同时在总览页顶部的键数统计（如有）加一。

### 5. 校验（必须全过再交付）

```bash
bash .claude/skills/new-setting-key-page/scripts/check_page.sh wiki/setting/<tab>/<分组>/<键名>.md
```

检查项：E1 文件名 snake_case（英文小写）｜E2 文件名 wiki 内全局唯一｜E3 Location 行存在｜E4 非孤儿页（已被总览或其他页面链接）｜E5 标题 = 文件名主干｜E6 页内相对链接可达（预留目录降级 WARN）｜E7 有 [Type] 行的完整页须配 [Default(s)] 行（FAIL）。

批量修订后跑 `--all` 审计全部键页。

### 6. 汇报

列出：新建/修改的每个文件路径、校验输出（原文贴 FAIL/WARN 行）、遗留的 🚧 项。校验有 FAIL 时如实报告，不许静默跳过。

## 已知偏差（依据现状，非拍脑袋）

- AGENTS.md 要求"标题下第二行放面包屑"，但既有 529 个键页统一用 `> Location:` 行替代（0 页带面包屑）。本 skill 沿用现状；若团队裁决键页也要面包屑，改模板 A/B 两处即可。
- 键页中 25 个键的小节属上游内容 fork 未实现（input_shaping、flow_ratio 族等，见 docs/09 §4），Default 显示 `—`，正文暂不删改，待团队裁决。
- Mode 取值 `Expert`（6 处，上游叫法）与 fork 枚举 `Simple/Advanced/Developer` 不一致，待统一（docs/09 Q4）。
- 规则依据：AGENTS.md（命名、全局唯一、孤儿页）；页面格式依据现存 529 页的实际形态（2026-11-05 核实）；元数据行格式 2026-11-06 起以 docs/09 §3 为准。
