# 内置占位符变量（Built-in Placeholders & Variables）

← [Wiki 首页](../home.md)

在自定义 G-code 里用 `{变量名}` 引用切片状态和设置值，例如层变更 G-code 里写 `{layer_num}` 输出当前层号。键页元数据行的 `[Variables]` 列出的就是该小节可用的配置键名。

两个基本事实：

1. **每个设置键本身就是占位符**，变量名 = 配置键名：`{layer_height}`；列表键用 `[索引]` 取值（索引从 0 起），如 `{first_layer_temperature[0]}`。
2. fork 的占位符在生成 G-code 时由切片器注入，代码位于 `src/libslic3r/GCode.cpp`（fork 仓库 iesteem/OrcaSlicer）。完整清单持续扩充中，本文先收录最常用的一批。

## 语法

- 花括号 `{name}`，支持表达式：算术、比较、逻辑、三目 `cond ? a : b`、文本拼接 `+`、正则 `=~` / `!~`
- 常用函数：`int` `round` `min` `max` `digits` `zdigits` `random` `interpolate_table` `one_of` `regex_replace` `size` `is_nil` `filament_change`
- 条件块：`{if}…{elsif}…{else}…{endif}`
- 旧式 `[name]` 只能取单个占位符；布尔值在 `{}` 里输出 `true/false`，在 `[]` 里输出 `1/0`

## 哪里能用

- 所有自定义 G-code 字段（开机/关机、耗材起止、层变更、延时摄影、换料、换挤出角色等）；部分字段另有专属占位符
- 文件名模板（`filename_format`）只支持其中子集，用不支持的变量会导致模板处理失败

## 常用变量

### 层数与高度

| 变量 | 含义 |
|---|---|
| `layer_num` | 当前层号，从 0 数起；首层之前为 −1 |
| `layer_z` | 当前层顶面高度（mm） |
| `total_layer_count` | 总层数 |
| `first_layer_height` | 首层厚度（mm）。注意占位符用旧名，配置键为 `initial_layer_print_height` |
| `max_print_z` | 最高对象高度（向上取整） |

### 温度

| 变量 | 含义 |
|---|---|
| `bed_temperature[]` | 逐耗材的床温 |
| `bed_temperature_initial_layer[]` / `first_layer_bed_temperature[]` | 逐耗材的首层床温 |
| `chamber_temperature[]` | 逐耗材的舱温 |
| `old_filament_temp` / `new_filament_temp` | 换料 G-code 里旧/新耗材的喷嘴温度 |

### 首层几何

| 变量 | 含义 |
|---|---|
| `first_layer_print_min` / `first_layer_print_max` | 首层最小/最大 X,Y |
| `first_layer_print_size` | 首层宽 × 深 |

### 工具与统计

| 变量 | 含义 |
|---|---|
| `current_extruder` / `current_filament_id` | 当前耗材（同义） |
| `num_extruders` | 物理挤出机数 |
| `print_time` | 预计耗时（如 `2h15m`），生成后填充 |
| `used_filament` / `total_weight` | 耗材长度（m）/ 重量（g），生成后填充 |
| `input_filename_base` | 首个对象文件名（去扩展名） |

> [!WARNING]
> 标注"生成后填充"的值（`print_time`、`total_weight` 等）只能原样输出，不能参与运算，否则报错 "This value is known only after the G-code is generated."

## 深入阅读

- [G-code 文件规范](../specification/gcode.3mf/gcode_standard.md)：G-code 自描述块与统计段和这些占位符同源
- 上游完整清单（约 170 个变量、逐 G-code 字段对照表）：上游完整清单见 OrcaSlicer wiki 的 built_in_placeholders_variables 页

> [!NOTE]
> 占位符集合随版本演进，上游与 fork 存在差异（如新旧键名并存）。拿不准时直接在自定义 G-code 里实测验证。
