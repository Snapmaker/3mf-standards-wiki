---
name: new-setting-key-page
description: 新增或更新 wiki/settings/ 下的设置参数键文档（printer/filament/process 三目录，每键一页）。当用户要求"加一个参数页 / 键文档 / 占位页"、"补某个参数的说明"、批量生成或修订设置键页面、或更新 *_overview.md 总览索引时使用。查询参数含义本身不需要本 skill，直接读对应页面即可。
---

# 新增/更新设置键文档

## 适用范围

- **适用**：在 `wiki/settings/{printer,filament,process}/<分组>/<键名>.md` 新建页面；修订既有键页内容；把 🚧 占位页补成完整页；更新对应 `*_overview.md` 索引。
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
- 上游未收录（fork 特有参数）→ **占位页**：跑 `promote` 从 repo 内 JSON 生成完整页格式骨架（见模板 B），正文以 tooltip 为起点，索引标记 🚧。fork 的 checkout 位置各人不同，不确定就问用户。
- 该键与既有页面共用同一 UI 区块（一个区块多个键）→ 在两页 Location 行下互加一行 `> Also in this section: ...`（参照 `wiki/settings/process/multimaterial/delta_temperature.md` 的写法），索引可用 🔗 交叉引用。
- **语言铁律（2026-11-19 裁决）**：`wiki/settings/` 下所有页面正文**全英文**——含标注行（`> Status:` / `> Visibility:` / `> G-code embedded name:` / `> Also in this section:`）、占位页模板、总览页；键名/代码/枚举值保持原样。

### 3. 生成页面

目录深度固定为 `wiki/settings/<tab>/<分组>/<键名>.md`，所以页内指向 `general_settings/` 等公共页的相对链接前缀恒为 `../../../`。

**模板 A —— 完整页**（样例：`wiki/settings/printer/basic_information/adaptive_bed_mesh_margin.md`）：

```markdown
# <键名>

> Location: <Tab> → <分组> → <UI 区块名> → <UI 标签>

---

[Mode](../../../general_settings/option_mode.md): `<Simple|Advanced|Develop>`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `<键名>`.  
[Type](../../../general_settings/option_type.md#锚点): `<类型>`.  
[Default](../../../general_settings/option_type.md#default-value): `<默认值>`.  
[Unit](../../../general_settings/option_type.md#unit): `<单位>`.  
[Range](../../../general_settings/option_type.md#range): `<min–max>`.  
[Aliases](../../../general_settings/option_type.md#aliases): `<历史键名>`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--kebab-case-键名=<示例值>`.  

<参数说明正文：拷贝/翻译上游内容，面向新人说人话>

> [!NOTE]
> <可选：注意事项，如与 Klipper 等固件的交互>
```

**版式铁律（2026-11-20 裁决，533 页已全量迁移）**：
- **键页不出现仓库代码内容**（2026-11-20 裁决）：不写源文件名（`Tab.cpp` 等）、类名（`FilamentColorDialog` 等）、`coXxx` 原始类型名（用用户术语：Boolean/Integer/Float/…/Choice list，见 option_type.md）；"the fork" 措辞用 **Snapmaker Orca**；上游纯文字引用（如 upstream PR 12669）仍按 2026-11-19 裁决保留；证据链归 docs/。
- **元数据行固定顺序**：`Mode → Variable → Type → Default → Unit → Range → Aliases → Options → CLI Example`，全库一致，**缺省跳过**（没有该字段的行不占位）；占位页 bullet 格式（`- Label:` / `- Mode:` / `- Type:` / `- Default:`）同样受辖，**Label 置顶**、其余同序。audit 的 `field_order` 项查行序（两种格式都查），migrate 自动重排兜底。
- **不写孤立的 `## <UI 标签>` 标题**——UI 标签是 Location 第 4 段（`Tab → 分组 → UI 区块 → UI 标签`）；多小节内容页（如 line_width 的 `## Line Types`）保留自己的内容标题，标题级别从 H2 起。
- **说明正文与元数据块之间必须空一行**——元数据行以行尾双空格硬换行连成一块，没有空行正文会粘成"第 8 个分类"。
- 元数据四行（Default/Unit/Range/Aliases）**由脚本生成，不要手写**：Default 必有（fork 无此键显示 `—`，有键无静态默认显示 `— no static default`，空串默认显示 `(empty)`）；Unit 仅源码 `sidetext` 存在时注入（复合单位原样，如 `mm or %`）；Range 仅 min/max 存在时注入且**不带单位**；Aliases 仅存在时注入（fork 仅 `inner_wall_speed` 一处）。
- 多键小节页同样**只写本键自己的单数行**（`[Variable]`/`[Default]`/`[Range]` 值均取本键），不捆绑同小节其他键，`[CLI Example]` 也只用本键的 kebab-case 旗标——兄弟键靠 `> Also in this section:` 行和各自键页交叉引用（2026-11-19 全量收敛，决议记录见 docs/09 §3）。既有键页改版式用 `migrate` 子命令，不要手改。

**模板 B —— 占位页**（2026-11-20 起与完整页同格式；全英文，2026-11-19 起）：

```markdown
# <键名>

> Location: <Tab> → <分组> → <UI 区块名> → <UI 标签>
> Status: placeholder — not covered by the upstream OrcaSlicer wiki; fork-specific; to be completed.

---

[Mode](../../../general_settings/option_mode.md): `<档位>`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `<键名>`.  
[Type](../../../general_settings/option_type.md#锚点): `<类型>`.  
[Default](../../../general_settings/option_type.md#default-value): `<默认值>`.  
[Unit](../../../general_settings/option_type.md#unit): `<单位>`.  
[Range](../../../general_settings/option_type.md#range): `<min–max>`.  
[Options](../../../general_settings/option_type.md#choice): `<枚举值>`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--kebab-case-键名=<值>`.  

<tooltip 文本作为正文起点>
```

用 `promote <页面>` 子命令从 repo 内 JSON 自动生成骨架（元数据行含 Default/Unit/Range/Options/CLI，正文取 tooltip；含链接的取值说明自动转为正文句，`%%` 还原为 `%`），手工补 Status/Visibility 等标注行与正文。补全线索用 HTML 注释留在页内（读者不可见）：`<!-- TODO: <线索> -->`。Setting Overrides 的 cross-reference 页（`Status: cross-reference` + `Parameter description` 链接）是独立格式，不用本模板。

注意：`general_settings/`、`cli/`、`developer_reference/` 的四件套支撑页已建（2026-11-19：`option_mode` / `option_type` / `built_in_placeholders_variables` / `cli_mode`），链接可达；键页正文仍可能链接 `print_prepare/` 等尚未启用的预留目录，悬空属预期，校验按 WARN 处理，不要改成别的目标。

新页写完四件套后，跑单页注入补元数据行（幂等，已注入则跳过）：

```bash
python .claude/skills/new-setting-key-page/scripts/print_config_tools.py inject <页面路径>
```

数据源是 repo 内 `docs/data/print_config_metadata.json`；若其 `meta.source_commit` 落后于 fork 当前 HEAD，先重跑 `extract <fork>/src/libslic3r/PrintConfig.cpp` 再注入。

### 4. 更新总览页

在对应 `*_overview.md` 的正确分组列表末尾加一行：

```markdown
- ✅ [`<键名>`](<分组>/<键名>.md) (<UI 区块名>)
```

（完整页 ✅ / 占位页 🚧 / 交叉引用 🔗。）同时在总览页顶部的键数统计（如有）加一。

### 5. 校验（必须全过再交付）

```bash
bash .claude/skills/new-setting-key-page/scripts/check_page.sh wiki/settings/<tab>/<分组>/<键名>.md
```

检查项：E1 文件名 snake_case（英文小写）｜E2 文件名 wiki 内全局唯一｜E3 Location 行存在｜E4 非孤儿页（已被总览或其他页面链接）｜E5 标题 = 文件名主干｜E6 页内相对链接可达（预留目录降级 WARN）｜E7 有 [Type] 行的完整页须配 [Default(s)] 行（FAIL）｜E8 Location 段数：完整页 4 段（含 UI 标签，FAIL）、占位/说明页 ≥3 段（WARN）。

批量修订后跑 `--all` 审计全部键页。

### 6. 汇报

列出：新建/修改的每个文件路径、校验输出（原文贴 FAIL/WARN 行）、遗留的 🚧 项。校验有 FAIL 时如实报告，不许静默跳过。

## 已知偏差（依据现状，非拍脑袋）

- AGENTS.md 要求"标题下第二行放面包屑"，但既有 529 个键页统一用 `> Location:` 行替代（0 页带面包屑）。本 skill 沿用现状；若团队裁决键页也要面包屑，改模板 A/B 两处即可。
- 键页中 25 个键的小节属上游内容 fork 未实现（input_shaping、flow_ratio 族等，见 docs/09 §4），Default 显示 `—`，正文暂不删改，待团队裁决。
- ~~Mode 取值 `Expert`（上游叫法）与 fork 枚举不一致，待统一~~ 已解决（2026-11-19）：全库 `Expert` 统一为 fork 叫法 `Develop`（scarf 族的 `scarf_joint_flow_ratio` 在 fork 为 `comDevelop`，input_shaping 等 fork 无键小节按档位映射；docs/09 Q4）。
- 规则依据：AGENTS.md（命名、全局唯一、孤儿页）；页面格式依据现存 529 页的实际形态（2026-11-05 核实）；元数据行格式 2026-11-06 起以 docs/09 §3 为准。
