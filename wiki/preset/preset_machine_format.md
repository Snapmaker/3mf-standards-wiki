# 打印机预设文件格式要求 v1.0（草案）

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
  - [5.1 基础信息](#51-基础信息)
  - [5.2 打印机G-code](#52-打印机g-code)
  - [5.3 移动能力](#53-移动能力)
  - [5.4 挤出机 %d](#54-挤出机-d)
  - [5.5 材料](#55-材料)
  - [5.6 注释](#56-注释)
- [6 一致性要求](#6-一致性要求)
- [深入阅读](#深入阅读)

## 前言

本规范规定 Snapmaker Orca 打印机系统预设的文件格式和一致性要求，适用于预设的使用、开发和维护。

## 引言

打印机预设以 JSON 对象保存元数据和配置参数。相关预设可通过继承复用设置，厂商清单负责登记需要加载的预设。本文依次说明文件组织、序列化形式、参数字典和一致性检查。预设的组织与命名入门见 [打印配置文件里的命名与继承](configuration_files.md)。

## 1 范围

本页面介绍 Snapmaker Orca **打印机系统预设**的文件组织、字段和值的写法，供使用、开发和维护预设的人员查阅。预设文件位于 `Snapmaker/machine/`，JSON 中的 `type` 为 `"machine"`。

参数字典列出界面设置项；预设还可包含元数据和其他非界面字段。

## 2 术语和定义

| 术语 | 含义 |
|---|---|
| 基础预设 | `instantiation` 为字符串 `"false"`，用于提供共享配置 |
| 实例 | `instantiation` 为字符串 `"true"`，用于选择或绑定具体配置 |
| 继承 | `inherits` 按名称引用父预设；子项覆盖父项的同名键，未指定的参数继续回退到父项或内置默认值 |

## 3 总体结构

系统文件放在 `Snapmaker/machine/`。相邻的厂商清单 `Snapmaker.json` 通过 `machine_list` 的 `name` 和 `sub_path` 登记预设；新增或改名时应同步核对清单及引用。清单还包含 `machine_model_list`；`machine_model` 是型号登记文件，不属于 `type: machine` 配置树。

## 4 文件格式与元数据

### 4.1 JSON 与元数据

文件应为合法 JSON 对象；文件使用 UTF-8，读取既有文件时宜兼容 UTF-8 BOM。键名应使用本页面列出的标准拼写和大小写。文件名去除 `.json` 后应与 `name` 一致，并符合目标操作系统的文件名规则。

| 字段 | 写法与用途 |
|---|---|
| `type` | 字符串 `"machine"`，与目录和预设类别对应 |
| `name` | 非空字符串，标识预设；与文件名及清单名称对应 |
| `from` | 系统预设使用字符串 `"system"` |
| `instantiation` | 系统预设使用字符串 `"true"` 或 `"false"`，不是 JSON 布尔值 |
| `inherits` | 父预设的 `name`；根预设可省略；父项应可解析且不得形成循环 |
| `setting_id` | 设置标识；可省略，填写时宜保持稳定 |
| `version`、`renamed_from` | 可选版本与历史名称元数据；应遵循所在预设集现有约定 |
| `printer_model` | 关联的 `machine_model` 名称；实例应与型号登记一致 |
| `printer_variant` | 喷嘴变体标识，使用字符串，如 `"0.2"` |
| `default_print_profile` | 默认工艺预设名称；应指向已登记且兼容的工艺 |
| `default_filament_profile` | 默认耗材预设名称数组；切换机器时使用；应与已登记且兼容的耗材对应 |

元数据与切片参数不是同一类字段；字段是否存在取决于基础层或实例层。基础预设可以不携带 `setting_id` 或 `inherits`。

### 4.2 预设示例

以下示例展示继承基础预设的实例；其他参数可由父预设提供。

```json
{
  "type": "machine",
  "name": "Snapmaker U1 (0.4 nozzle)",
  "from": "system",
  "instantiation": "true",
  "inherits": "fdm_U1",
  "setting_id": "SM_U1",
  "printer_model": "Snapmaker U1",
  "printer_variant": "0.4",
  "default_print_profile": "0.20mm Standard @Snapmaker U1 (0.4 nozzle)",
  "nozzle_diameter": [
    "0.4",
    "0.4",
    "0.4",
    "0.4"
  ]
}
```

### 4.3 参数值的序列化

参数字典中的逻辑类型和默认值描述参数含义，不一定能直接用作 JSON 字面量。系统预设通常把数值、布尔和枚举序列化为字符串，向量写为字符串数组，例如 `"layer_height": "0.2"`、`"wipe": ["0"]`；百分比值可写成 `"15%"`。特殊字段应按目标版本支持的格式及同类预设确认。

复数类型一般表示向量，不是多选；索引语义取决于字段：打印机挤出机页面的相关向量按挤出机槽位使用，耗材页面按当前耗材槽使用；带 `flow_support` 的字段还涉及流量级别，不能一概按挤出机解释。`points`、`point`、多行 G-code、特殊枚举和覆盖项应按各自序列化实现处理，不能机械地按类型名称推断 JSON 结构。`nullable` 标记逻辑上的自动或不覆盖。对于支持空值的回抽覆盖项，系统预设可使用字符串 `"nil"`，例如 `"filament_retraction_length": ["nil"]`；它不同于 JSON 的 `null`，其他字段应确认各自的写法。

例如，可打印区域可写成 `"printable_area": ["0x0", "230x0", "230x250", "0x250"]`，每个字符串表示一个二维坐标；不要直接把字典中的坐标数组默认值当作文件字面量。多行 G-code 是 JSON 字符串，换行和引号应按 JSON 规则转义。

## 5 参数字典

下表按界面页面和分组顺序列出设置项；预设还可包含隐藏参数、历史字段和扩展字段。表中列出显示名、逻辑类型、默认值、范围、候选值和特殊标记。默认值是逻辑默认值，不代表当前文件中必须出现，也不一定是完整继承后的最终值。缺少边界表示表中未列出边界，不表示实现一定没有其他约束。标有“可编辑候选”的 `values` 是建议选项，允许输入其他值；没有该标记的候选值也应结合对应字段的实现判断。未建键页的键（元数据字段、Developer 键，以及未挂入三个设置 Tab 的键）以纯代码键名标注，其说明以本页为准。

类型名称中，`bool`、`int`、`float`、`string` 和 `enum` 分别表示布尔、整数、浮点数、文本和枚举；复数形式表示向量。`percent` 表示百分数，`float_or_percent` 可表示数值或百分比。`flow_support` 表示字段支持按流量变体（flow variant）取多个值：数组首项为 `standard`，第二项为 `high_flow`；具体顺序由本模块的 `printer_flow_support` 声明（见 5.1 流量支持）。`nullable` 表示该值可处于自动或不覆盖状态。

表中 `范围/候选/标记` 的数值约束也以逻辑值表示；部分字段的显示或可用状态取决于其他设置；界面中隐藏或禁用字段不意味着该字段在文件中非法。

### 5.1 基础信息

#### 可打印区域

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`printable_area`](../settings/printer/basic_information/printable_area.md) | 可打印区域 | `points` | `[[0,0],[200,0],[200,200],[0,200]]` | — |
| [`bed_exclude_area`](../settings/printer/basic_information/bed_exclude_area.md) | 不可打印区域 | `points` | `[[0,0]]` | — |
| [`printable_height`](../settings/printer/basic_information/printable_height.md) | 可打印高度（mm） | `float` | `100` | min=0; max=214700 |
| [`support_multi_bed_types`](../settings/printer/basic_information/support_multi_bed_types.md) | 支持多种打印床类型 | `bool` | `false` | — |
| [`nozzle_volume`](../settings/printer/basic_information/nozzle_volume.md) | 喷嘴内腔体积（mm³） | `float` | `0` | — |
| [`best_object_pos`](../settings/printer/basic_information/best_object_pos.md) | 最佳对象位置 | `point` | `[0.5,0.5]` | — |
| [`z_offset`](../settings/printer/basic_information/z_offset.md) | Z偏移（mm） | `float` | `0` | — |
| [`preferred_orientation`](../settings/printer/basic_information/preferred_orientation.md) | 零件朝向偏好（°） | `float` | `0` | min=-360; max=360 |

#### 高级

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`printer_structure`](../settings/printer/basic_information/printer_structure.md) | 打印机结构 | `enum` | `"undefine"` | values=["undefine","corexy","i3","hbot","delta"] |
| [`gcode_flavor`](../settings/printer/basic_information/gcode_flavor.md) | G-code风格 | `enum` | `"marlin"` | values=["marlin","klipper","reprapfirmware","marlin2"] |
| [`pellet_modded_printer`](../settings/printer/basic_information/pellet_modded_printer.md) | 颗粒改装打印机 | `bool` | `false` | — |
| [`bbl_use_printhost`](../settings/printer/basic_information/bbl_use_printhost.md) | 启用第三方网络连接 | `bool` | `false` | — |
| [`disable_m73`](../settings/printer/basic_information/disable_m73.md) | 禁用M73剩余打印时间 | `bool` | `false` | — |
| [`thumbnails`](../settings/printer/basic_information/thumbnails.md) | G-code缩略图尺寸 | `string` | `"48x48/PNG,300x300/PNG"` | — |
| [`use_relative_e_distances`](../settings/printer/basic_information/use_relative_e_distances.md) | 使用相对E距离 | `bool` | `true` | — |
| [`use_firmware_retraction`](../settings/printer/basic_information/use_firmware_retraction.md) | 使用固件回抽 | `bool` | `false` | — |
| [`time_cost`](../settings/printer/basic_information/time_cost.md) | 时间花费（元/时） | `float` | `0` | min=0 |
| `default_bed_type` | 默认打印板类型 | `string` | `""` | — |
| `host_type` | 主机类型 | `enum` | `"octoprint"` | values=["prusalink","prusaconnect","octoprint","duet","flashair","astrobox","repetier","mks","esp3d","crealityprint","obico","flashforge","simplyprint","elegoolink"] |
| `scan_first_layer` | 扫描首层 | `bool` | `false` | — |

#### 冷却风扇

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`fan_speedup_time`](../settings/printer/basic_information/fan_speedup_time.md) | —（s） | `float` | `0` | — |
| [`fan_speedup_overhangs`](../settings/printer/basic_information/fan_speedup_overhangs.md) | 仅悬垂 | `bool` | `true` | — |
| [`fan_kickstart`](../settings/printer/basic_information/fan_kickstart.md) | 风扇（s） | `float` | `0` | min=0 |

#### 挤出机避让空间

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`extruder_clearance_radius`](../settings/printer/basic_information/extruder_clearance_radius.md) | 半径（mm） | `float` | `40` | min=0 |
| [`extruder_clearance_height_to_rod`](../settings/printer/basic_information/extruder_clearance_height_to_rod.md) | 到横杆高度（mm） | `float` | `40` | min=0 |
| [`extruder_clearance_height_to_lid`](../settings/printer/basic_information/extruder_clearance_height_to_lid.md) | 到顶盖高度（mm） | `float` | `120` | min=0 |

#### 自适应网床

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`bed_mesh_min`](../settings/printer/basic_information/bed_mesh_min.md) | 网床最小点（mm） | `point` | `[-99999,-99999]` | — |
| [`bed_mesh_max`](../settings/printer/basic_information/bed_mesh_max.md) | 网床最大点（mm） | `point` | `[99999,99999]` | — |
| [`bed_mesh_probe_distance`](../settings/printer/basic_information/bed_mesh_probe_distance.md) | 网格点间距离（mm） | `point` | `[50,50]` | min=0 |
| [`adaptive_bed_mesh_margin`](../settings/printer/basic_information/adaptive_bed_mesh_margin.md) | 网床边缘外扩（mm） | `float` | `0` | — |

#### 配件

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`nozzle_type`](../settings/printer/basic_information/nozzle_type.md) | 喷嘴类型 | `enum` | `"undefine"` | values=["undefine","hardened_steel","stainless_steel","brass"] |
| [`nozzle_hrc`](../settings/printer/basic_information/nozzle_hrc.md) | 喷嘴洛氏硬度（HRC） | `int` | `0` | min=0; max=500 |
| [`auxiliary_fan`](../settings/printer/basic_information/auxiliary_fan.md) | 辅助部件冷却风扇 | `bool` | `false` | — |
| [`support_chamber_temp_control`](../settings/printer/basic_information/support_chamber_temp_control.md) | 支持仓温控制 | `bool` | `true` | — |
| [`support_air_filtration`](../settings/printer/basic_information/support_air_filtration.md) | 支持空气过滤 | `bool` | `true` | — |

#### 流量支持（非界面键）

该字段声明本预设支持的流量变体及其顺序：数组首项为 `standard`，其后为 `high_flow` 等变体。带 `flow_support` 标记的多值参数按同一顺序排列，首值属于 `standard`；未提供的变体在参数中可写作字符串 `nil`，与数字 `0` 不同。字段取值为字符串数组，与 [gcode.3mf 交互字段](../specification/gcode.3mf/gcode_3mf_interaction_fields.md#31-流量类型族) 的 `process_flow_support` 描述一致。

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| `printer_flow_support` | 打印机流量支持 | `strings` | `["standard"]` | values=["standard","high_flow"]; 非界面键（Developer 级） |

### 5.2 打印机G-code

#### 打印机起始G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`machine_start_gcode`](../settings/printer/machine_gcode/machine_start_gcode.md) | 起始G-code | `string` | `"G28 ; home all axes\nG1 Z5 F5000 ; lift nozzle\n"` | — |

#### 打印机结束G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`machine_end_gcode`](../settings/printer/machine_gcode/machine_end_gcode.md) | 结尾G-code | `string` | `"M104 S0 ; turn off temperature\nG28 X0  ; home X axis\nM84     ; disable motors\n"` | — |

#### 逐件打印G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`printing_by_object_gcode`](../settings/printer/machine_gcode/printing_by_object_gcode.md) | 对象之间Gcode | `string` | `""` | — |

#### 换层前G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`before_layer_change_gcode`](../settings/printer/machine_gcode/before_layer_change_gcode.md) | 换层前G-code | `string` | `""` | — |

#### 换层G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`layer_change_gcode`](../settings/printer/machine_gcode/layer_change_gcode.md) | 换层G-code | `string` | `""` | — |

#### 延时摄影G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`time_lapse_gcode`](../settings/printer/machine_gcode/time_lapse_gcode.md) | 延时摄影G-code | `string` | `""` | — |

#### 耗材丝更换G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`change_filament_gcode`](../settings/printer/machine_gcode/change_filament_gcode.md) | 耗材丝更换G-code | `string` | `""` | — |

#### 挤出类型更换G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`change_extrusion_role_gcode`](../settings/printer/machine_gcode/change_extrusion_role_gcode.md) | 挤出类型更换G-code | `string` | `""` | — |

#### 暂停 G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`machine_pause_gcode`](../settings/printer/machine_gcode/machine_pause_gcode.md) | 暂停 G-code | `string` | `""` | — |

#### 模板自定义G-code

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`template_custom_gcode`](../settings/printer/machine_gcode/template_custom_gcode.md) | 自定义 G-code | `string` | `""` | — |

### 5.3 移动能力

#### 高级

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`emit_machine_limits_to_gcode`](../settings/printer/motion_ability/emit_machine_limits_to_gcode.md) | 写入限制到G-code | `bool` | `true` | — |

#### 共振规避

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`resonance_avoidance`](../settings/printer/motion_ability/resonance_avoidance.md) | 共振规避 | `bool` | `false` | — |
| [`min_resonance_avoidance_speed`](../settings/printer/motion_ability/min_resonance_avoidance_speed.md) | 最小（mm/s） | `float` | `70` | min=0 |
| [`max_resonance_avoidance_speed`](../settings/printer/motion_ability/max_resonance_avoidance_speed.md) | 最大（mm/s） | `float` | `120` | min=0 |

#### 速度限制

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`machine_max_speed_x`](../settings/printer/motion_ability/machine_max_speed_x.md) | —（mm/s） | `floats` | `[500,200]` | min=0 |
| [`machine_max_speed_y`](../settings/printer/motion_ability/machine_max_speed_y.md) | —（mm/s） | `floats` | `[500,200]` | min=0 |
| [`machine_max_speed_z`](../settings/printer/motion_ability/machine_max_speed_z.md) | —（mm/s） | `floats` | `[12,12]` | min=0 |
| [`machine_max_speed_e`](../settings/printer/motion_ability/machine_max_speed_e.md) | —（mm/s） | `floats` | `[120,120]` | min=0 |

#### 加速度限制

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`machine_max_acceleration_x`](../settings/printer/motion_ability/machine_max_acceleration_x.md) | —（mm/s²） | `floats` | `[1000,1000]` | min=0 |
| [`machine_max_acceleration_y`](../settings/printer/motion_ability/machine_max_acceleration_y.md) | —（mm/s²） | `floats` | `[1000,1000]` | min=0 |
| [`machine_max_acceleration_z`](../settings/printer/motion_ability/machine_max_acceleration_z.md) | —（mm/s²） | `floats` | `[500,200]` | min=0 |
| [`machine_max_acceleration_e`](../settings/printer/motion_ability/machine_max_acceleration_e.md) | —（mm/s²） | `floats` | `[5000,5000]` | min=0 |
| [`machine_max_acceleration_extruding`](../settings/printer/motion_ability/machine_max_acceleration_extruding.md) | —（mm/s²） | `floats` | `[1500,1250]` | min=0 |
| [`machine_max_acceleration_retracting`](../settings/printer/motion_ability/machine_max_acceleration_retracting.md) | —（mm/s²） | `floats` | `[1500,1250]` | min=0 |
| [`machine_max_acceleration_travel`](../settings/printer/motion_ability/machine_max_acceleration_travel.md) | —（mm/s²） | `floats` | `[0,0]` | min=0 |

#### 抖动限制

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`machine_max_jerk_x`](../settings/printer/motion_ability/machine_max_jerk_x.md) | —（mm/s） | `floats` | `[10,10]` | min=0 |
| [`machine_max_jerk_y`](../settings/printer/motion_ability/machine_max_jerk_y.md) | —（mm/s） | `floats` | `[10,10]` | min=0 |
| [`machine_max_jerk_z`](../settings/printer/motion_ability/machine_max_jerk_z.md) | —（mm/s） | `floats` | `[0.2,0.4]` | min=0 |
| [`machine_max_jerk_e`](../settings/printer/motion_ability/machine_max_jerk_e.md) | —（mm/s） | `floats` | `[2.5,2.5]` | min=0 |
| [`machine_max_junction_deviation`](../settings/printer/motion_ability/machine_max_junction_deviation.md) | —（mm） | `floats` | `[0,0]` | min=0 |

### 5.4 挤出机 %d

#### 外观

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| `extruder_colour` | 挤出机颜色 | `strings` | `[""]` | — |

#### 大小

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`nozzle_diameter`](../settings/printer/extruder/nozzle_diameter.md) | 喷嘴直径（mm） | `floats` | `[0.4]` | max=100 |

#### 层高限制

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`min_layer_height`](../settings/printer/extruder/min_layer_height.md) | 最小（mm） | `floats` | `[0.07]` | min=0 |
| [`max_layer_height`](../settings/printer/extruder/max_layer_height.md) | 最大（mm） | `floats` | `[0]` | min=0 |

#### 位置

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`extruder_offset`](../settings/printer/extruder/extruder_offset.md) | 挤出机偏移（mm） | `points` | `[[0,0]]` | — |

#### 回抽

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`retraction_length`](../settings/printer/extruder/retraction_length.md) | 长度（mm） | `floats` | `[0.8]` | — |
| [`retract_restart_extra`](../settings/printer/extruder/retract_restart_extra.md) | 额外回填长度（mm） | `floats` | `[0]` | — |
| [`retraction_speed`](../settings/printer/extruder/retraction_speed.md) | 回抽速度（mm/s） | `floats` | `[30]` | — |
| [`deretraction_speed`](../settings/printer/extruder/deretraction_speed.md) | 装填速度（mm/s） | `floats` | `[0]` | — |
| [`retraction_minimum_travel`](../settings/printer/extruder/retraction_minimum_travel.md) | 空驶距离阈值（mm） | `floats` | `[2]` | — |
| [`retract_when_changing_layer`](../settings/printer/extruder/retract_when_changing_layer.md) | 换层时回抽 | `bools` | `[false]` | — |
| [`wipe`](../settings/printer/extruder/wipe.md) | 回抽时擦拭 | `bools` | `[false]` | — |
| [`wipe_distance`](../settings/printer/extruder/wipe_distance.md) | 擦拭距离（mm） | `floats` | `[1]` | min=0 |
| [`retract_before_wipe`](../settings/printer/extruder/retract_before_wipe.md) | 擦拭前的回抽量（%） | `percents` | `[100]` | — |

#### Z轴抬升

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`retract_lift_enforce`](../settings/printer/extruder/retract_lift_enforce.md) | 仅表面抬Z | `enums` | `["All Surfaces"]` | values=["All Surfaces","Top Only","Bottom Only","Top and Bottom"] |
| [`z_hop_types`](../settings/printer/extruder/z_hop_types.md) | Z抬升类型 | `enums` | `["Slope Lift"]` | values=["Auto Lift","Normal Lift","Slope Lift","Spiral Lift"] |
| [`z_hop`](../settings/printer/extruder/z_hop.md) | Z抬升高度（mm） | `floats` | `[0.4]` | min=0; max=5 |
| [`z_hop_when_prime`](../settings/printer/extruder/z_hop_when_prime.md) | 移动到擦拭塔时Z抬升 | `bools` | `[true]` | — |
| [`travel_slope`](../settings/printer/extruder/travel_slope.md) | 空驶抬高角度（°） | `floats` | `[3]` | min=1; max=90 |
| [`retract_lift_above`](../settings/printer/extruder/retract_lift_above.md) | 仅在高度以上抬Z（mm） | `floats` | `[0]` | min=0 |
| [`retract_lift_below`](../settings/printer/extruder/retract_lift_below.md) | 仅在高度以下抬Z（mm） | `floats` | `[0]` | min=0 |

#### 切换材料时的回抽量

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`retract_length_toolchange`](../settings/printer/extruder/retract_length_toolchange.md) | Retraction Length (Toolchange)（mm） | `floats` | `[10]` | — |
| [`retract_restart_extra_toolchange`](../settings/printer/extruder/retract_restart_extra_toolchange.md) | 额外回填长度（mm） | `floats` | `[0]` | — |
| [`long_retractions_when_cut`](../settings/printer/extruder/long_retractions_when_cut.md) | 切料时回抽（实验） | `bools` | `[false]` | — |
| [`retraction_distances_when_cut`](../settings/printer/extruder/retraction_distances_when_cut.md) | 切料回抽距离 | `floats` | `[18]` | min=10; max=18 |

### 5.5 材料

#### 设置单挤出机多材料

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`single_extruder_multi_material`](../settings/printer/multimaterial/single_extruder_multi_material.md) | 单挤出机多材料 | `bool` | `true` | — |
| [`manual_filament_change`](../settings/printer/multimaterial/manual_filament_change.md) | 手动更换丝材 | `bool` | `false` | — |

#### 色塔

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`purge_in_prime_tower`](../settings/printer/multimaterial/purge_in_prime_tower.md) | 冲刷进擦拭塔 | `bool` | `true` | — |
| [`enable_filament_ramming`](../settings/printer/multimaterial/enable_filament_ramming.md) | 启用耗材尖端成型 | `bool` | `true` | — |
| [`ramming_line_width_ratio`](../settings/printer/multimaterial/ramming_line_width_ratio.md) | 冲刷线宽比 | `float` | `2` | — |
| [`enable_change_pressure_when_wiping`](../settings/printer/multimaterial/enable_change_pressure_when_wiping.md) | 擦拭时压力提前启用 | `bool` | `true` | — |
| [`ramming_pressure_advance_value`](../settings/printer/multimaterial/ramming_pressure_advance_value.md) | 冲刷时压力提前值 | `float` | `0` | — |

#### 单挤出机多材料参数

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`cooling_tube_retraction`](../settings/printer/multimaterial/cooling_tube_retraction.md) | 喉管位置（mm） | `float` | `91.5` | min=0 |
| [`cooling_tube_length`](../settings/printer/multimaterial/cooling_tube_length.md) | 喉管长度（mm） | `float` | `5` | min=0 |
| [`parking_pos_retraction`](../settings/printer/multimaterial/parking_pos_retraction.md) | 耗材停靠位置（mm） | `float` | `92` | min=0 |
| [`extra_loading_move`](../settings/printer/multimaterial/extra_loading_move.md) | 额外加载距离（mm） | `float` | `-2` | — |
| [`high_current_on_filament_swap`](../settings/printer/multimaterial/high_current_on_filament_swap.md) | 更换耗材挤出机大电流 | `bool` | `false` | — |

#### 高级

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`machine_load_filament_time`](../settings/printer/multimaterial/machine_load_filament_time.md) | 加载耗材丝的时间（s） | `float` | `0` | min=0 |
| [`machine_unload_filament_time`](../settings/printer/multimaterial/machine_unload_filament_time.md) | 卸载耗材丝的时间（s） | `float` | `0` | min=0 |
| [`machine_tool_change_time`](../settings/printer/multimaterial/machine_tool_change_time.md) | 换工具头所需时间（s） | `float` | `0` | min=0 |
| [`tool_change_temprature_wait`](../settings/printer/multimaterial/tool_change_temprature_wait.md) | 换头时等待温度达标 | `bool` | `true` | — |

### 5.6 注释

#### 注释

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`printer_notes`](../settings/printer/notes/printer_notes.md) | 打印机注释 | `string` | `""` | — |

## 6 一致性要求

生产或修改预设时应检查：

1. JSON 可解析，文件名、`name`、`type`、目录及厂商清单相互对应。
2. `inherits` 能找到同类父项，继承链无环；改名时同步更新子项、清单和引用。
3. 参数使用目标版本支持的键与序列化形态；按完整继承结果检查类型、范围和相互约束。
4. 实例的适配关系、名称、标识和实际参数一致；默认工艺及型号引用可解析。
5. 检查 UI 条件以及特殊序列化，再使用目标版本 Snapmaker Orca 加载并验证。

## 深入阅读

- 字段与参数页面的三方对账、未覆盖键清单与处理状态见 [10-对账-预设格式文档与参数页面](../../docs/10-对账-预设格式文档与参数页面.md)。
