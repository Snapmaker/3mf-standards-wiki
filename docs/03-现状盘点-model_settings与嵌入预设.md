# 阶段一现状盘点（续）：model_settings.config 与嵌入预设文件

> 日期：2026-09-10　数据：7 样本 + bbs_3mf.cpp 源码

## 1. model_settings.config 分层字段实测（XML 解析，非正则）

### object 层（130 个对象）

- **固定 key**：`name`、`extruder`
- **参数覆盖 key**（= project_settings 字段子集，按需覆盖，共观测 32 种）：`wall_loops`(47)、`enable_support`(21)、`support_*`(多)、`sparse_infill_*`、`skeleton_infill_density`、`skin_infill_density`、`outer_wall_*`、`brim_*`、`ironing_*`、`layer_height`、`seam_position`、`wall_generator`、`wall_sequence` 等

### part 层（515 个部件）

- **固定 key**：`name`、`matrix`(4×4)、`source_file/object_id/volume_id/offset_x|y|z`(6)、`mesh_stat`(属性×5)
- **参数覆盖 key**（观测 17 种）：`extruder`(396!)、`wall_loops`、`sparse_infill_*`、`skeleton/skin_infill_density` 等

> **关键问题 P3 实证**：同名参数覆盖同时存在于 object 层（`wall_loops`×47）和 part 层（×10），覆盖优先级（part > object > project）完全由读取代码隐含，文件内无任何声明。

### plate 层（42 个盘）

固定 key：`plater_id`、`plater_name`、`locked`、`filament_maps`、`filament_map_mode`、`thumbnail_file`、`thumbnail_no_light_file`、`top_file`、`pick_file`；条件 key：`first_layer_print_sequence`；源码另有 `curr_bed_type`、`print_sequence`、`spiral_mode`、`gcode_file`、`pattern_bbox_file`（样本未捕获全）。

### model_instance 层

仅 `object_id`、`instance_id`、`identify_id`。

### assemble 层

样本中 0 次出现（`assemble_item` 均未写入）——源码要求 `is_assemble_initialized()`，普通文件不触发。疑似条件性死代码，待确认。

## 2. 嵌入预设文件（filament/process/machine_settings_N.config）

### 结构与写入规则（已实证，对照官方预设 resources/profiles/Snapmaker/）

官方预设文件本身就是**相对父预设的差异文件**（含 `inherits` 指向父预设名，如 `Snapmaker TPU 95A HF @U1 0.4 nozzle` → `...base` → ...，且带 `setting_id`/`instantiation` 等 header）。

嵌入 3mf 的 `*_settings_N.config` 遵循同一模型，按预设状态分两种形态：

| 形态 | 触发条件 | 实测 |
|---|---|---|
| **差异存根**（2-3 字段） | 预设保留继承（`inherits` = 父预设名）→ 只写用户修改过的字段 + `inherits` | 鸡蛋托盘/SnapMates 样本 |
| **全量快照**（105-318 字段） | 继承断裂（`inherits` = 空串，预设被复制/深度修改转为自定义）→ 写全部字段 | TPU 遮阳帽/iPhone 壳样本 |

**与官方预设对照的实证结果**（TPU 遮阳帽样本 filament_settings_1，105 字段 vs 官方 `Snapmaker TPU 95A HF @U1 0.4 nozzle` 解析继承链后 108 字段）：

- embedded-only 字段：**0**（嵌入字段 100% 可被官方链解释）
- 完全一致：93 个（= 官方默认值）
- 值不同：12 个（= **用户实际修改量**，如 retraction_length 1.5→1、压力 advance 开关等）

| 文件 | 字段数 | 与 project_settings 重叠 | 独有字段 |
|---|---|---|---|
| machine_settings_1 | 133 | 125 | **`print_host`、`printhost_apikey/password/user/port/cafile`**、`inherits` 等 8 |
| process_settings_1 | 319 | 316 | `compatible_printers*`、`inherits` 等 3 |
| filament_settings_N | 106 | 101 | `compatible_printers*/prints*`、`inherits` 等 5 |

### 官方预设对照的价值（方法论确认）

以官方 profiles 为基线解析继承链，可实现：
1. **提取用户修改量**：嵌入预设 − 官方解析链 = 用户真实调整（12/105 实测），这是"预设切换/参数推荐"功能的核心输入；
2. **白名单完备性自动校验**：embedded-only = 0 证明官方链可完整解释嵌入字段，该对账可做成 validate 工具的检查项；
3. **第三方转换锚点**：第三方 3mf 的预设参数可尝试收敛为"官方预设 + 差异"，大幅压缩转换映射表；
4. 这正是立项文档"参数预设库"（设备×材料×喷嘴三维索引）的既有数据基础——官方 profiles 目录已是该结构（machine 按设备×喷嘴、filament 按材料×喷嘴、process 按层高质量×设备）。

### 新发现问题（升级为 Blocker/Warning）

- **P6（Blocker，安全）**：`machine_settings_N` 结构性写入 `printhost_apikey`/`printhost_password` 等凭据字段。当前样本值为空（用户未配置打印主机），但用户一旦配置，凭据即随 3mf 分发。规范必须将凭据类字段列为强制禁入项。
- **W7**：预设 `name` 泄漏历史文件名/来源，如 `Bambu Lab H2C 0.4 nozzle(分色.3mf)`——预设名内嵌了**另一个项目的文件名**（该文件由 Bambu Studio 生成后被导入），属元数据污染。
- **W8**：预设 `version`（2.3.0.4 / 2.5.0.66 / 2.6.0.51）与软件 `version`（2.3.6）是**三套互不相干的版本号**，无文档说明语义。
- **W9**：机器预设显示 `printer_model: 'Bambu Lab H2C' / 'X1 Carbon'`——第三方导入痕迹直接固化在官方导出文件中，规范需决定是否清洗。
- **W10**：嵌入预设与 project_settings 数据 95% 重复（双写），二者不一致时语义（谁生效）未定义。

## 3. 规范含义小结

model_settings 的"参数覆盖"机制是合理的三层作用域设计，但需要规范显式化：
1. 哪些 key 允许作为覆盖项（建议：白名单 = 影响切片结果的参数，排除纯机器/G-code 输出类）；
2. 覆盖优先级 part > object > project 写入规范并供读取端校验；
3. `identify_id`、`source_*` 等结构 key 与参数覆盖 key 分命名空间，避免新增参数与结构 key 撞名。

---

## 附：两个非阻塞项说明（回应询问）

**① 25 个废弃候选逐项确认（GUI 内部/废弃候选类）**

这些是源码中仍有定义、但 7 个样本从未落盘的键，且多数有明显"被取代"迹象：如 `zhop`（已被 `filament_z_hop` 取代）、`adaptive_layer_height`（已被独立的 layer_heights_profile.txt 文件取代）、`initial_layer_height`（已被 `initial_layer_print_height` 取代）、`brim_ears`（已被 `brim_ears_detection_length/max_angle` 取代）、`makerlab_*`、`mtcpp/mstpp` 等。**为什么非阻塞**：它们不落盘，不影响规范白名单的初始集合；但正式定稿前要与切片软件团队逐个确认"确实是死代码"而不是"特定流程会写"，防止白名单漏项。属核实性工作，不改变规范框架。

**② `plate_N.json` 生成代码定位**

2.4.0 样本中出现的新条目 `Metadata/plate_1.json`（盘面布局摘要：bbox、bed_type、nozzle_diameter、对象列表，自带 `version:2`），与既有 `slice_info.config`/`model_settings.config` plate 段职责重叠。我尚未在当前这份 OrcaSlicer 源码中找到它的生成代码——可能是 2.4.0 对应的更新源码分支才有的。**为什么非阻塞**：它是个增量条目，不改变既有三文件的分析结论；但阶段二设计"配置文件职责边界"时必须决定它是收编进 plate 段、还是独立条目规范化，届时需要找到生成代码确认其完整字段集。
