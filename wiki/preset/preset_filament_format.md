# 耗材预设文件格式 v1.0（草案）

← [Wiki 首页](../home.md)

相关：[耗材预设](preset_filament_format.md) · [工艺预设](preset_process_format.md) · [打印机预设](preset_machine_format.md)

> 规范性用语：**应 / 不应**表示要求，**宜 / 不宜**表示推荐，**可**表示允许。

## 目录

- [前言](#前言)
- [引言](#引言)
- [1 范围](#1-范围)
- [2 术语和定义](#2-术语和定义)
- [3 总体结构](#3-总体结构)
- [4 文件格式与元数据](#4-文件格式与元数据)
  - [4.1 JSON 与元数据](#41-json-与元数据)
  - [4.2 预设示例](#42-预设示例)
  - [4.3 参数值的序列化](#43-参数值的序列化)
- [5 参数字典](#5-参数字典)
  - [5.1 耗材丝](#51-耗材丝)
  - [5.2 冷却](#52-冷却)
  - [5.3 参数覆盖](#53-参数覆盖)
  - [5.4 高级](#54-高级)
  - [5.5 材料](#55-材料)
  - [5.6 依赖](#56-依赖)
  - [5.7 注释](#57-注释)
- [6 一致性要求](#6-一致性要求)
- [深入阅读](#深入阅读)

## 前言

本规范规定 Snapmaker Orca 耗材系统预设的文件格式和一致性要求，适用于预设的使用、开发和维护。

## 引言

耗材预设以 JSON 对象保存元数据和配置参数。相关预设可通过继承复用设置，厂商清单负责登记需要加载的预设。本文依次说明文件组织、序列化形式、参数字典和一致性检查。预设的命名与继承规则见 [打印配置文件命名与继承规范](configuration_files.md)。

## 1 范围

本页面介绍 Snapmaker Orca **耗材系统预设**的文件组织、字段和值的写法，供使用、开发和维护预设的人员查阅。预设文件位于 `Snapmaker/filament/`，JSON 中的 `type` 为 `"filament"`。

参数字典列出界面设置项；预设还可包含元数据和其他非界面字段。

## 2 术语和定义

| 术语 | 含义 |
|---|---|
| 基础预设 | `instantiation` 为字符串 `"false"`，用于提供共享配置 |
| 实例 | `instantiation` 为字符串 `"true"`，用于选择或绑定具体配置 |
| 继承 | `inherits` 按名称引用父预设；子项覆盖父项的同名键，未指定的参数继续回退到父项或内置默认值 |

## 3 总体结构

系统文件放在 `Snapmaker/filament/`。相邻的厂商清单 `Snapmaker.json` 通过 `filament_list` 的 `name` 和 `sub_path` 登记预设；新增或改名时应同步核对清单及引用。清单还包含 `machine_model_list`；`machine_model` 是型号登记文件，不属于 `type: machine` 配置树。

## 4 文件格式与元数据

### 4.1 JSON 与元数据

文件应为合法 JSON 对象；文件使用 UTF-8，读取既有文件时宜兼容 UTF-8 BOM。键名应使用本页面列出的标准拼写和大小写。文件名去除 `.json` 后应与 `name` 一致，并符合目标操作系统的文件名规则。

| 字段 | 写法与用途 |
|---|---|
| `type` | 字符串 `"filament"`，与目录和预设类别对应 |
| `name` | 非空字符串，标识预设；与文件名及清单名称对应 |
| `from` | 系统预设使用字符串 `"system"` |
| `instantiation` | 系统预设使用字符串 `"true"` 或 `"false"`，不是 JSON 布尔值 |
| `inherits` | 父预设的 `name`；根预设可省略；父项应可解析且不得形成循环 |
| `setting_id` | 设置标识；可省略，填写时宜保持稳定 |
| `version`、`renamed_from` | 可选版本与历史名称元数据；应遵循所在预设集现有约定 |
| `filament_id` | 耗材实体标识，可在父层定义；不可与 `setting_id` 混为一谈 |
| [`compatible_printers`](../settings/filament/dependencies/compatible_printers.md) | 兼容打印机预设名称的字符串数组；具体实例宜明确列出相应机器配置名称 |
| [`compatible_printers_condition`](../settings/filament/dependencies/compatible_printers_condition.md) | 可选的打印机兼容性条件表达式；列表为空且表达式非空时用于判断兼容性 |

兼容性判断还可能受到厂商排除规则等因素影响；列表和条件表达式均为空时通常不限定打印机。

元数据与切片参数不是同一类字段；字段是否存在取决于基础层或实例层。基础预设可以不携带 `setting_id` 或 `inherits`。

### 4.2 预设示例

以下示例展示继承基础预设的实例；其他参数可由父预设提供。

```json
{
  "type": "filament",
  "name": "Generic ABS @U1 0.2 nozzle",
  "from": "system",
  "instantiation": "true",
  "inherits": "Generic ABS @U1 base",
  "setting_id": "GFSB99",
  "compatible_printers": [
    "Snapmaker U1 (0.2 nozzle)"
  ],
  "filament_type": [
    "ABS"
  ],
  "nozzle_temperature": [
    "270"
  ]
}
```

### 4.3 参数值的序列化

参数字典中的逻辑类型和默认值描述参数含义，不一定能直接用作 JSON 字面量。系统预设通常把数值、布尔和枚举序列化为字符串，向量写为字符串数组，例如 `"layer_height": "0.2"`、`"wipe": ["0"]`；百分比值可写成 `"15%"`。特殊字段应按目标版本支持的格式及同类预设确认。

复数类型一般表示向量，不是多选；索引语义取决于字段：打印机挤出机页面的相关向量按挤出机槽位使用，耗材页面按当前耗材槽使用；带 `flow_support` 的字段还涉及流量级别，不能一概按挤出机解释。`points`、`point`、多行 G-code、特殊枚举和覆盖项应按各自序列化实现处理，不能机械地按类型名称推断 JSON 结构。`nullable` 标记逻辑上的自动或不覆盖。对于支持空值的回抽覆盖项，系统预设可使用字符串 `"nil"`，例如 `"filament_retraction_length": ["nil"]`；它不同于 JSON 的 `null`，其他字段应确认各自的写法。

## 5 参数字典

下表按界面页面和分组顺序列出设置项；预设还可包含隐藏参数、历史字段和扩展字段。表中列出显示名、逻辑类型、默认值、范围、候选值和特殊标记。默认值是逻辑默认值，不代表当前文件中必须出现，也不一定是完整继承后的最终值。缺少边界表示表中未列出边界，不表示实现一定没有其他约束。标有“可编辑候选”的 `values` 是建议选项，允许输入其他值；没有该标记的候选值也应结合对应字段的实现判断。未建键页的键（元数据字段、Developer 键，以及未挂入三个设置 Tab 的键）以纯代码键名标注，其说明以本页为准。

类型名称中，`bool`、`int`、`float`、`string` 和 `enum` 分别表示布尔、整数、浮点数、文本和枚举；复数形式表示向量。`percent` 表示百分数，`float_or_percent` 可表示数值或百分比。`flow_support` 表示字段支持按流量变体（flow variant）取多个值：数组首项为 `standard`，第二项为 `high_flow`；具体顺序由本模块的 `filament_flow_support` 声明（见 5.4 流量支持）。`nullable` 表示该值可处于自动或不覆盖状态。

表中 `范围/候选/标记` 的数值约束也以逻辑值表示；部分字段的显示或可用状态取决于其他设置；界面中隐藏或禁用字段不意味着该字段在文件中非法。

### 5.1 耗材丝

#### 基础信息

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`filament_type`](../settings/filament/filament/filament_type.md) | 类型 | `strings` | `["PLA"]` | values=["ABS","ABS-GF","ASA","ASA-Aero","BVOH","PCTG","EVA","FLEX","HIPS","PA","PA-CF","PA-GF","PA6-CF","PA11-CF","PC","PC-CF","PCTG","PE","PE-CF","PET-CF","PETG","PETG-CF","PETG-CF10","PETG-GF","PHA","PLA","PLA-AERO","PLA-CF","PP","PP-CF","PP-GF","PPA-CF","PPA-GF","PPS","PPS-CF","PVA","PVB","SBS","TPU"]; 可编辑候选 |
| [`filament_vendor`](../settings/filament/filament/filament_vendor.md) | 供应商 | `strings` | `["(Undefined)"]` | — |
| [`filament_soluble`](../settings/filament/filament/filament_soluble.md) | 可溶性材料 | `bools` | `[false]` | — |
| [`filament_is_support`](../settings/filament/filament/filament_is_support.md) | 支撑材料 | `bools` | `[false]` | — |
| `filament_is_high_temperature` | 高温耗材 | `bools` | `[false]` | — |
| [`required_nozzle_HRC`](../settings/filament/filament/required_nozzle_hrc.md) | 喷嘴硬度要求 | `ints` | `[0]` | min=0; max=500 |
| [`default_filament_colour`](../settings/filament/filament/default_filament_colour.md) | 缺省颜色 | `strings` | `[""]` | — |
| [`filament_diameter`](../settings/filament/filament/filament_diameter.md) | 直径（mm） | `floats` | `[1.75]` | min=0 |
| [`filament_density`](../settings/filament/filament/filament_density.md) | 密度（g/cm³） | `floats` | `[0]` | min=0 |
| [`filament_shrink`](../settings/filament/filament/filament_shrink.md) | 收缩率（XY）（%） | `percents` | `[100]` | min=10 |
| [`filament_shrinkage_compensation_z`](../settings/filament/filament/filament_shrinkage_compensation_z.md) | 收缩率（Z）（%） | `percents` | `[100]` | min=10 |
| [`filament_cost`](../settings/filament/filament/filament_cost.md) | 价格（money/kg） | `floats` | `[0]` | min=0 |
| [`temperature_vitrification`](../settings/filament/filament/temperature_vitrification.md) | 软化温度（℃） | `ints` | `[100]` | — |
| [`idle_temperature`](../settings/filament/filament/idle_temperature.md) | 待机温度（℃） | `ints` | `[0]` | min=0; max=1500 |
| [`filament_tower_interface_pre_extrusion_dist`](../settings/filament/filament/filament_tower_interface_pre_extrusion_dist.md) | 接触层预挤出距离（mm） | `floats` | `[10]` | min=0 |
| [`filament_tower_interface_pre_extrusion_length`](../settings/filament/filament/filament_tower_interface_pre_extrusion_length.md) | 接触层预挤出长度（mm） | `floats` | `[0]` | min=0 |
| [`filament_tower_interface_print_temp`](../settings/filament/filament/filament_tower_interface_print_temp.md) | 接触层打印温度（°C） | `ints` | `[-1]` | min=-1 |
| [`filament_tower_ironing_area`](../settings/filament/filament/filament_tower_ironing_area.md) | 擦拭塔熨烫面积（mm²） | `floats` | `[4]` | min=0 |
| [`filament_adhesiveness_category`](../settings/filament/filament/filament_adhesiveness_category.md) | 粘接性类别 | `ints` | `[100]` | min=0 |
| [`nozzle_temperature_range_low`](../settings/filament/filament/nozzle_temperature_range_low.md) | 最小（℃） | `ints` | `[190]` | min=0; max=1500 |
| [`nozzle_temperature_range_high`](../settings/filament/filament/nozzle_temperature_range_high.md) | 最大（℃） | `ints` | `[240]` | min=0; max=1500 |

#### 流量和压力提前

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`pellet_flow_coefficient`](../settings/filament/filament/pellet_flow_coefficient.md) | 颗粒流动系数 | `floats` | `[0.4157]` | min=0 |
| [`filament_flow_ratio`](../settings/filament/filament/filament_flow_ratio.md) | 流量比例 | `floats` | `[1]` | min=0; max=2; flow_support |
| [`enable_pressure_advance`](../settings/filament/filament/enable_pressure_advance.md) | 启用压力提前 | `bools` | `[false]` | flow_support |
| [`pressure_advance`](../settings/filament/filament/pressure_advance.md) | 压力提前 | `floats` | `[0.02]` | max=2; flow_support |
| [`adaptive_pressure_advance`](../settings/filament/filament/adaptive_pressure_advance.md) | 启用自适应压力提前（实验） | `bools` | `[false]` | — |
| [`adaptive_pressure_advance_bridges`](../settings/filament/filament/adaptive_pressure_advance_bridges.md) | 桥接压力提前 | `floats` | `[0]` | max=2 |
| [`adaptive_pressure_advance_model`](../settings/filament/filament/adaptive_pressure_advance_model.md) | 自适应压力提前测量值（实验） | `strings` | `["0,0,0\n0,0,0"]` | — |
| [`adaptive_pressure_advance_overhangs`](../settings/filament/filament/adaptive_pressure_advance_overhangs.md) | 启用悬垂自适应压力提前（实验） | `bools` | `[false]` | — |

#### 打印仓温度

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`chamber_temperature`](../settings/filament/filament/chamber_temperature.md) | 机箱温度（℃） | `ints` | `[0]` | min=0; max=1500 |
| [`activate_chamber_temp_control`](../settings/filament/filament/activate_chamber_temp_control.md) | 激活温度控制 | `bools` | `[false]` | — |

#### 打印温度

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`nozzle_temperature_initial_layer`](../settings/filament/filament/nozzle_temperature_initial_layer.md) | 首层（℃） | `ints` | `[200]` | min=0; max=1500; flow_support |
| [`nozzle_temperature`](../settings/filament/filament/nozzle_temperature.md) | 其它层（℃） | `ints` | `[200]` | min=0; max=1500; flow_support |

#### 床温

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`supertack_plate_temp_initial_layer`](../settings/filament/filament/supertack_plate_temp_initial_layer.md) | 首层（℃） | `ints` | `[35]` | min=0; max=120 |
| [`supertack_plate_temp`](../settings/filament/filament/supertack_plate_temp.md) | 其它层（℃） | `ints` | `[35]` | min=0; max=120 |
| [`cool_plate_temp_initial_layer`](../settings/filament/filament/cool_plate_temp_initial_layer.md) | 首层（℃） | `ints` | `[35]` | min=0; max=120 |
| [`cool_plate_temp`](../settings/filament/filament/cool_plate_temp.md) | 其它层（℃） | `ints` | `[35]` | min=0; max=300 |
| [`textured_cool_plate_temp_initial_layer`](../settings/filament/filament/textured_cool_plate_temp_initial_layer.md) | 首层（℃） | `ints` | `[40]` | min=0; max=120 |
| [`textured_cool_plate_temp`](../settings/filament/filament/textured_cool_plate_temp.md) | 其它层（℃） | `ints` | `[40]` | min=0; max=300 |
| [`eng_plate_temp_initial_layer`](../settings/filament/filament/eng_plate_temp_initial_layer.md) | 首层（℃） | `ints` | `[45]` | min=0; max=300 |
| [`eng_plate_temp`](../settings/filament/filament/eng_plate_temp.md) | 其它层（℃） | `ints` | `[45]` | min=0; max=300 |
| [`hot_plate_temp_initial_layer`](../settings/filament/filament/hot_plate_temp_initial_layer.md) | 首层（℃） | `ints` | `[45]` | max=300 |
| [`hot_plate_temp`](../settings/filament/filament/hot_plate_temp.md) | 其它层（℃） | `ints` | `[45]` | min=0; max=300 |
| [`textured_plate_temp_initial_layer`](../settings/filament/filament/textured_plate_temp_initial_layer.md) | 首层（℃） | `ints` | `[45]` | min=0; max=300 |
| [`textured_plate_temp`](../settings/filament/filament/textured_plate_temp.md) | 其它层（℃） | `ints` | `[45]` | min=0; max=300 |
| [`graphic_effect_plate_temp_initial_layer`](../settings/filament/filament/graphic_effect_plate_temp_initial_layer.md) | 首层（℃） | `ints` | `[0]` | min=0; max=300 |
| [`graphic_effect_plate_temp`](../settings/filament/filament/graphic_effect_plate_temp.md) | 其它层（℃） | `ints` | `[0]` | min=0; max=300 |

#### 体积速度限制

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`filament_max_volumetric_speed`](../settings/filament/filament/filament_max_volumetric_speed.md) | 最大体积速度（mm³/s） | `floats` | `[2]` | min=0; flow_support |

### 5.2 冷却

#### 特定层冷却

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`close_fan_the_first_x_layers`](../settings/filament/cooling/close_fan_the_first_x_layers.md) | 关闭冷却对前（层） | `ints` | `[1]` | min=0; max=1000 |
| [`full_fan_speed_layer`](../settings/filament/cooling/full_fan_speed_layer.md) | 满速风扇在（层） | `ints` | `[0]` | min=0; max=1000 |

#### 部件冷却风扇

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`fan_min_speed`](../settings/filament/cooling/fan_min_speed.md) | 风扇速度（%） | `floats` | `[20]` | min=0; max=100; flow_support |
| [`fan_cooling_layer_time`](../settings/filament/cooling/fan_cooling_layer_time.md) | 层时间（s） | `floats` | `[60]` | min=0; max=1000 |
| [`fan_max_speed`](../settings/filament/cooling/fan_max_speed.md) | 风扇速度（%） | `floats` | `[100]` | min=0; max=100; flow_support |
| [`slow_down_layer_time`](../settings/filament/cooling/slow_down_layer_time.md) | 层时间（s） | `floats` | `[5]` | min=0; max=1000 |
| [`reduce_fan_stop_start_freq`](../settings/filament/cooling/reduce_fan_stop_start_freq.md) | 保持风扇常开 | `bools` | `[false]` | — |
| [`slow_down_for_layer_cooling`](../settings/filament/cooling/slow_down_for_layer_cooling.md) | 降低打印速度 以得到更好的冷却 | `bools` | `[true]` | — |
| [`dont_slow_down_outer_wall`](../settings/filament/cooling/dont_slow_down_outer_wall.md) | 不减速外墙 | `bools` | `[false]` | — |
| [`slow_down_min_speed`](../settings/filament/cooling/slow_down_min_speed.md) | 最小打印速度（mm/s） | `floats` | `[10]` | min=0 |
| [`enable_overhang_bridge_fan`](../settings/filament/cooling/enable_overhang_bridge_fan.md) | 悬垂/桥接强制冷却 | `bools` | `[true]` | — |
| [`overhang_fan_threshold`](../settings/filament/cooling/overhang_fan_threshold.md) | 悬垂冷却激活阈值 | `enums` | `["95%"]` | values=["0%","10%","25%","50%","75%","95%"] |
| [`overhang_fan_speed`](../settings/filament/cooling/overhang_fan_speed.md) | 悬垂和外部桥接风扇速度（%） | `ints` | `[100]` | min=0; max=100 |
| [`internal_bridge_fan_speed`](../settings/filament/cooling/internal_bridge_fan_speed.md) | 内部桥接风扇速度（%） | `ints` | `[-1]` | min=-1; max=100 |
| [`support_material_interface_fan_speed`](../settings/filament/cooling/support_material_interface_fan_speed.md) | 支撐接触面风扇（%） | `ints` | `[-1]` | min=-1; max=100 |
| [`ironing_fan_speed`](../settings/filament/cooling/ironing_fan_speed.md) | 熨烫风扇速度（%） | `ints` | `[-1]` | min=-1; max=100 |

#### 辅助部件冷却风扇

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`additional_cooling_fan_speed`](../settings/filament/cooling/additional_cooling_fan_speed.md) | 风扇速度（%） | `ints` | `[0]` | min=0; max=100; flow_support |

#### 排气风扇

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`activate_air_filtration`](../settings/filament/cooling/activate_air_filtration.md) | 启用空气过滤/排气 | `bools` | `[false]` | — |
| [`during_print_exhaust_fan_speed`](../settings/filament/cooling/during_print_exhaust_fan_speed.md) | 风扇速度（%） | `ints` | `[60]` | min=0; max=100 |
| [`complete_print_exhaust_fan_speed`](../settings/filament/cooling/complete_print_exhaust_fan_speed.md) | 风扇速度（%） | `ints` | `[80]` | min=0; max=100 |

### 5.3 参数覆盖

#### 回抽

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`filament_retraction_length`](../settings/filament/setting_overrides/filament_retraction_length.md) | 长度（mm） | `floats` | `[null]` | nullable; flow_support |
| [`filament_z_hop`](../settings/filament/setting_overrides/filament_z_hop.md) | Z抬升高度（mm） | `floats` | `[null]` | min=0; max=5; nullable |
| [`filament_z_hop_types`](../settings/filament/setting_overrides/filament_z_hop_types.md) | Z抬升类型 | `enums` | `[null]` | values=["Auto Lift","Normal Lift","Slope Lift","Spiral Lift"]; nullable; flow_support |
| [`filament_retract_lift_above`](../settings/filament/setting_overrides/filament_retract_lift_above.md) | 仅在高度以上抬Z（mm） | `floats` | `[null]` | min=0; nullable |
| [`filament_retract_lift_below`](../settings/filament/setting_overrides/filament_retract_lift_below.md) | 仅在高度以下抬Z（mm） | `floats` | `[null]` | min=0; nullable |
| [`filament_retract_lift_enforce`](../settings/filament/setting_overrides/filament_retract_lift_enforce.md) | 仅表面抬Z | `enums` | `[null]` | values=["All Surfaces","Top Only","Bottom Only","Top and Bottom"]; nullable |
| [`filament_retraction_speed`](../settings/filament/setting_overrides/filament_retraction_speed.md) | 回抽速度（mm/s） | `floats` | `[null]` | nullable; flow_support |
| [`filament_deretraction_speed`](../settings/filament/setting_overrides/filament_deretraction_speed.md) | 装填速度（mm/s） | `floats` | `[null]` | nullable; flow_support |
| [`filament_retract_restart_extra`](../settings/filament/setting_overrides/filament_retract_restart_extra.md) | 额外回填长度（mm） | `floats` | `[null]` | nullable |
| [`filament_retraction_minimum_travel`](../settings/filament/setting_overrides/filament_retraction_minimum_travel.md) | 空驶距离阈值（mm） | `floats` | `[null]` | nullable |
| [`filament_retract_when_changing_layer`](../settings/filament/setting_overrides/filament_retract_when_changing_layer.md) | 换层时回抽 | `bools` | `[null]` | nullable |
| [`filament_wipe`](../settings/filament/setting_overrides/filament_wipe.md) | 回抽时擦拭 | `bools` | `[null]` | nullable |
| [`filament_wipe_distance`](../settings/filament/setting_overrides/filament_wipe_distance.md) | 擦拭距离（mm） | `floats` | `[null]` | min=0; nullable; flow_support |
| [`filament_retract_before_wipe`](../settings/filament/setting_overrides/filament_retract_before_wipe.md) | 擦拭前的回抽量（%） | `percents` | `[null]` | nullable |
| [`filament_long_retractions_when_cut`](../settings/filament/setting_overrides/filament_long_retractions_when_cut.md) | 切料时回抽（实验） | `bools` | `[null]` | nullable |
| [`filament_retraction_distances_when_cut`](../settings/filament/setting_overrides/filament_retraction_distances_when_cut.md) | 切料回抽距离 | `floats` | `[null]` | min=10; max=18; nullable |
| [`filament_retract_length_toolchange`](../settings/filament/setting_overrides/filament_retract_length_toolchange.md) | Retraction Length (Toolchange)（mm） | `floats` | `[null]` | nullable; flow_support |
| [`filament_retract_restart_extra_toolchange`](../settings/filament/setting_overrides/filament_retract_restart_extra_toolchange.md) | 额外回填长度（mm） | `floats` | `[null]` | nullable |

### 5.4 高级

#### 耗材丝起始G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`filament_start_gcode`](../settings/filament/advanced/filament_start_gcode.md) | 起始G-code | `strings` | `[" "]` | — |

#### 耗材丝结束G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`filament_end_gcode`](../settings/filament/advanced/filament_end_gcode.md) | 结尾G-code | `strings` | `[" "]` | — |

#### 流量支持（非界面键）

该字段声明本预设支持的流量变体及其顺序：数组首项为 `standard`，其后为 `high_flow` 等变体。带 `flow_support` 标记的多值参数按同一顺序排列，首值属于 `standard`；未提供的变体在参数中可写作字符串 `nil`，与数字 `0` 不同。字段取值为字符串数组，与 [gcode.3mf 交互字段](../specification/gcode.3mf/gcode_3mf_interaction_fields.md#31-流量类型族) 的 `process_flow_support` 描述一致。

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| `filament_flow_support` | 耗材流量支持 | `strings` | `["standard"]` | values=["standard","high_flow"]; 非界面键（Developer 级） |

### 5.5 材料

#### 色塔参数

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`filament_minimal_purge_on_wipe_tower`](../settings/filament/multimaterial/filament_minimal_purge_on_wipe_tower.md) | 擦拭塔上的最小清理量（mm³） | `floats` | `[15]` | min=0; flow_support |

#### 单挤出机多材料打印机的换色参数

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`filament_loading_speed_start`](../settings/filament/multimaterial/filament_loading_speed_start.md) | 加载初始速度（mm/s） | `floats` | `[3]` | min=0 |
| [`filament_loading_speed`](../settings/filament/multimaterial/filament_loading_speed.md) | 加载速度（mm/s） | `floats` | `[28]` | min=0 |
| [`filament_unloading_speed_start`](../settings/filament/multimaterial/filament_unloading_speed_start.md) | 卸载初始速度（mm/s） | `floats` | `[100]` | min=0 |
| [`filament_unloading_speed`](../settings/filament/multimaterial/filament_unloading_speed.md) | 卸载速度（mm/s） | `floats` | `[90]` | min=0 |
| [`filament_toolchange_delay`](../settings/filament/multimaterial/filament_toolchange_delay.md) | 卸载后延迟（s） | `floats` | `[0]` | min=0 |
| [`filament_cooling_moves`](../settings/filament/multimaterial/filament_cooling_moves.md) | 冷却移动次数 | `ints` | `[4]` | max=20 |
| [`filament_cooling_initial_speed`](../settings/filament/multimaterial/filament_cooling_initial_speed.md) | 第一次冷却移动的速度（mm/s） | `floats` | `[2.2]` | min=0 |
| [`filament_cooling_final_speed`](../settings/filament/multimaterial/filament_cooling_final_speed.md) | 最后一次冷却移动的速度（mm/s） | `floats` | `[3.4]` | min=0 |
| [`filament_stamping_loading_speed`](../settings/filament/multimaterial/filament_stamping_loading_speed.md) | 尖端成型加载速度 | `floats` | `[0]` | min=0 |
| [`filament_stamping_distance`](../settings/filament/multimaterial/filament_stamping_distance.md) | 从冷却管中心测量的尖端成型距离 | `floats` | `[0]` | min=0 |
| [`filament_ramming_parameters`](../settings/filament/multimaterial/filament_ramming_parameters.md) | 尖端成型参数 | `strings` | `["120 100 6.6 6.8 7.2 7.6 7.9 8.2 8.7 9.4 9.9 10.0\| 0.05 6.6 0.45 6.8 0.95 7.8 1.45 8.3 1.95 9.7 2.45 10 2.95 7.6 3.45 7.6 3.95 7.6 4.45 7.6 4.95 7.6"]` | — |

#### 多挤出机多材料打印机的换色参数

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`filament_multitool_ramming`](../settings/filament/multimaterial/filament_multitool_ramming.md) | 启用多色尖端成型设置 | `bools` | `[false]` | flow_support |
| [`filament_multitool_ramming_volume`](../settings/filament/multimaterial/filament_multitool_ramming_volume.md) | 多色尖端成型体积（mm³） | `floats` | `[10]` | min=0; flow_support |
| [`filament_multitool_ramming_flow`](../settings/filament/multimaterial/filament_multitool_ramming_flow.md) | 多色尖端成型流量（mm³/s） | `floats` | `[10]` | min=0; flow_support |

### 5.6 依赖

#### 兼容打印机

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`compatible_printers`](../settings/filament/dependencies/compatible_printers.md) | 选择打印机 | `strings` | `[]` | — |
| [`compatible_printers_condition`](../settings/filament/dependencies/compatible_printers_condition.md) | 条件 | `string` | `""` | — |

#### 兼容的切片配置

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`compatible_prints`](../settings/filament/dependencies/compatible_prints.md) | 选择配置文件 | `strings` | `[]` | — |
| [`compatible_prints_condition`](../settings/filament/dependencies/compatible_prints_condition.md) | 条件 | `string` | `""` | — |

### 5.7 注释

#### 注释

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`filament_notes`](../settings/filament/notes/filament_notes.md) | 耗材注释 | `strings` | `[""]` | — |

## 6 一致性要求

生产或修改预设时应检查：

1. JSON 可解析，文件名、`name`、`type`、目录及厂商清单相互对应。
2. `inherits` 能找到同类父项，继承链无环；改名时同步更新子项、清单和引用。
3. 参数使用目标版本支持的键与序列化形态；按完整继承结果检查类型、范围和相互约束。
4. 实例的适配关系、名称、标识和实际参数一致；默认工艺及型号引用可解析。
5. 检查 UI 条件以及特殊序列化，再使用目标版本 Snapmaker Orca 加载并验证。

## 深入阅读

- 命名、元数据与继承规则见 [打印配置文件命名与继承规范](configuration_files.md)。
