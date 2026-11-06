# 09 对账：PrintConfig 元数据提取与键页注入

> 调研基线：fork 源码 `src/libslic3r/PrintConfig.cpp` + `PrintConfig.hpp`（commit `f77ec1f8`，2026-11-06）；wiki 侧 525 个键页面（不含 3 个总览页）。
> 回答的问题：**键页四件套（Mode/Variable/Type/CLI Example）之外，fork `ConfigOptionDef` 还提供哪些元数据？如何以脚本化、可复跑的方式补进键页？**
> 状态：filament/cooling 20 页已按新格式试点注入，其余 ~505 页待团队批准模板后批量注入。

## 1. 结论

- 键页可补三项元数据：**默认值（Default）**、**取值范围+单位（Range）**、**兼容别名（Aliases）**；Choice 页另有 **[Options]** 枚举值（既有标签，本次未改动）。
- 全部数据由 `print_config_tools.py extract` 从 fork 源码提取，落档 `docs/data/print_config_metadata.json`（含 `source_commit` 溯源），注入由 `inject` 子命令完成，`audit` 子命令对账——不依赖手工誊抄，防 wiki 与源码漂移。
- fork 实测 `aliases` 仅 1 处（`inner_wall_speed` ← `perimeter_feed_rate`）：OrcaSlicer 已清除 PrusaSlicer 的大量历史别名，**Aliases 是"存在才注入"的个发行**，不是批量行。

## 2. 提取口径与统计

提取器：`.claude/skills/new-setting-key-page/scripts/print_config_tools.py extract <PrintConfig.cpp 路径>`（fork checkout 位置各人不同，路径必传）。

解析处理：剥块/行注释（39 处注释键、22 处注释 max）；`def = this->add("key", …)` 与 `new_def(...)` 宏两种定义起点；宽松正则容忍无空格/tab/对齐写法；剥 `L()` 壳并合并多行字符串；`set_default_value(...)` 方法调用式取值（`60.0f`→`60.0`、`60.`→`60`）。

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
- 显示规则三分：有值 → 值；fork 有键但 def 未设默认 → `— 无静态默认值`；fork 无此键 → `—`。
- 默认值字面量归一化（自查补充）：`60.0f`→`60.0`、`60.`→`60`；枚举常量经 `s_keys_map_*` 静态映射翻译为用户可见串（如 `(int)Overhang_threshold_bridge`→`95%`、`btAutoBrim`→`auto_brim`）；点类型 `Vec2d(a, b)`→`a×b`；`FloatOrPercent{50., true}`→`50%`。hpp 宏注册的枚举（`fvtStandard`、`ipMonotonic` 等）无映射表，保留常量名——它即配置文件里的存储值。
- 多键小节页镜像复数惯例：`[Defaults]: `key1` (80), `key2` (—)`，顺序跟随 [Variables] 行。
- **与方案的偏差**：原方案 Range = min/max/sidetext 任一存在即注入；实施收窄为 **min/max 任一存在**（仅 sidetext 的"单位行"信息量为零）。单边界显示 `≥ x` / `≤ x`。
- 校验：`check_page.sh` 新增 E7（有 [Type] 行的完整页须配 [Default(s)] 行，WARN；`--all` 聚合计数）。

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

## 5. 待团队裁决

| # | 问题 | 建议 |
|---|---|---|
| Q1 | 内插式格式（含 `—` 三分显示、多键页 `[Defaults]` 复数样式）是否批准为标准模板 | 批准后 `inject --all` 刷剩余 ~505 页 |
| Q2 | E7 是否从 WARN 升级为 FAIL（全量注入完成后） | 建议升级，防止新页漏注入 |
| Q3 | [Options] 补全取 `enum_values` 还是 `enum_labels`（如 `auto_brim` vs 显示文本） | 建议以 `enum_values` 为准（与 CLI/JSON 一致），labels 可后补 |
| Q4 | Mode 取值不一致：页内有 `Expert`（上游叫法 6 处）vs fork 枚举 `Simple/Advanced/Developer` | 建议统一为 fork 枚举名 |
| Q5 | §4 的 25 个 fork 无键小节如何处理 | 建议小节头部加 `> [!WARNING] fork 未实现此参数`，正文保留上游内容 |
| Q6 | 24 个占位页是否统一升级为新格式 | 建议保持"基本信息"结构，仅补 [Default] 链接化 |

## 6. 工具用法备忘

```bash
# 提取（fork 路径各人不同；产出到 docs/data/print_config_metadata.json）
python .claude/skills/new-setting-key-page/scripts/print_config_tools.py extract <fork>/src/libslic3r/PrintConfig.cpp

# 注入（单页 / 整组 / 全量；--dry-run 预览；幂等）
python .claude/skills/new-setting-key-page/scripts/print_config_tools.py inject --group wiki/setting/filament/cooling

# 对账（值漂移 / Choice 缺 Options / 页键在 JSON 缺失 / 缺 [Default] 行）
python .claude/skills/new-setting-key-page/scripts/print_config_tools.py audit
```

JSON 过期判定：`meta.source_commit` 与 fork 当前 HEAD 不一致时需重跑 extract（页面注入不依赖 fork，只依赖 repo 内 JSON）。
