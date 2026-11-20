# 09 对账：PrintConfig 元数据提取与键页注入

> 调研基线：fork 源码 `src/libslic3r/PrintConfig.cpp` + `PrintConfig.hpp`（commit `f77ec1f8`，2026-11-06）；wiki 侧 525 个键页面（不含 3 个总览页）。
> 回答的问题：**键页四件套（Mode/Variable/Type/CLI Example）之外，fork `ConfigOptionDef` 还提供哪些元数据？如何以脚本化、可复跑的方式补进键页？**
> 状态：2026-11-06 全量完成。525 键页全部注入元数据行（含试点 20 页），缺键小节加 WARNING 横幅，Mode 对账修正，占位页默认值填充，E7 升级 FAIL。§5 各项已按建议执行完毕。

## 1. 结论

- 键页可补三项元数据：**默认值（Default）**、**取值范围+单位（Range）**、**兼容别名（Aliases）**；Choice 页另有 **[Options]** 枚举值（既有标签，本次未改动）。
- 全部数据由 `print_config_tools.py extract` 从 fork 源码提取，落档 `docs/data/print_config_metadata.json`（含 `source_commit` 溯源），注入由 `inject` 子命令完成，`audit` 子命令对账——不依赖手工誊抄，防 wiki 与源码漂移。
- fork 实测 `aliases` 仅 1 处（`inner_wall_speed` ← `perimeter_feed_rate`）：OrcaSlicer 已清除 PrusaSlicer 的大量历史别名，**Aliases 是"存在才注入"的个发行**，不是批量行。

## 2. 提取口径与统计

提取器：`.claude/skills/new-setting-key-page/scripts/print_config_tools.py extract <PrintConfig.cpp 路径>`（fork checkout 位置各人不同，路径必传）。

解析处理：剥块/行注释（39 处注释键、22 处注释 max）；`def = this->add("key", …)` 与 `new_def(...)` 宏两种定义起点；宽松正则容忍无空格/tab/对齐写法；剥 `L()` 壳并合并多行字符串；`set_default_value(...)` 方法调用式取值（`60.0f`→`60.0`、`60.`→`60`）。

**2026-11-20 口径修正（同字段取值与块截断）**：① 同字段重复赋值由"取首值"改为"取末值"，对齐 C++ 赋值语义——修复 `filament_cooling_moves`（源码 `max = 0` 死代码行后紧跟 `max = 20`，首值把笔误当真值，页面 Range 曾错显 `≤ 0`，实际 `≤ 20`）；② 块先在下一个 `def = this->add(`（含动态键，锚定 add 而非任意 `def =`，避免 `auto 别名 = def = add` 形式被拦腰截断）处截断再取值——顺带清掉三处存量漏入垃圾：`filament_notes`（min 0/max 500 实为 `required_nozzle_HRC` 的，其大写键名不构成字面量边界）、`has_scarf_joint_seam`（sidetext mm/s、min 0 实为 `machine_max_speed_*` 动态键的）、`nozzle_volume_type`（min 1 实为 `project_schema` 动态键的）。重提取后全量 diff 仅上述 4 键变化；`filament_cooling_moves` 页已重注入，audit `default_drift` 0。

**2026-11-20 修复（`L()` 宏壳漏入默认值 + audit 漏报）**：`parse_default` 此前未剥默认值里的 `L()` 本地化宏壳（§2 口径文字早有承诺、代码未兑现），全源码唯一受害键 `filament_vendor`（`set_default_value(new ConfigOptionStrings{L("(Undefined)")})`）——宏壳原样漏进 JSON 与键页。修复后重提取，diff 除该键默认值 `L("(Undefined)")` → `(Undefined)` 外无变化。同时修 audit `default_drift` 的漏报根因：原比对为"整行拍平后子串包含"，`L(Undefined)` 含子串 `Undefined` 导致宏壳类漂移必然漏网，改为取值部分（首个冒号后、剥行尾句点）拍平等值比较——修前对旧页恰好报出这 1 条真阳性、误报 0。顺带修正 audit 新揪出的 4 页存量 `mode_drift`（`filament_tower_interface_pre_extrusion_dist` / `_length` / `filament_tower_interface_print_temp` / `filament_tower_ironing_area`，页标 Advanced、fork 源码均 `comDevelop`），全量 audit 五类问题归零（`key_not_in_json` 18 条为 §3 已记录待裁决的 resonance 镜像块，不计）。

| 项 | 本次提取 | Explore 手工统计 | 差异说明 |
|---|---|---|---|
| 键总数 | 844 | 818 静态 + 18 动态 | 844 = 806（cpp 字面+宏）+ 20（hpp 宏补位）+ 18（filament_* 派生）；手工数 818 含计数口径差（重复定义按一次计） |
| min / max 非空 | 363 / 156 | 367 / 157 | 手工数为源码出现次数（含 1 处动态拷贝行、重复定义）；提取数为唯一键首匹配 |
| sidetext 非空 | 307 | 204 | 口径差（自查修正）：Explore 所引 41 处 `sidetext = ""` **全部在注释里**，剥注释后 311 处赋值全部非空（唯一键 303 + 派生克隆 12）；Explore 的 204 为注释计入且非空判定正则更窄 |
| aliases | 1 | 1 | 一致 |
| enum_values 行 | 262 | 277 | 手工数含 `enum_keys_map` 相邻行；提取只收 push_back/emplace_back 实际值行 |
| nocli | 42 | 43 | 1 处重复定义 |

三种键来源：

1. **cpp 定义**（806）：`this->add()`/`new_def()`，元数据最全。
2. **hpp 宏补位**（20）：`PRINT_CONFIG_CLASS_DEFINE` 的 `((ConfigOptionXxx, key))` 序列——machine limits 族（`machine_max_{acceleration,speed,jerk}_{x,y,z,e}` 等，默认值由机器预设 JSON 提供）、`required_nozzle_HRC`（宏内声明为大写，JSON 已归一为小写并保留 `declared_as`）等。这些键**有键无静态默认值**，页面上显示 `— 无静态默认值`。
3. **派生键**（18）：`filament_<retract 系列>`，由打印机级键循环拷贝（PrintConfig.cpp L6612-6637），min/max/sidetext 同源键，`derived: true`，默认值未克隆。

跳过的动态键（3 处调用点）：`project_schema.config_key`、宏体 `OPT_KEY`、`add_nullable` 循环（派生键已按源键克隆补齐）。

## 3. 注入格式（试点已落地，待团队批准）

位置：**内插式**——[Type] 行与 [CLI Example] 行之间；四件套既有行字节不动，diff 纯增量。

```markdown
[Mode](…): `Simple`.  
[Variable](…): `complete_print_exhaust_fan_speed`.  
[Type](…): `Integer list`.  
[Default](…#default-value): `80`.  
[Range](…#range): `0–100` %.          ← 仅 min/max 存在时注入
[Aliases](…#aliases): `perimeter_feed_rate`.   ← 仅存在时注入
[CLI Example](…): `--complete-print-exhaust-fan-speed=80`.  
```

- 新行链接统一指向 `general_settings/option_type.md` 预留页的约定锚点（`#default-value` / `#range` / `#aliases`），建页时按锚点写标题。
- 显示规则三分：有值 → 值；fork 有键但 def 未设默认 → `— no static default`；fork 无此键 → `—`（空串默认 → `(empty)`）。**2026-11-19 用户裁决：`wiki/settings/` 全目录页面改全英文**，标记从中文（`— 无静态默认值`/`（空）`）换为上述英文写法，全量 220+ 页已转换（含占位页模板、Status/Visibility/G-code embedded name/Also in this section 标注行、三个总览页）；inject 脚本与 SKILL.md 模板同步。
- 默认值字面量归一化（自查补充）：`60.0f`→`60.0`、`60.`→`60`；枚举常量经 `s_keys_map_*` 静态映射翻译为用户可见串（如 `(int)Overhang_threshold_bridge`→`95%`、`btAutoBrim`→`auto_brim`）；点类型 `Vec2d(a, b)`→`a×b`；`FloatOrPercent{50., true}`→`50%`。hpp 宏注册的枚举（`fvtStandard`、`ipMonotonic` 等）无映射表，保留常量名——它即配置文件里的存储值。
- ~~多键小节页镜像复数惯例：`[Defaults]: `key1` (80), `key2` (—)`，顺序跟随 [Variables] 行。~~ **2026-11-19 用户裁决废止**：键页元数据行（Variable/Type/Default/Range/CLI Example）只保留本键自己的值、一律单数标签，`[CLI Example]` 只用本键 kebab-case 旗标，不再捆小节兄弟键、不再带 `(same pattern...)` 尾注；兄弟键交叉引用走"本小节同时涵盖"行与各自键页。当日起全量收敛 131 页（含 `[Modes]` 双行结构坍缩 20 页、错键名块修正 9 页；`inject` 脚本同步改为恒取文件名主干键）。页内镜像的**非本键小节**（如 resonance_avoidance 页内的 Input Shaping 块、junction_deviation 交叉块）原样保留，待团队裁决。
- **与方案的偏差**：原方案 Range = min/max/sidetext 任一存在即注入；实施收窄为 **min/max 任一存在**（仅 sidetext 的"单位行"信息量为零）。单边界显示 `≥ x` / `≤ x`。~~此收窄已废止，见下方 2026-11-20 裁决①~~
- 校验：`check_page.sh` 新增 E7（有 [Type] 行的完整页须配 [Default(s)] 行，WARN；`--all` 聚合计数）。
- **2026-11-20 版式裁决**（用户审核通过，`migrate --all [--fold]` 全量执行 461+450 页）：
  1. **新增 `[Unit]` 行**（取 `sidetext`，仅存在时注入），`[Range]` 不再内嵌单位——废止上文"仅 sidetext 信息量为零"的收窄：单位同时限定 `[Default]`，且覆盖无 min/max 的键（实测新注入 258 行）；
  2. **元数据块与说明正文之间强制空行**：此前所有行以行尾双空格硬换行连成同一段落，正文说明粘成"第 8 个分类"，无法区分（本次修复 463+ 处）；
  3. **孤立 `## <UI 标签>` 标题废止**，UI 标签折进 Location 第 4 段（`Tab → 分组 → UI 区块 → UI 标签`）：450 完整页折叠，占位页维持三段；多小节内容页（如 line_width 的 `## Line Types`）保留内容标题；
  4. **元数据 8 类定案**：Mode / Variable / Type / Default / Unit / Range / Aliases / CLI Example，不精简（Variable 虽与 H1 键名同值，保留其"可用于自定义 G-code 占位符"的链接语义）。
  5. **元数据行固定顺序**（同日追加裁决）：`Mode → Variable → Type → Default → Unit → Range → Aliases → Options → CLI Example`，全库一致，缺省跳过。全量核查 476 个元数据块相对顺序零违规（观感差异均为字段缺席所致）；audit 增 `field_order` 项、migrate 增自动重排兜底（负向测试验证可抓乱序与重复）。**同日二次追加（用户指出 filament_colour 占位页）**：占位页 bullet 格式（`- Label/Mode/Type/Default`）原本不在行序管辖内且模板 B 把 Mode 排末位——32 页统一为 `Label 置顶 > Mode > Type > Default`（Label 为占位页独有身份字段），audit `field_order` 与 migrate A3 通道同步覆盖 bullet 格式；顺带清除提取器行话残留（`full_label same`、`the source sidetext lists mm only`，3 处）。
  6. **键页不出现仓库代码内容**（同日用户指示，源自 filament_colour.md）：占位页标题去 "(from fork \`PrintConfig.cpp\)" 括注（32 页）；Type 行 `coXxx` 原始类型名映射为用户术语（31 页，如 coStrings→Text list；"GUIType=color"→"color picker"、"max_literal"→"max"）；正文剔除源文件名/类名（Tab.cpp、FilamentColorDialog、wxColourDialog，3 页）；"this fork / the fork" 措辞改 **Snapmaker Orca**（3 页）。枚举常量值（`ipMonotonicLine` 等）是配置文件实际存储值，保留；上游纯文字引用（upstream PR 12669）按 2026-11-19 裁决保留；用户内容警示（硬件/CPU 类 WARNING callout）不受影响。banner 子命令横幅文案同步改为英文用户术语（"Not available in this software version"，不再出现"源码"字样，兼容旧文案幂等识别）。**同日扩展至支撑页**：四件套（option_type/option_mode/cli_mode/built_in_placeholders_variables，清除 `src/…` 路径、`coXxx`/`comXxx` 枚举名、`def->` 字段、仓库位置、"fork 源码"措辞，改"软件内置/当前软件版本"表述）、三个总览页题注（Tab.cpp `build` 方法名 → "actual software UI"）、home.md 设置区说明（`PrintConfig.cpp` 元数据 → 软件内置元数据）；AGENTS.md 文风节成文，`specification/` 规范正文的源码引用不受影响。占位页 `> Tooltip (original):` 标记同步去括注为 `> Tooltip:`（26 页——"Tooltip:"本身已表明是软件提示原文，"(original)"是维护者视角来源标记，对读者是噪音）。占位页收尾 `(To add: …)` 行清除（32 处）：模板默认套话直接删（24 处，Status 行已表明待补全），页面专属补全线索转 HTML 注释 `<!-- TODO: … -->`（8 处，读者渲染不可见、补全者仍可见）。
  7. **占位页升格完整页格式**（同日裁决，源自 graphic_effect_plate_temp 与 filament_cost 风格对比）：占位页 bullet 基本信息结构与完整页元数据行结构双风格并存，根源是"上游 wiki 是否写过"而非内容多少。`promote` 子命令把 32 页占位页升格为完整页格式——元数据行（Mode/Variable/Type/Default/Unit/Range/Options/Aliases/CLI）全部由 repo 内 JSON 生成（Mode 无定义显示 `—`；coXxx→用户类型名映射；Choice 页自动补 [Options] 行取 enum_values），tooltip 文本作为正文起点，取值说明括注含链接/代码段时自动转为正文句（"% relative to X" → "A % value is X."），`%%` 还原 `%`；`> Status:` 行保留维持 🚧 跟踪与总览标记；Setting Overrides 的 18 页 cross-reference 页是独立格式不受影响。升格后 [Type] 小节 463→495，audit choice_no_options 由 promote 自动消化，check WARN 21→18（3 个 plate 占位页 Location 段数问题随升格消失）。**Mode 缺省口径修正**（同日）：5 个键源码未显式设置档位（graphic_effect_plate_temp、nozzle_temperature_range_high/low、pellet_flow_coefficient、tree_support_adaptive_layer_height），升格初版显示 `—`；框架默认为 comSimple（Config.hpp `ConfigOptionDef::mode` 初值），实际 UI 即 Simple 档——promote 缺省映射改为 `Simple`，5 页已改，option_mode.md 补"未指定档位的键按 Simple 处理"说明。**无正文页补齐**（同日）：7 页元数据后无描述——extract 增捕 `tooltip` 字段（648 键，JSON 其余零漂移）、promote 对页面漏抄 tooltip 的键回退 JSON（retraction_distances_when_cut、skirt_type 由此补上）；源码本无 tooltip 的 5 页手写一句话描述（nozzle_temperature_range_high/low、z_hop_when_prime、first/other_layers_sequence_choice）；全库"元数据后无正文"页清零。
  8. **无元数据块历史页升格**（同日裁决，源自 filament_ramming_parameters 空页）：33 页无 [Type] 无 Status 的历史页（多仅 1–2 行正文）由 promote 遗留分支统一升格为完整页格式——元数据全取 JSON；首个标题与 label/UI 区块同名则折叠、内容标题（如 min_bead_width 的 Arachne 节）保留且 tooltip 描述插其前；正文类名行话同步清理（RammingDialog → the ramming dialog）。配套：hpp 宏键类型名 `ConfigOptionXxx` 归一映射后查表、`coPercent(s)` 补录；extract 修复相邻字符串字面量拼接（ramming 默认值引号残渣，全库仅此 1 键漂移）。`extruders_count` 为 GUI 层动态选项、非注册配置键，保持最小页不编造元数据。machine_max_{speed,acceleration,jerk}_{x..e} 12 页 Location 第 4 段统一为轴字母（替代"区块名→区块名"重复）。升格后 [Type] 小节 495→515，"无正文页"保持 0。
  - 配套：`extract` 增捕 `label` 字段（851 键中 677 有，供后续 Location 第 4 段对账）；`audit` 增 unit_missing / unit_drift / range_unit_leftover 三项（迁移后全部归零）；`check_page.sh` 增 E8（完整页 Location 须 4 段 FAIL，占位/说明页 ≥3 段 WARN——现存 3 处 WARN 为 plate 目录占位页既有段数缺失，待补全时修）；镜像小节（Variable 键≠页主干，如 resonance_avoidance 页内 Input Shaping 块）迁移时原样保留，仅手工剥除 4 处 machine_max_jerk_* 镜像块的 Range 残留单位。

## 4. fork 缺键清单（25 个，页面显示 `—` 的全部来源）

以下键在 wiki 键页的 [Variables] 行出现，但 fork 全源码（src/ + resources/）零引用——均为**上游 OrcaSlicer 功能、fork 未实现**：

| 类别 | 键 | 涉及页面数 |
|---|---|---|
| Input Shaping | `input_shaping_{emit,freq_x,freq_y,damp_x,damp_y,type}` | 3 |
| 流量比例族 | `{first_layer,inner_wall,outer_wall,sparse_infill,support,support_interface,internal_solid_infill,gap_fill,overhang}_flow_ratio`、`set_other_flow_ratios` | 3 |
| 多材质指定 | `outer_wall_filament_id`、`sparse_infill_filament_id`、`internal_solid_filament_id` | 各 1 |
| 空气过滤多态 | `activate_air_filtration_on_completion`、`activate_air_filtration_during_print`（fork 只有单一 `activate_air_filtration`） | 各 1 |
| 首层加速度/Jerk | `initial_layer_travel_acceleration`、`initial_layer_travel_jerk` | 1 |
| 腔温 | `chamber_minimal_temperature` | 2 |
| 耗材塔 | `filament_tower_interface_purge_volume` | 5 |

这些小节是建页时照抄上游 wiki 的内容，**本变更只标注不删改**（是否删除/加警示横幅属于内容决策，待裁决）。

## 5. 裁决项与执行结果（2026-11-06 按建议全部执行）

| # | 问题 | 决议/结果 |
|---|---|---|
| Q1 | 内插式格式是否批准为标准模板 | ✅ 已全量执行：`inject --all` 430 页 + 试点 20 页 = 450 个含 [Type] 小节的页面全部注入 |
| Q2 | E7 是否从 WARN 升级为 FAIL | ✅ 已升级（check_page.sh），当前 E7 违规 0 |
| Q3 | [Options] 补全取值口径 | ✅ 空操作：audit 实测 Choice 页缺 [Options] 为 0（既有 [Options] 行已全覆盖）；行内取值以 `enum_values` 为准（与 CLI/JSON 一致），值为上游显示文本的留待后续人工对账 |
| Q4 | Mode 取值不一致 | ✅ 单键小节已修正 6 文件（`filament_tower`/`retract_*_toolchange` 族，页标与 fork 可见级真实差异）；`Expert` 6 处当时全在 fork 无键小节、随 Q5 横幅处理暂不改名——**2026-11-19 按用户指示改判**：全库统一为 fork 叫法 `Develop`（实测共 14 文件 20 处，非原记 6 处：input_shaping 族 6 处 + scarf/seam_slope `[Modes]` 行 14 处；`scarf_joint_flow_ratio` 在 fork 为 `comDevelop`，同小节其余 10 键 `comAdvanced` 与页面标注相符）；**混合模式小节**（`filament_tower` 区块 purge=Advanced + tower=Developer）单行 [Mode] 无法表达，audit 已静音，留待模板升级 [Modes] 逐键样式 |
| Q5 | 25 个 fork 无键小节 | ✅ 20 页小节头部加 `> [!WARNING] fork 未实现` 横幅，正文保留 |
| Q6 | 24 个占位页 | ✅ 保持"基本信息"结构；默认值 `—` 全部按 JSON 填充真实值（21/24 页原为 `—`，实际 fork 有默认值；2 个 notes 页为空串），漂移复核 0 |

全量执行后验证：`check_page.sh --all` FAIL=0（E7 计 0），audit 的 default_drift/mode_drift/no_default_line 全部归零；key_not_in_json 62 条即 §4 缺键清单在页面上的映射（多页交叉列举同键）。

执行中发现并修复的问题：`required_nozzle_HRC.md` 大小写不一致（git 规范名大写 vs 全部内链小写，Windows 大小写不敏感 FS 掩盖已久，`git checkout` 重写目录项后暴露）——已两步 `git mv` 规范为小写；字符串型默认值带引号显示（thumbnails 等 4 页）——extract 增加整串字符串字面量处理。

## 6. 工具用法备忘

```bash
# 提取（fork 路径各人不同；产出到 docs/data/print_config_metadata.json）
python .claude/skills/new-setting-key-page/scripts/print_config_tools.py extract <fork>/src/libslic3r/PrintConfig.cpp

# 注入（单页 / 整组 / 全量；--dry-run 预览；幂等）
python .claude/skills/new-setting-key-page/scripts/print_config_tools.py inject --group wiki/settings/filament/cooling

# 版式迁移（既有键页：Unit 拆分 / 正文空行分隔；--fold 折 UI 标签进 Location 第 4 段；幂等）
python .claude/skills/new-setting-key-page/scripts/print_config_tools.py migrate --all [--fold] [--dry-run]

# 对账（值漂移 / Unit 缺失与漂移 / Range 残留单位 / 元数据行序 / Choice 缺 Options / 页键在 JSON 缺失 / 缺 [Default] 行）
python .claude/skills/new-setting-key-page/scripts/print_config_tools.py audit
```

JSON 过期判定：`meta.source_commit` 与 fork 当前 HEAD 不一致时需重跑 extract（页面注入不依赖 fork，只依赖 repo 内 JSON）。
