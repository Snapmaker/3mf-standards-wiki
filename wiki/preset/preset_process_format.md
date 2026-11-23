# 工艺预设文件格式 v1.0（草案）

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
  - [5.1 质量](#51-质量)
  - [5.2 强度](#52-强度)
  - [5.3 速度](#53-速度)
  - [5.4 支撑](#54-支撑)
  - [5.5 材料](#55-材料)
  - [5.6 其他](#56-其他)
- [6 一致性要求](#6-一致性要求)
- [深入阅读](#深入阅读)

## 前言

本规范规定 Snapmaker Orca 工艺系统预设的文件格式和一致性要求，适用于预设的使用、开发和维护。

## 引言

工艺预设以 JSON 对象保存元数据和配置参数。相关预设可通过继承复用设置，厂商清单负责登记需要加载的预设。本文依次说明文件组织、序列化形式、参数字典和一致性检查。预设的命名与继承规则见 [打印配置文件命名与继承规范](configuration_files.md)。

## 1 范围

本页面介绍 Snapmaker Orca **工艺系统预设**的文件组织、字段和值的写法，供使用、开发和维护预设的人员查阅。预设文件位于 `Snapmaker/process/`，JSON 中的 `type` 为 `"process"`。

参数字典列出界面设置项；预设还可包含元数据和其他非界面字段。

## 2 术语和定义

| 术语 | 含义 |
|---|---|
| 基础预设 | `instantiation` 为字符串 `"false"`，用于提供共享配置 |
| 实例 | `instantiation` 为字符串 `"true"`，用于选择或绑定具体配置 |
| 继承 | `inherits` 按名称引用父预设；子项覆盖父项的同名键，未指定的参数继续回退到父项或内置默认值 |

## 3 总体结构

系统文件放在 `Snapmaker/process/`。相邻的厂商清单 `Snapmaker.json` 通过 `process_list` 的 `name` 和 `sub_path` 登记预设；新增或改名时应同步核对清单及引用。清单还包含 `machine_model_list`；`machine_model` 是型号登记文件，不属于 `type: machine` 配置树。

## 4 文件格式与元数据

### 4.1 JSON 与元数据

文件应为合法 JSON 对象；文件使用 UTF-8，读取既有文件时宜兼容 UTF-8 BOM。键名应使用本页面列出的标准拼写和大小写。文件名去除 `.json` 后应与 `name` 一致，并符合目标操作系统的文件名规则。

| 字段 | 写法与用途 |
|---|---|
| `type` | 字符串 `"process"`，与目录和预设类别对应 |
| `name` | 非空字符串，标识预设；与文件名及清单名称对应 |
| `from` | 系统预设使用字符串 `"system"` |
| `instantiation` | 系统预设使用字符串 `"true"` 或 `"false"`，不是 JSON 布尔值 |
| `inherits` | 父预设的 `name`；根预设可省略；父项应可解析且不得形成循环 |
| `setting_id` | 设置标识；可省略，填写时宜保持稳定 |
| `version`、`renamed_from` | 可选版本与历史名称元数据；应遵循所在预设集现有约定 |
| `compatible_printers` | 兼容打印机预设名称的字符串数组；具体实例宜明确列出相应机器配置名称 |
| `compatible_printers_condition` | 可选的打印机兼容性条件表达式；列表为空且表达式非空时用于判断兼容性 |

兼容性判断还可能受到厂商排除规则等因素影响；列表和条件表达式均为空时通常不限定打印机。

元数据与切片参数不是同一类字段；字段是否存在取决于基础层或实例层。基础预设可以不携带 `setting_id` 或 `inherits`。

### 4.2 预设示例

以下示例展示继承基础预设的实例；其他参数可由父预设提供。

```json
{
  "type": "process",
  "name": "0.08mm High Quality @Snapmaker U1 (0.2 nozzle)",
  "from": "system",
  "instantiation": "true",
  "inherits": "fdm_process_U1_0.08_nozzle_0.2",
  "setting_id": "GP122",
  "compatible_printers": [
    "Snapmaker U1 (0.2 nozzle)"
  ]
}
```

### 4.3 参数值的序列化

参数字典中的逻辑类型和默认值描述参数含义，不一定能直接用作 JSON 字面量。系统预设通常把数值、布尔和枚举序列化为字符串，向量写为字符串数组，例如 `"layer_height": "0.2"`、`"wipe": ["0"]`；百分比值可写成 `"15%"`。特殊字段应按目标版本支持的格式及同类预设确认。

复数类型一般表示向量，不是多选；索引语义取决于字段：打印机挤出机页面的相关向量按挤出机槽位使用，耗材页面按当前耗材槽使用；带 `flow_support` 的字段还涉及流量级别，不能一概按挤出机解释。`points`、`point`、多行 G-code、特殊枚举和覆盖项应按各自序列化实现处理，不能机械地按类型名称推断 JSON 结构。`nullable` 标记逻辑上的自动或不覆盖。对于支持空值的回抽覆盖项，系统预设可使用字符串 `"nil"`，例如 `"filament_retraction_length": ["nil"]`；它不同于 JSON 的 `null`，其他字段应确认各自的写法。

## 5 参数字典

下表按界面页面和分组顺序列出设置项；预设还可包含隐藏参数、历史字段和扩展字段。表中列出显示名、逻辑类型、默认值、范围、候选值和特殊标记。默认值是逻辑默认值，不代表当前文件中必须出现，也不一定是完整继承后的最终值。缺少边界表示表中未列出边界，不表示实现一定没有其他约束。标有“可编辑候选”的 `values` 是建议选项，允许输入其他值；没有该标记的候选值也应结合对应字段的实现判断。未建键页的键（元数据字段、Developer 键，以及未挂入三个设置 Tab 的键）以纯代码键名标注，其说明以本页为准。

类型名称中，`bool`、`int`、`float`、`string` 和 `enum` 分别表示布尔、整数、浮点数、文本和枚举；复数形式表示向量。`percent` 表示百分数，`float_or_percent` 可表示数值或百分比。`flow_support` 表示字段支持按流量变体（flow variant）取多个值：数组首项为 `standard`，第二项为 `high_flow`；具体顺序由本模块的 `process_flow_support` 声明（见 5.3 流量支持）。`nullable` 表示该值可处于自动或不覆盖状态。

表中 `范围/候选/标记` 的数值约束也以逻辑值表示；部分字段的显示或可用状态取决于其他设置；界面中隐藏或禁用字段不意味着该字段在文件中非法。

### 5.1 质量

#### 层高

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`layer_height`](../settings/process/quality/layer_height.md) | 层高（mm） | `float` | `0.2` | min=0 |
| [`initial_layer_print_height`](../settings/process/quality/initial_layer_print_height.md) | 首层层高（mm） | `float` | `0.2` | min=0 |

#### 线宽

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`line_width`](../settings/process/quality/line_width.md) | 缺省（mm 或 %） | `float_or_percent` | `0` | min=0; max=1000 |
| [`initial_layer_line_width`](../settings/process/quality/initial_layer_line_width.md) | 首层（mm 或 %） | `float_or_percent` | `0` | min=0; max=1000 |
| [`outer_wall_line_width`](../settings/process/quality/outer_wall_line_width.md) | 外墙（mm 或 %） | `float_or_percent` | `0` | min=0; max=1000 |
| [`inner_wall_line_width`](../settings/process/quality/inner_wall_line_width.md) | 内墙（mm 或 %） | `float_or_percent` | `0` | min=0; max=1000 |
| [`top_surface_line_width`](../settings/process/quality/top_surface_line_width.md) | 顶面（mm 或 %） | `float_or_percent` | `0` | min=0; max=1000 |
| [`sparse_infill_line_width`](../settings/process/quality/sparse_infill_line_width.md) | 稀疏填充（mm 或 %） | `float_or_percent` | `0` | min=0; max=1000 |
| [`internal_solid_infill_line_width`](../settings/process/quality/internal_solid_infill_line_width.md) | 内部实心填充（mm 或 %） | `float_or_percent` | `0` | min=0; max=1000 |
| [`support_line_width`](../settings/process/quality/support_line_width.md) | 支撑（mm 或 %） | `float_or_percent` | `0` | min=0; max=1000 |

#### 接缝

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`seam_position`](../settings/process/quality/seam_position.md) | 接缝位置 | `enum` | `"aligned"` | values=["nearest","aligned","aligned_back","back","random"] |
| [`staggered_inner_seams`](../settings/process/quality/staggered_inner_seams.md) | 交错的内墙接缝 | `bool` | `false` | — |
| [`seam_gap`](../settings/process/quality/seam_gap.md) | 接缝间隔（mm 或 %） | `float_or_percent` | `"10%"` | min=0 |
| [`seam_slope_type`](../settings/process/quality/seam_slope_type.md) | 斜拼接缝（试验） | `enum` | `"none"` | values=["none","external","all"] |
| [`seam_slope_conditional`](../settings/process/quality/seam_slope_conditional.md) | 选择性应用斜拼接缝 | `bool` | `false` | — |
| [`scarf_angle_threshold`](../settings/process/quality/scarf_angle_threshold.md) | 角度阈值（°） | `int` | `155` | min=0; max=180 |
| [`scarf_overhang_threshold`](../settings/process/quality/scarf_overhang_threshold.md) | 悬垂阈值（%） | `percent` | `40` | min=0 |
| [`scarf_joint_speed`](../settings/process/quality/scarf_joint_speed.md) | 斜拼接缝速度（mm/s 或 %） | `float_or_percent` | `"100%"` | min=1 |
| [`seam_slope_start_height`](../settings/process/quality/seam_slope_start_height.md) | 斜拼接缝起始高度（mm 或 %） | `float_or_percent` | `0` | min=0 |
| [`seam_slope_entire_loop`](../settings/process/quality/seam_slope_entire_loop.md) | 围绕整个围墙 | `bool` | `false` | — |
| [`seam_slope_min_length`](../settings/process/quality/seam_slope_min_length.md) | 斜拼接缝长度（mm） | `float` | `20` | min=0 |
| [`seam_slope_steps`](../settings/process/quality/seam_slope_steps.md) | 斜拼段数 | `int` | `10` | min=1 |
| [`scarf_joint_flow_ratio`](../settings/process/quality/scarf_joint_flow_ratio.md) | 斜拼接缝流量 | `float` | `1` | max=2 |
| [`seam_slope_inner_walls`](../settings/process/quality/seam_slope_inner_walls.md) | 应用斜拼于内墙 | `bool` | `false` | — |
| [`role_based_wipe_speed`](../settings/process/quality/role_based_wipe_speed.md) | 自动擦拭速度 | `bool` | `true` | — |
| [`wipe_speed`](../settings/process/quality/wipe_speed.md) | 擦拭速度（mm/s 或 %） | `float_or_percent` | `"80%"` | min=0 |
| [`wipe_on_loops`](../settings/process/quality/wipe_on_loops.md) | 闭环擦拭 | `bool` | `false` | — |
| [`wipe_before_external_loop`](../settings/process/quality/wipe_before_external_loop.md) | 额外的外墙打印前擦拭 | `bool` | `false` | — |

#### 精度

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`slice_closing_radius`](../settings/process/quality/slice_closing_radius.md) | 切片间隙闭合半径（mm） | `float` | `0.049` | min=0 |
| [`resolution`](../settings/process/quality/resolution.md) | 分辨率（mm） | `float` | `0.01` | min=0 |
| [`enable_arc_fitting`](../settings/process/quality/enable_arc_fitting.md) | 圆弧拟合 | `bool` | `false` | — |
| [`xy_hole_compensation`](../settings/process/quality/xy_hole_compensation.md) | X-Y 孔洞尺寸补偿（mm） | `float` | `0` | — |
| [`xy_contour_compensation`](../settings/process/quality/xy_contour_compensation.md) | X-Y 外轮廓尺寸补偿（mm） | `float` | `0` | — |
| [`elefant_foot_compensation`](../settings/process/quality/elefant_foot_compensation.md) | 象脚补偿（mm） | `float` | `0` | min=0 |
| [`elefant_foot_compensation_layers`](../settings/process/quality/elefant_foot_compensation_layers.md) | 象脚补偿层数（层） | `int` | `1` | min=1 |
| [`precise_outer_wall`](../settings/process/quality/precise_outer_wall.md) | 精准外墙尺寸 | `bool` | `true` | — |
| [`precise_z_height`](../settings/process/quality/precise_z_height.md) | 精准Z高度 | `bool` | `false` | — |
| [`hole_to_polyhole`](../settings/process/quality/hole_to_polyhole.md) | 将圆孔转换为多边型孔 | `bool` | `false` | — |
| [`hole_to_polyhole_threshold`](../settings/process/quality/hole_to_polyhole_threshold.md) | 多边型孔检测边缘（mm 或 %） | `float_or_percent` | `0.01` | — |
| [`hole_to_polyhole_twisted`](../settings/process/quality/hole_to_polyhole_twisted.md) | 扭曲多边型孔 | `bool` | `true` | — |

#### 熨烫

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`ironing_type`](../settings/process/quality/ironing_type.md) | 熨烫类型 | `enum` | `"no ironing"` | values=["no ironing","top","topmost","solid"] |
| [`ironing_pattern`](../settings/process/quality/ironing_pattern.md) | 熨烫模式 | `enum` | `"rectilinear"` | values=["rectilinear","concentric"] |
| [`ironing_flow`](../settings/process/quality/ironing_flow.md) | 熨烫流量（%） | `percent` | `10` | min=0; max=100 |
| [`ironing_spacing`](../settings/process/quality/ironing_spacing.md) | 熨烫间距（mm） | `float` | `0.1` | min=0; max=1 |
| [`ironing_inset`](../settings/process/quality/ironing_inset.md) | 熨烫内缩（mm） | `float` | `0` | min=0; max=100 |
| [`ironing_angle`](../settings/process/quality/ironing_angle.md) | 熨烫角度（°） | `float` | `-1` | min=-1; max=359 |

#### 墙生成器

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`wall_generator`](../settings/process/quality/wall_generator.md) | 墙生成器 | `enum` | `"arachne"` | values=["classic","arachne"] |
| [`wall_transition_angle`](../settings/process/quality/wall_transition_angle.md) | 墙过渡阈值角度（°） | `float` | `10` | min=1; max=59 |
| [`wall_transition_filter_deviation`](../settings/process/quality/wall_transition_filter_deviation.md) | 墙过渡过滤间距（%） | `percent` | `25` | min=0 |
| [`wall_transition_length`](../settings/process/quality/wall_transition_length.md) | 墙过渡长度（%） | `percent` | `100` | min=0 |
| [`wall_distribution_count`](../settings/process/quality/wall_distribution_count.md) | 墙分布计数 | `int` | `1` | min=1 |
| [`initial_layer_min_bead_width`](../settings/process/quality/initial_layer_min_bead_width.md) | 首层墙最小线宽（%） | `percent` | `85` | min=0 |
| [`min_bead_width`](../settings/process/quality/min_bead_width.md) | 墙最小线宽（%） | `percent` | `85` | min=0 |
| [`min_feature_size`](../settings/process/quality/min_feature_size.md) | 最小特征尺寸（%） | `percent` | `25` | min=0 |
| [`min_length_factor`](../settings/process/quality/min_length_factor.md) | 最小允许的墙长度（mm） | `float` | `0.5` | min=0; max=25 |

#### 墙壁和表面

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`wall_sequence`](../settings/process/quality/wall_sequence.md) | 墙顺序 | `enum` | `"inner wall/outer wall"` | values=["inner wall/outer wall","outer wall/inner wall","inner-outer-inner wall"] |
| [`is_infill_first`](../settings/process/quality/is_infill_first.md) | 首先打印填充 | `bool` | `false` | — |
| [`wall_direction`](../settings/process/quality/wall_direction.md) | 围墙打印方向 | `enum` | `"auto"` | values=["auto","ccw","cw"] |
| [`print_flow_ratio`](../settings/process/quality/print_flow_ratio.md) | 流量比例 | `float` | `1` | min=0.01; max=2 |
| [`top_solid_infill_flow_ratio`](../settings/process/quality/top_solid_infill_flow_ratio.md) | 顶部表面流量比例 | `float` | `1` | min=0; max=2 |
| [`bottom_solid_infill_flow_ratio`](../settings/process/quality/bottom_solid_infill_flow_ratio.md) | 底部表面流量比例 | `float` | `1` | min=0; max=2 |
| [`only_one_wall_top`](../settings/process/quality/only_one_wall_top.md) | 顶面单层墙 | `bool` | `false` | — |
| [`min_width_top_surface`](../settings/process/quality/min_width_top_surface.md) | 单层墙阈值（mm 或 %） | `float_or_percent` | `"300%"` | min=0 |
| [`only_one_wall_first_layer`](../settings/process/quality/only_one_wall_first_layer.md) | 首层仅单层墙 | `bool` | `false` | — |
| [`reduce_crossing_wall`](../settings/process/quality/reduce_crossing_wall.md) | 避免跨越外墙 | `bool` | `false` | — |
| [`max_travel_detour_distance`](../settings/process/quality/max_travel_detour_distance.md) | 避免跨越外墙-最大绕行长度（mm 或 %） | `float_or_percent` | `0` | min=0 |
| [`small_area_infill_flow_compensation`](../settings/process/quality/small_area_infill_flow_compensation.md) | 小区域填充流量补偿（试验） | `bool` | `false` | — |
| [`small_area_infill_flow_compensation_model`](../settings/process/quality/small_area_infill_flow_compensation_model.md) | 流量补偿模型 | `strings` | `["0,0","\n0.2,0.4444","\n0.4,0.6145","\n0.6,0.7059","\n0.8,0.7619","\n1.5,0.8571","\n2,0.8889","\n3,0.9231","\n5,0.9520","\n10,1"]` | — |

#### 搭桥

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`bridge_flow`](../settings/process/quality/bridge_flow.md) | 桥接流量 | `float` | `1` | min=0; max=2 |
| [`internal_bridge_flow`](../settings/process/quality/internal_bridge_flow.md) | 内部搭桥流量比例 | `float` | `1` | min=0; max=2 |
| [`bridge_density`](../settings/process/quality/bridge_density.md) | 外部桥接密度（%） | `percent` | `100` | min=10; max=120 |
| [`internal_bridge_density`](../settings/process/quality/internal_bridge_density.md) | 内部桥接密度（%） | `percent` | `100` | min=10; max=100 |
| [`thick_bridges`](../settings/process/quality/thick_bridges.md) | 外部搭桥用厚桥 | `bool` | `false` | — |
| [`thick_internal_bridges`](../settings/process/quality/thick_internal_bridges.md) | 内部搭桥用厚桥 | `bool` | `true` | — |
| [`enable_extra_bridge_layer`](../settings/process/quality/enable_extra_bridge_layer.md) | 额外桥层（测试版） | `enum` | `"disabled"` | values=["disabled","external_bridge_only","internal_bridge_only","apply_to_all"] |
| [`dont_filter_internal_bridges`](../settings/process/quality/dont_filter_internal_bridges.md) | 过滤掉小的内部桥接 | `enum` | `"disabled"` | values=["disabled","limited","nofilter"] |
| [`counterbore_hole_bridging`](../settings/process/quality/counterbore_hole_bridging.md) | 沉孔搭桥 | `enum` | `"none"` | values=["none","partiallybridge","sacrificiallayer"] |

#### 悬垂

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`detect_overhang_wall`](../settings/process/quality/detect_overhang_wall.md) | 识别悬空外墙 | `bool` | `true` | — |
| [`make_overhang_printable`](../settings/process/quality/make_overhang_printable.md) | 悬垂可打印化 | `bool` | `false` | — |
| [`make_overhang_printable_angle`](../settings/process/quality/make_overhang_printable_angle.md) | 悬垂可打印化的最大角度（°） | `float` | `55` | min=0; max=90 |
| [`make_overhang_printable_hole_size`](../settings/process/quality/make_overhang_printable_hole_size.md) | 最大孔洞面积（mm²） | `float` | `0` | min=0 |
| [`extra_perimeters_on_overhangs`](../settings/process/quality/extra_perimeters_on_overhangs.md) | 悬垂上的额外周长 | `bool` | `false` | — |
| [`overhang_reverse`](../settings/process/quality/overhang_reverse.md) | 反转偶数层悬垂方向 | `bool` | `false` | — |
| [`overhang_reverse_internal_only`](../settings/process/quality/overhang_reverse_internal_only.md) | 仅反转内部墙壁 | `bool` | `false` | — |
| [`overhang_reverse_threshold`](../settings/process/quality/overhang_reverse_threshold.md) | 反转阈值（mm 或 %） | `float_or_percent` | `"50%"` | min=0 |

### 5.2 强度

#### 墙

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`wall_loops`](../settings/process/strength/wall_loops.md) | 墙层数 | `int` | `2` | min=0; max=1000 |
| [`alternate_extra_wall`](../settings/process/strength/alternate_extra_wall.md) | 交替添加额外内墙 | `bool` | `false` | — |
| [`detect_thin_wall`](../settings/process/strength/detect_thin_wall.md) | 检查薄壁 | `bool` | `false` | — |

#### 顶部/底部外壳

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`top_surface_pattern`](../settings/process/strength/top_surface_pattern.md) | 顶面图案 | `enum` | `"monotonicline"` | values=["monotonic","monotonicline","rectilinear","alignedrectilinear","concentric","hilbertcurve","archimedeanchords","octagramspiral"] |
| [`top_shell_layers`](../settings/process/strength/top_shell_layers.md) | 顶部壳体层数（层） | `int` | `4` | min=0 |
| [`top_shell_thickness`](../settings/process/strength/top_shell_thickness.md) | 顶部壳体厚度（mm） | `float` | `0.6` | min=0 |
| [`top_color_penetration_layers`](../settings/process/strength/top_color_penetration_layers.md) | 顶部涂色渗透层数（层） | `int` | `4` | min=0 |
| [`bottom_surface_pattern`](../settings/process/strength/bottom_surface_pattern.md) | 底面图案 | `enum` | `"monotonic"` | values=["monotonic","monotonicline","rectilinear","alignedrectilinear","concentric","hilbertcurve","archimedeanchords","octagramspiral"] |
| [`bottom_shell_layers`](../settings/process/strength/bottom_shell_layers.md) | 底部壳体层数（层） | `int` | `3` | min=0 |
| [`bottom_shell_thickness`](../settings/process/strength/bottom_shell_thickness.md) | 底部壳体厚度（mm） | `float` | `0` | min=0 |
| [`bottom_color_penetration_layers`](../settings/process/strength/bottom_color_penetration_layers.md) | 底部涂色渗透层数（层） | `int` | `3` | min=0 |
| [`top_bottom_infill_wall_overlap`](../settings/process/strength/top_bottom_infill_wall_overlap.md) | 顶/底部实心填充/墙重叠率（%） | `percent` | `25` | — |

#### 填充

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`sparse_infill_density`](../settings/process/strength/sparse_infill_density.md) | 稀疏填充密度（%） | `percent` | `20` | min=0; max=100 |
| [`fill_multiline`](../settings/process/strength/fill_multiline.md) | 填充多线 | `int` | `1` | min=1; max=5 |
| [`sparse_infill_pattern`](../settings/process/strength/sparse_infill_pattern.md) | 稀疏填充图案 | `enum` | `"crosshatch"` | values=["rectilinear","alignedrectilinear","zigzag","crosszag","lockedzag","line","grid","triangles","tri-hexagon","cubic","adaptivecubic","quartercubic","supportcubic","lightning","honeycomb","3dhoneycomb","lateral-honeycomb","lateral-lattice","crosshatch","tpmsd","tpmsfk","gyroid","concentric","hilbertcurve","archimedeanchords","octagramspiral"] |
| [`infill_direction`](../settings/process/strength/infill_direction.md) | 稀疏填充方向（°） | `float` | `45` | min=0; max=360 |
| [`sparse_infill_rotate_template`](../settings/process/strength/sparse_infill_rotate_template.md) | 稀疏填充旋转模板（°） | `string` | `""` | — |
| [`skin_infill_density`](../settings/process/strength/skin_infill_density.md) | 外壳填充密度（%） | `percent` | `25` | min=0; max=100 |
| [`skeleton_infill_density`](../settings/process/strength/skeleton_infill_density.md) | 骨架填充密度（%） | `percent` | `25` | min=0; max=100 |
| [`infill_lock_depth`](../settings/process/strength/infill_lock_depth.md) | 填充锁定深度（mm） | `float` | `1` | min=0; max=100 |
| [`skin_infill_depth`](../settings/process/strength/skin_infill_depth.md) | 外壳填充深度（mm） | `float` | `2` | min=0; max=100 |
| [`skin_infill_line_width`](../settings/process/strength/skin_infill_line_width.md) | 外壳线宽（mm） | `float_or_percent` | `"100%"` | min=0 |
| [`skeleton_infill_line_width`](../settings/process/strength/skeleton_infill_line_width.md) | 骨架线宽（mm） | `float_or_percent` | `"100%"` | min=0 |
| [`symmetric_infill_y_axis`](../settings/process/strength/symmetric_infill_y_axis.md) | 对称填充Y轴 | `bool` | `false` | — |
| [`infill_shift_step`](../settings/process/strength/infill_shift_step.md) | 填充偏移步长（mm） | `float` | `0.4` | min=0; max=10 |
| [`lateral_lattice_angle_1`](../settings/process/strength/lateral_lattice_angle_1.md) | 侧向晶格角度1（°） | `float` | `-45` | min=-75; max=75 |
| [`lateral_lattice_angle_2`](../settings/process/strength/lateral_lattice_angle_2.md) | 侧向晶格角度2（°） | `float` | `45` | min=-75; max=75 |
| [`infill_overhang_angle`](../settings/process/strength/infill_overhang_angle.md) | 填充悬空角度（°） | `float` | `60` | min=15; max=75 |
| [`infill_anchor_max`](../settings/process/strength/infill_anchor_max.md) | 填充锚线的最大长度 | `float_or_percent` | `20` | values=["0","1","2","5","10","1000"]; 可编辑候选 |
| [`infill_anchor`](../settings/process/strength/infill_anchor.md) | 稀疏填充锚线长度（mm 或 %） | `float_or_percent` | `"400%"` | values=["0","1","2","5","10","1000"]; 可编辑候选 |
| [`internal_solid_infill_pattern`](../settings/process/strength/internal_solid_infill_pattern.md) | 内部实心填充图案 | `enum` | `"monotonicline"` | values=["monotonic","monotonicline","rectilinear","alignedrectilinear","concentric","hilbertcurve","archimedeanchords","octagramspiral"] |
| [`solid_infill_direction`](../settings/process/strength/solid_infill_direction.md) | 实心填充方向（°） | `float` | `45` | min=0; max=360 |
| [`solid_infill_rotate_template`](../settings/process/strength/solid_infill_rotate_template.md) | 实心填充旋转模板（°） | `string` | `""` | — |
| [`gap_fill_target`](../settings/process/strength/gap_fill_target.md) | 启用间隙填充 | `enum` | `"nowhere"` | values=["everywhere","topbottom","nowhere"] |
| [`filter_out_gap_fill`](../settings/process/strength/filter_out_gap_fill.md) | 忽略微小间隙（mm） | `float` | `0` | — |
| [`infill_wall_overlap`](../settings/process/strength/infill_wall_overlap.md) | 填充/墙 重叠（%） | `percent` | `15` | — |

#### 高级

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`align_infill_direction_to_model`](../settings/process/strength/align_infill_direction_to_model.md) | 对齐填充方向到模型 | `bool` | `false` | — |
| [`extra_solid_infills`](../settings/process/strength/extra_solid_infills.md) | 插入实心层 | `string` | `""` | — |
| [`bridge_angle`](../settings/process/strength/bridge_angle.md) | 外部桥接填充方向（°） | `float` | `0` | min=0 |
| [`internal_bridge_angle`](../settings/process/strength/internal_bridge_angle.md) | 内部桥接填充方向（°） | `float` | `0` | min=0 |
| [`minimum_sparse_infill_area`](../settings/process/strength/minimum_sparse_infill_area.md) | 稀疏填充最小阈值（mm²） | `float` | `15` | min=0 |
| [`infill_combination`](../settings/process/strength/infill_combination.md) | 合并填充 | `bool` | `false` | — |
| [`infill_combination_max_layer_height`](../settings/process/strength/infill_combination_max_layer_height.md) | 填充组合 - 最大层高（mm 或 %） | `float_or_percent` | `"100%"` | min=0 |
| [`detect_narrow_internal_solid_infill`](../settings/process/strength/detect_narrow_internal_solid_infill.md) | 识别狭窄内部实心填充 | `bool` | `true` | — |
| [`ensure_vertical_shell_thickness`](../settings/process/strength/ensure_vertical_shell_thickness.md) | 确保垂直外壳厚度 | `enum` | `"ensure_all"` | values=["none","ensure_critical_only","ensure_moderate","ensure_all"] |

### 5.3 速度

#### 首层速度

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`initial_layer_speed`](../settings/process/speed/initial_layer_speed.md) | 首层（mm/s） | `floats` | `[30]` | min=1; flow_support |
| [`initial_layer_infill_speed`](../settings/process/speed/initial_layer_infill_speed.md) | 首层填充（mm/s） | `floats` | `[60]` | min=1; flow_support |
| [`initial_layer_travel_speed`](../settings/process/speed/initial_layer_travel_speed.md) | 首层空驶速度（mm/s 或 %） | `floats_or_percents` | `["100%"]` | min=1; flow_support |
| [`slow_down_layers`](../settings/process/speed/slow_down_layers.md) | 慢速打印层数（层） | `ints` | `[0]` | min=0; flow_support |

#### 其他层速度

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`outer_wall_speed`](../settings/process/speed/outer_wall_speed.md) | 外墙（mm/s） | `floats` | `[60]` | min=1; flow_support |
| [`inner_wall_speed`](../settings/process/speed/inner_wall_speed.md) | 内墙（mm/s） | `floats` | `[60]` | min=1; flow_support |
| [`small_perimeter_speed`](../settings/process/speed/small_perimeter_speed.md) | 微小部位（mm/s 或 %） | `floats_or_percents` | `["50%"]` | min=1; flow_support |
| [`small_perimeter_threshold`](../settings/process/speed/small_perimeter_threshold.md) | 微小部位周长阈值（mm） | `floats` | `[0]` | min=0; flow_support |
| [`sparse_infill_speed`](../settings/process/speed/sparse_infill_speed.md) | 稀疏填充（mm/s） | `floats` | `[100]` | min=1; flow_support |
| [`internal_solid_infill_speed`](../settings/process/speed/internal_solid_infill_speed.md) | 内部实心填充（mm/s） | `floats` | `[100]` | min=1; flow_support |
| [`top_surface_speed`](../settings/process/speed/top_surface_speed.md) | 顶面（mm/s） | `floats` | `[100]` | min=1; flow_support |
| [`gap_infill_speed`](../settings/process/speed/gap_infill_speed.md) | 填缝（mm/s） | `floats` | `[30]` | min=1; flow_support |
| [`ironing_speed`](../settings/process/speed/ironing_speed.md) | 熨烫速度（mm/s） | `floats` | `[20]` | min=1; flow_support |
| [`support_speed`](../settings/process/speed/support_speed.md) | 支撑（mm/s） | `floats` | `[80]` | min=1; flow_support |
| [`support_interface_speed`](../settings/process/speed/support_interface_speed.md) | 支撑面（mm/s） | `floats` | `[80]` | min=1; flow_support |

#### 悬垂速度

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`enable_overhang_speed`](../settings/process/speed/enable_overhang_speed.md) | 悬垂降速 | `bools` | `[true]` | flow_support |
| [`slowdown_for_curled_perimeters`](../settings/process/speed/slowdown_for_curled_perimeters.md) | 翘边降速 | `bools` | `[true]` | flow_support |
| [`overhang_1_4_speed`](../settings/process/speed/overhang_1_4_speed.md) | [10%, 25%)（mm/s 或 %） | `floats_or_percents` | `[0]` | min=0; flow_support |
| [`overhang_2_4_speed`](../settings/process/speed/overhang_2_4_speed.md) | [25%, 50%)（mm/s 或 %） | `floats_or_percents` | `[0]` | min=0; flow_support |
| [`overhang_3_4_speed`](../settings/process/speed/overhang_3_4_speed.md) | [50%, 75%)（mm/s 或 %） | `floats_or_percents` | `[0]` | min=0; flow_support |
| [`overhang_4_4_speed`](../settings/process/speed/overhang_4_4_speed.md) | [75%, 100%)（mm/s 或 %） | `floats_or_percents` | `[0]` | min=0; flow_support |
| [`overhang_totally_speed`](../settings/process/speed/overhang_totally_speed.md) | 100%（mm/s 或 %） | `floats_or_percents` | `[10]` | min=0; flow_support |
| [`bridge_speed`](../settings/process/speed/bridge_speed.md) | 外部（mm/s） | `floats` | `[25]` | min=1; flow_support |
| [`internal_bridge_speed`](../settings/process/speed/internal_bridge_speed.md) | 内部（mm/s 或 %） | `floats_or_percents` | `["150%"]` | min=1; flow_support |

#### 空驶速度

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`travel_speed`](../settings/process/speed/travel_speed.md) | 空驶（mm/s） | `floats` | `[120]` | min=1; flow_support |

#### 加速度

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`default_acceleration`](../settings/process/speed/default_acceleration.md) | 普通打印（mm/s²） | `floats` | `[500]` | min=0; flow_support |
| [`outer_wall_acceleration`](../settings/process/speed/outer_wall_acceleration.md) | 外墙（mm/s²） | `floats` | `[500]` | min=0; flow_support |
| [`inner_wall_acceleration`](../settings/process/speed/inner_wall_acceleration.md) | 内墙（mm/s²） | `floats` | `[10000]` | min=0; flow_support |
| [`bridge_acceleration`](../settings/process/speed/bridge_acceleration.md) | 桥接（mm/s² 或 %） | `floats_or_percents` | `["50%"]` | min=0; flow_support |
| [`sparse_infill_acceleration`](../settings/process/speed/sparse_infill_acceleration.md) | 稀疏填充（mm/s² 或 %） | `floats_or_percents` | `["100%"]` | min=0; flow_support |
| [`internal_solid_infill_acceleration`](../settings/process/speed/internal_solid_infill_acceleration.md) | 内部实心填充（mm/s² 或 %） | `floats_or_percents` | `["100%"]` | min=0; flow_support |
| [`initial_layer_acceleration`](../settings/process/speed/initial_layer_acceleration.md) | 首层（mm/s²） | `floats` | `[300]` | min=0; flow_support |
| [`first_layer_travel_acceleration`](../settings/process/speed/first_layer_travel_acceleration.md) | 首层空驶（mm/s² 或 %） | `float_or_percent` | `"100%"` | min=0 |
| [`top_surface_acceleration`](../settings/process/speed/top_surface_acceleration.md) | 顶面（mm/s²） | `floats` | `[500]` | min=0; flow_support |
| [`travel_acceleration`](../settings/process/speed/travel_acceleration.md) | 空驶（mm/s²） | `floats` | `[10000]` | min=0; flow_support |
| [`accel_to_decel_enable`](../settings/process/speed/accel_to_decel_enable.md) | 启用制动速度 | `bools` | `[true]` | flow_support |
| [`accel_to_decel_factor`](../settings/process/speed/accel_to_decel_factor.md) | 制动速度（%） | `percents` | `[50]` | min=1; max=100; flow_support |

#### 抖动（XY轴）

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`default_jerk`](../settings/process/speed/default_jerk.md) | 缺省（mm/s） | `floats` | `[0]` | min=0; flow_support |
| [`outer_wall_jerk`](../settings/process/speed/outer_wall_jerk.md) | 外墙（mm/s） | `floats` | `[9]` | min=0; flow_support |
| [`inner_wall_jerk`](../settings/process/speed/inner_wall_jerk.md) | 内墙（mm/s） | `floats` | `[9]` | min=0; flow_support |
| [`infill_jerk`](../settings/process/speed/infill_jerk.md) | 填充（mm/s） | `floats` | `[9]` | min=0; flow_support |
| [`top_surface_jerk`](../settings/process/speed/top_surface_jerk.md) | 顶面（mm/s） | `floats` | `[9]` | min=0; flow_support |
| [`initial_layer_jerk`](../settings/process/speed/initial_layer_jerk.md) | 首层（mm/s） | `floats` | `[9]` | min=0; flow_support |
| [`first_layer_travel_jerk`](../settings/process/speed/first_layer_travel_jerk.md) | 首层空驶（mm/s 或 %） | `float_or_percent` | `"100%"` | min=0 |
| [`travel_jerk`](../settings/process/speed/travel_jerk.md) | 空驶（mm/s） | `floats` | `[12]` | min=0; flow_support |
| [`default_junction_deviation`](../settings/process/speed/default_junction_deviation.md) | 结点偏差（mm） | `floats` | `[0]` | min=0; flow_support |

#### 高级

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`max_volumetric_extrusion_rate_slope`](../settings/process/speed/max_volumetric_extrusion_rate_slope.md) | 平滑挤出率（mm³/s²） | `floats` | `[0]` | min=0; flow_support |
| [`max_volumetric_extrusion_rate_slope_segment_length`](../settings/process/speed/max_volumetric_extrusion_rate_slope_segment_length.md) | 平滑段长度（mm） | `floats` | `[3]` | min=0.5; max=5; flow_support |
| [`extrusion_rate_smoothing_external_perimeter_only`](../settings/process/speed/extrusion_rate_smoothing_external_perimeter_only.md) | 仅应用于外部特征 | `bools` | `[false]` | flow_support |

#### 流量支持（非界面键）

该字段声明本预设支持的流量变体及其顺序：数组首项为 `standard`，其后为 `high_flow` 等变体。带 `flow_support` 标记的多值参数按同一顺序排列，首值属于 `standard`；未提供的变体在参数中可写作字符串 `nil`，与数字 `0` 不同。字段取值为字符串数组，与 [gcode.3mf 交互字段](../specification/gcode.3mf/gcode_3mf_interaction_fields.md#31-流量类型族) 的 `process_flow_support` 描述一致。

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| `process_flow_support` | 工艺流量支持 | `strings` | `["standard"]` | values=["standard","high_flow"]; 非界面键（Developer 级） |

### 5.4 支撑

#### 支撑

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`enable_support`](../settings/process/support/enable_support.md) | 开启支撑 | `bool` | `false` | — |
| [`support_type`](../settings/process/support/support_type.md) | 类型 | `enum` | `"normal(auto)"` | values=["normal(auto)","tree(auto)","normal(manual)","tree(manual)"] |
| [`support_style`](../settings/process/support/support_style.md) | 样式 | `enum` | `"default"` | values=["default","grid","snug","organic","tree_slim","tree_strong","tree_hybrid"] |
| [`support_threshold_angle`](../settings/process/support/support_threshold_angle.md) | 阈值角度（°） | `int` | `30` | min=1; max=90 |
| [`support_threshold_overlap`](../settings/process/support/support_threshold_overlap.md) | 阈值支撑比例（mm 或 %） | `float_or_percent` | `"50%"` | min=0; max=100 |
| [`raft_first_layer_density`](../settings/process/support/raft_first_layer_density.md) | 首层密度（%） | `percent` | `90` | min=10; max=100 |
| [`raft_first_layer_expansion`](../settings/process/support/raft_first_layer_expansion.md) | 首层扩展（mm） | `float` | `-1` | min=-1 |
| [`support_on_build_plate_only`](../settings/process/support/support_on_build_plate_only.md) | 仅在构建板生成 | `bool` | `false` | — |
| [`support_critical_regions_only`](../settings/process/support/support_critical_regions_only.md) | 仅支撑关键区域 | `bool` | `false` | — |
| [`support_remove_small_overhang`](../settings/process/support/support_remove_small_overhang.md) | 移除小悬空 | `bool` | `true` | — |

#### 筏层

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`raft_layers`](../settings/process/support/raft_layers.md) | 筏层（层） | `int` | `0` | min=0; max=100 |
| [`raft_contact_distance`](../settings/process/support/raft_contact_distance.md) | 筏层Z间距（mm） | `float` | `0.1` | min=0 |
| `raft_expansion` | 筏层扩展（mm） | `float` | `1.5` | min=0 |

#### 支撑耗材

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`support_filament`](../settings/process/support/support_filament.md) | 支撑/筏层主体 | `int` | `0` | min=0 |
| [`support_interface_filament`](../settings/process/support/support_interface_filament.md) | 支撑/筏层界面 | `int` | `0` | min=0 |
| [`support_interface_not_for_body`](../settings/process/support/support_interface_not_for_body.md) | 界面材料不用于主体 | `bool` | `true` | — |

#### 支撑熨烫

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`support_ironing`](../settings/process/support/support_ironing.md) | 支撑界面熨烫 | `bool` | `false` | — |
| [`support_ironing_pattern`](../settings/process/support/support_ironing_pattern.md) | 支撑熨烫图案 | `enum` | `"rectilinear"` | values=["rectilinear","concentric"] |
| [`support_ironing_flow`](../settings/process/support/support_ironing_flow.md) | 支撑熨烫流量（%） | `percent` | `10` | min=0; max=100 |
| [`support_ironing_spacing`](../settings/process/support/support_ironing_spacing.md) | 支撑熨烫线间距（mm） | `float` | `0.1` | min=0; max=1 |

#### 高级

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`support_top_z_distance`](../settings/process/support/support_top_z_distance.md) | 顶部Z距离（mm） | `float` | `0.2` | min=0 |
| [`support_bottom_z_distance`](../settings/process/support/support_bottom_z_distance.md) | 底部Z距离（mm） | `float` | `0.2` | min=0 |
| [`tree_support_wall_count`](../settings/process/support/tree_support_wall_count.md) | 支撑外墙层数 | `int` | `0` | min=0; max=2 |
| [`support_base_pattern`](../settings/process/support/support_base_pattern.md) | 支撑主体图案 | `enum` | `"default"` | values=["default","rectilinear","rectilinear-grid","honeycomb","lightning","hollow"] |
| [`support_base_pattern_spacing`](../settings/process/support/support_base_pattern_spacing.md) | 主体图案线距（mm） | `float` | `2.5` | min=0 |
| [`support_angle`](../settings/process/support/support_angle.md) | 模式角度（°） | `float` | `0` | min=0; max=359 |
| [`support_interface_top_layers`](../settings/process/support/support_interface_top_layers.md) | 顶部接触面层数（层） | `int` | `3` | min=0; values=["0","1","2","3"]; 可编辑候选 |
| [`support_interface_bottom_layers`](../settings/process/support/support_interface_bottom_layers.md) | 底部接触面层数（层） | `int` | `0` | min=-1; values=["-1","0","1","2","3"]; 可编辑候选 |
| [`support_interface_pattern`](../settings/process/support/support_interface_pattern.md) | 支撑面图案 | `enum` | `"auto"` | values=["auto","rectilinear","concentric","rectilinear_interlaced","grid"] |
| `support_interface_loop_pattern` | 接触面使用闭环图案 | `bool` | `false` | — |
| [`support_interface_spacing`](../settings/process/support/support_interface_spacing.md) | 顶部接触面线距（mm） | `float` | `0.5` | min=0 |
| [`support_interface_min_area`](../settings/process/support/support_interface_min_area.md) | 最小支撑接触面面积（mm²） | `float` | `0.25` | min=0; values=["0","0.25","0.64","1"]; 可编辑候选 |
| [`support_bottom_interface_spacing`](../settings/process/support/support_bottom_interface_spacing.md) | 底部接触面线距（mm） | `float` | `0.5` | min=0 |
| [`support_expansion`](../settings/process/support/support_expansion.md) | 普通支撑拓展（mm） | `float` | `0` | — |
| [`support_object_xy_distance`](../settings/process/support/support_object_xy_distance.md) | 支撑/模型xy间距（mm） | `float` | `0.35` | min=0; max=10 |
| [`support_object_first_layer_gap`](../settings/process/support/support_object_first_layer_gap.md) | 支撑/对象首层间距（mm） | `float` | `0.2` | min=0; max=10 |
| [`bridge_no_support`](../settings/process/support/bridge_no_support.md) | 不支撑桥接 | `bool` | `false` | — |
| [`max_bridge_length`](../settings/process/support/max_bridge_length.md) | 最大桥接长度（mm） | `float` | `0` | min=0 |
| [`independent_support_layer_height`](../settings/process/support/independent_support_layer_height.md) | 支撑独立层高 | `bool` | `false` | — |

#### 树状支撑

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`tree_support_tip_diameter`](../settings/process/support/tree_support_tip_diameter.md) | 尖端直径（mm） | `float` | `0.8` | min=0.1; max=100 |
| [`tree_support_branch_distance`](../settings/process/support/tree_support_branch_distance.md) | 树状支撑分支距离（mm） | `float` | `5` | min=1; max=10 |
| [`tree_support_branch_distance_organic`](../settings/process/support/tree_support_branch_distance_organic.md) | 树状支撑分支距离（mm） | `float` | `1` | min=1; max=10 |
| [`tree_support_top_rate`](../settings/process/support/tree_support_top_rate.md) | 分支密度（%） | `percent` | `30` | min=5 |
| [`tree_support_branch_diameter`](../settings/process/support/tree_support_branch_diameter.md) | 树状支撑分支直径（mm） | `float` | `5` | min=1; max=10 |
| [`tree_support_branch_diameter_organic`](../settings/process/support/tree_support_branch_diameter_organic.md) | 树状支撑分支直径（mm） | `float` | `2` | min=1; max=10 |
| [`tree_support_branch_diameter_angle`](../settings/process/support/tree_support_branch_diameter_angle.md) | 分支直径的角度（°） | `float` | `5` | min=0; max=15 |
| [`tree_support_branch_angle`](../settings/process/support/tree_support_branch_angle.md) | 树状支撑分支角度（°） | `float` | `40` | min=0; max=60 |
| [`tree_support_branch_angle_organic`](../settings/process/support/tree_support_branch_angle_organic.md) | 树状支撑分支角度（°） | `float` | `40` | min=0; max=60 |
| [`tree_support_angle_slow`](../settings/process/support/tree_support_angle_slow.md) | 首选分支角度（°） | `float` | `25` | min=10; max=85 |
| [`tree_support_adaptive_layer_height`](../settings/process/support/tree_support_adaptive_layer_height.md) | 自适应层高 | `bool` | `true` | — |
| [`tree_support_auto_brim`](../settings/process/support/tree_support_auto_brim.md) | 自动裙边宽度 | `bool` | `true` | — |
| [`tree_support_brim_width`](../settings/process/support/tree_support_brim_width.md) | 树状支撑裙边宽度 | `float` | `3` | min=0 |
| `tree_support_with_infill` | 树状支撑填充 | `bool` | `false` | — |

### 5.5 材料

#### 擦拭塔

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`enable_prime_tower`](../settings/process/multimaterial/enable_prime_tower.md) | 开启 | `bool` | `false` | — |
| [`prime_tower_width`](../settings/process/multimaterial/prime_tower_width.md) | 宽度（mm） | `float` | `60` | min=2 |
| [`prime_volume`](../settings/process/multimaterial/prime_volume.md) | 清理量（mm³） | `float` | `45` | min=1 |
| [`prime_tower_brim_width`](../settings/process/multimaterial/prime_tower_brim_width.md) | Brim宽度（mm） | `float` | `3` | min=0 |
| [`wipe_tower_bridging`](../settings/process/multimaterial/wipe_tower_bridging.md) | 最大桥接距离（mm） | `float` | `10` | — |
| [`wipe_tower_extra_spacing`](../settings/process/multimaterial/wipe_tower_extra_spacing.md) | 擦拭塔冲刷线间距（%） | `percent` | `100` | min=100; max=300 |
| [`wipe_tower_extra_flow`](../settings/process/multimaterial/wipe_tower_extra_flow.md) | 额外冲刷量（%） | `percent` | `100` | min=100; max=300 |
| [`wipe_tower_max_purge_speed`](../settings/process/multimaterial/wipe_tower_max_purge_speed.md) | 最大速度（mm/s） | `float` | `90` | min=10 |
| [`wipe_tower_wall_type`](../settings/process/multimaterial/wipe_tower_wall_type.md) | 墙体类型 | `enum` | `"rectangle"` | values=["rectangle","cone","rib"] |
| [`wipe_tower_cone_angle`](../settings/process/multimaterial/wipe_tower_cone_angle.md) | 稳定锥体顶角（°） | `float` | `30` | min=0; max=90 |
| [`wipe_tower_extra_rib_length`](../settings/process/multimaterial/wipe_tower_extra_rib_length.md) | 额外加强筋长度（mm） | `float` | `0` | max=300 |
| [`wipe_tower_rib_width`](../settings/process/multimaterial/wipe_tower_rib_width.md) | 加强筋宽度（mm） | `float` | `8` | min=0 |
| [`wipe_tower_fillet_wall`](../settings/process/multimaterial/wipe_tower_fillet_wall.md) | 墙体加圆角 | `bool` | `true` | — |
| [`wipe_tower_no_sparse_layers`](../settings/process/multimaterial/wipe_tower_no_sparse_layers.md) | 无稀疏层 （实验） | `bool` | `false` | — |
| [`wipe_tower_wall_gap`](../settings/process/multimaterial/wipe_tower_wall_gap.md) | 外墙缺口 | `bool` | `true` | — |
| `wipe_tower_rotation_angle` | 擦拭塔旋转角度（°） | `float` | `0` | — |
| [`prime_tower_enable_framework`](../settings/process/multimaterial/prime_tower_enable_framework.md) | 内支撑肋 | `bool` | `false` | — |
| [`enable_tower_interface_features`](../settings/process/multimaterial/enable_tower_interface_features.md) | 启用擦拭塔接触层功能 | `bool` | `false` | — |
| [`enable_tower_interface_cooldown_during_tower`](../settings/process/multimaterial/enable_tower_interface_cooldown_during_tower.md) | 擦拭塔期间从接触层加速状态冷却 | `bool` | `false` | — |
| [`single_extruder_multi_material_priming`](../settings/process/multimaterial/single_extruder_multi_material_priming.md) | 所有挤出机画线 | `bool` | `false` | — |

#### 特征用耗材

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`wall_filament`](../settings/process/multimaterial/wall_filament.md) | 墙 | `int` | `1` | min=1 |
| [`sparse_infill_filament`](../settings/process/multimaterial/sparse_infill_filament.md) | 填充 | `int` | `1` | min=1 |
| [`solid_infill_filament`](../settings/process/multimaterial/solid_infill_filament.md) | 实心填充 | `int` | `1` | min=1 |
| [`wipe_tower_filament`](../settings/process/multimaterial/wipe_tower_filament.md) | 色塔 | `int` | `0` | min=0 |

#### Ooze 预防

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`ooze_prevention`](../settings/process/multimaterial/ooze_prevention.md) | 开启 | `bool` | `false` | — |
| [`standby_temperature_delta`](../settings/process/multimaterial/standby_temperature_delta.md) | 软化温度（∆℃） | `int` | `-5` | min=-1500; max=1500 |
| [`preheat_time`](../settings/process/multimaterial/preheat_time.md) | 预热时间（s） | `float` | `30` | min=0; max=120 |
| [`preheat_steps`](../settings/process/multimaterial/preheat_steps.md) | 预热步骤 | `int` | `1` | min=1; max=10 |
| [`delta_temperature`](../settings/process/multimaterial/delta_temperature.md) | Preheat delta temperature（∆°C） | `int` | `0` | min=-50; max=50 |

#### 换料冲刷选项

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`flush_into_infill`](../settings/process/multimaterial/flush_into_infill.md) | 冲刷到对象的填充 | `bool` | `false` | — |
| [`flush_into_objects`](../settings/process/multimaterial/flush_into_objects.md) | 冲刷到这个对象 | `bool` | `false` | — |
| [`flush_into_support`](../settings/process/multimaterial/flush_into_support.md) | 冲刷到对象的支撑 | `bool` | `true` | — |

#### 高级

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`interlocking_beam`](../settings/process/multimaterial/interlocking_beam.md) | 启用互锁梁 | `bool` | `false` | — |
| [`interface_shells`](../settings/process/multimaterial/interface_shells.md) | 接触面外壳 | `bool` | `false` | — |
| [`mmu_segmented_region_max_width`](../settings/process/multimaterial/mmu_segmented_region_max_width.md) | 分段区域的最大宽度（mm） | `float` | `0` | min=0 |
| [`mmu_segmented_region_interlocking_depth`](../settings/process/multimaterial/mmu_segmented_region_interlocking_depth.md) | 分割区域的交错深度（mm） | `float` | `0` | min=0 |
| [`interlocking_beam_width`](../settings/process/multimaterial/interlocking_beam_width.md) | 互锁梁宽度（mm） | `float` | `0.8` | min=0.01 |
| [`interlocking_orientation`](../settings/process/multimaterial/interlocking_orientation.md) | 互锁方向（°） | `float` | `22.5` | min=0; max=360 |
| [`interlocking_beam_layer_count`](../settings/process/multimaterial/interlocking_beam_layer_count.md) | 互锁梁层数 | `int` | `2` | min=1 |
| [`interlocking_depth`](../settings/process/multimaterial/interlocking_depth.md) | 互锁深度 | `int` | `2` | min=1 |
| [`interlocking_boundary_avoidance`](../settings/process/multimaterial/interlocking_boundary_avoidance.md) | 互锁与边界的留白量 | `int` | `2` | min=0 |

#### 混色（试验）

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`dithering_local_z_mode`](../settings/process/multimaterial/dithering_local_z_mode.md) | 混色细分层高 | `bool` | `false` | — |
| [`dithering_local_z_whole_objects`](../settings/process/multimaterial/dithering_local_z_whole_objects.md) | 全域生效 | `bool` | `false` | — |
| [`dithering_local_z_infill`](../settings/process/multimaterial/dithering_local_z_infill.md) | 应用到填充 | `bool` | `false` | — |

### 5.6 其他

#### 裙边

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`skirt_loops`](../settings/process/others/skirt_loops.md) | Skirt圈数 | `int` | `1` | min=0; max=10 |
| [`skirt_type`](../settings/process/others/skirt_type.md) | Skirt类型 | `enum` | `"combined"` | values=["combined","perobject"] |
| [`min_skirt_length`](../settings/process/others/min_skirt_length.md) | Skirt最小挤出长度（mm） | `float` | `0` | min=0 |
| [`skirt_distance`](../settings/process/others/skirt_distance.md) | Skirt距离（mm） | `float` | `2` | min=0; max=60 |
| [`skirt_start_angle`](../settings/process/others/skirt_start_angle.md) | Skirt起始点（°） | `float` | `-135` | min=-180; max=180 |
| [`skirt_speed`](../settings/process/others/skirt_speed.md) | Skirt速度（mm/s） | `float` | `50` | min=0 |
| [`skirt_height`](../settings/process/others/skirt_height.md) | Skirt高度（层） | `int` | `1` | max=10000 |
| [`draft_shield`](../settings/process/others/draft_shield.md) | 风挡 | `enum` | `"disabled"` | values=["disabled","enabled"] |
| [`single_loop_draft_shield`](../settings/process/others/single_loop_draft_shield.md) | 首层后单圈 | `bool` | `false` | — |

#### Brim

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`brim_type`](../settings/process/others/brim_type.md) | Brim类型 | `enum` | `"auto_brim"` | values=["auto_brim","brim_ears","painted","outer_only","inner_only","outer_and_inner","no_brim"] |
| [`brim_width`](../settings/process/others/brim_width.md) | Brim宽度（mm） | `float` | `0` | min=0; max=100 |
| [`brim_object_gap`](../settings/process/others/brim_object_gap.md) | Brim与模型的间隙（mm） | `float` | `0` | min=0; max=2 |
| [`brim_ears_max_angle`](../settings/process/others/brim_ears_max_angle.md) | 圆盘最大角度（°） | `float` | `125` | min=0; max=180 |
| [`brim_ears_detection_length`](../settings/process/others/brim_ears_detection_length.md) | 圆盘检测半径（mm） | `float` | `1` | min=0 |

#### 特殊模式

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`slicing_mode`](../settings/process/others/slicing_mode.md) | 切片模式 | `enum` | `"regular"` | values=["regular","even_odd","close_holes"] |
| [`print_sequence`](../settings/process/others/print_sequence.md) | 打印顺序 | `enum` | `"by layer"` | values=["by layer","by object"] |
| [`print_order`](../settings/process/others/print_order.md) | 层内打印顺序 | `enum` | `"default"` | values=["default","as_obj_list"] |
| [`spiral_mode`](../settings/process/others/spiral_mode.md) | 旋转花瓶 | `bool` | `false` | — |
| [`spiral_mode_smooth`](../settings/process/others/spiral_mode_smooth.md) | 光滑螺旋模式 | `bool` | `false` | — |
| [`spiral_mode_max_xy_smoothing`](../settings/process/others/spiral_mode_max_xy_smoothing.md) | 最大XY平滑阈值（mm 或 %） | `float_or_percent` | `"200%"` | min=0; max=1000 |
| [`spiral_starting_flow_ratio`](../settings/process/others/spiral_starting_flow_ratio.md) | 螺旋开始流量比 | `float` | `0` | min=0; max=1 |
| [`spiral_finishing_flow_ratio`](../settings/process/others/spiral_finishing_flow_ratio.md) | 螺旋结束流量比 | `float` | `0` | min=0; max=1 |
| [`timelapse_type`](../settings/process/others/timelapse_type.md) | 延时摄影 | `enum` | `"0"` | values=["0","1"] |

#### 绒毛表面

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`fuzzy_skin`](../settings/process/others/fuzzy_skin.md) | 绒毛表面 | `enum` | `"none"` | values=["none","external","all","allwalls"] |
| [`fuzzy_skin_mode`](../settings/process/others/fuzzy_skin_mode.md) | 绒毛表面生成器模式 | `enum` | `"displacement"` | values=["displacement","extrusion","combined"] |
| [`fuzzy_skin_noise_type`](../settings/process/others/fuzzy_skin_noise_type.md) | 绒毛噪声类型 | `enum` | `"classic"` | values=["classic","perlin","billow","ridgedmulti","voronoi"] |
| [`fuzzy_skin_point_distance`](../settings/process/others/fuzzy_skin_point_distance.md) | 绒毛表面点间距（mm） | `float` | `0.3` | min=0; max=5 |
| [`fuzzy_skin_thickness`](../settings/process/others/fuzzy_skin_thickness.md) | 绒毛表面厚度（mm） | `float` | `0.2` | min=0; max=1 |
| [`fuzzy_skin_scale`](../settings/process/others/fuzzy_skin_scale.md) | 绒毛表面特征尺寸（mm） | `float` | `1` | min=0.1; max=500 |
| [`fuzzy_skin_octaves`](../settings/process/others/fuzzy_skin_octaves.md) | 绒毛噪声倍频 | `int` | `4` | min=1; max=10 |
| [`fuzzy_skin_persistence`](../settings/process/others/fuzzy_skin_persistence.md) | 绒毛噪声持续性 | `float` | `0.5` | min=0.01; max=1 |
| [`fuzzy_skin_first_layer`](../settings/process/others/fuzzy_skin_first_layer.md) | 绒毛表面应用至首层 | `bool` | `false` | — |

#### G-code 输出

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`reduce_infill_retraction`](../settings/process/others/reduce_infill_retraction.md) | 减小填充回抽 | `bool` | `false` | — |
| [`gcode_add_line_number`](../settings/process/others/gcode_add_line_number.md) | 标注行号 | `bool` | `false` | — |
| [`gcode_comments`](../settings/process/others/gcode_comments.md) | 注释G-code | `bool` | `false` | — |
| [`gcode_label_objects`](../settings/process/others/gcode_label_objects.md) | 标注模型 | `bool` | `true` | — |
| [`exclude_object`](../settings/process/others/exclude_object.md) | 对象排除 | `bool` | `false` | — |
| [`filename_format`](../settings/process/others/filename_format.md) | 文件名格式 | `string` | `"{input_filename_base}_{filament_type[initial_tool]}_{print_time}.gcode"` | — |

#### 后处理脚本

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`post_process`](../settings/process/others/post_process.md) | 后处理脚本 | `strings` | `[]` | — |

#### 注释

| 键 | 显示名（单位） | 逻辑类型 | 默认值 | 范围/候选/标记 |
|---|---|---|---|---|
| [`notes`](../settings/process/others/notes.md) | 配置注释 | `string` | `""` | — |

## 6 一致性要求

生产或修改预设时应检查：

1. JSON 可解析，文件名、`name`、`type`、目录及厂商清单相互对应。
2. `inherits` 能找到同类父项，继承链无环；改名时同步更新子项、清单和引用。
3. 参数使用目标版本支持的键与序列化形态；按完整继承结果检查类型、范围和相互约束。
4. 实例的适配关系、名称、标识和实际参数一致；默认工艺及型号引用可解析。
5. 检查 UI 条件以及特殊序列化，再使用目标版本 Snapmaker Orca 加载并验证。

## 深入阅读

- 字段与参数页面的三方对账、未覆盖键清单与处理状态见 [10-对账-预设格式文档与参数页面](../../docs/10-对账-预设格式文档与参数页面.md)。
