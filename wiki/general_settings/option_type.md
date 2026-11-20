# Option Type（参数取值类型）

← [Wiki 首页](../home.md)

设置键页面元数据行的 `[Type]` 标记该参数接受什么形态的值，决定你在界面里怎么填、命令行怎么传（见 [CLI 模式](../cli/cli_mode.md)）。类型来自 fork `src/libslic3r/PrintConfig.cpp` 中各键的 `coXxx` 定义（枚举在 `src/libslic3r/Config.hpp`）。

## Boolean

开/关二选一，界面上是勾选框。命令行里布尔开关**只写选项名即生效**（`--info`）；要关闭必须用等号 `--info=0`。注意 `--info 0`（空格分隔）并不会关闭它——`0` 会被当成输入文件参数。

## Integer, Float, Percentage

- `Integer`：整数。
- `Float`：小数（如层高 0.2）。
- `Percentage`：可带 `%` 的百分数（如稀疏填充 20%）。

界面里显示的单位（mm、mm/s、℃、s）只是标注，不是值的一部分；命令行传值永远只写数字：`--layer-height=0.2`、`--sparse-infill-density=20%`。

## Text

文本串，如文件名、标签、G-code 片段：`--outputdir=D:\exports`。

## Choice

固定候选中的某一个（界面上下拉框）。填配置键的原始值（通常为 snake_case 英文），不要填界面显示文案——文案会随翻译变化。可用候选见键页正文或 `PrintConfig.cpp` 中该键的枚举定义。

## Point

X,Y 坐标对，两个逗号分隔的数字：`--align-xy=100,100`。

## List Types

以上类型都可能"按耗材/按对象逐个取值"而成为列表。命令行传逗号分隔的序列，**位置 = 索引（从 0 起）**：`--retraction-length=0.8,0.8,1.2,0.8` 是四个耗材槽各自的回抽长度。列表的补齐与追加行为见 [Vector (multi-value) flags](../cli/cli_mode.md#vector-multi-value-flags)。

## Default Value

键页 `[Default]` 行：你不做任何修改时该参数使用的值，取自 `PrintConfig.cpp` 的静态默认定义。

- fork 源码没有该键、或该键无静态默认值时显示 `—`（注入约定见 [docs/09 §3](../../docs/09-对账-PrintConfig元数据提取与键页注入.md)）。

## Unit

键页 `[Unit]` 行：该参数数值的单位，取自 fork `PrintConfig.cpp` 中该键的 `sidetext` 定义（即设置界面输入框旁的标注文字）。仅源码定义了单位时才显示此行；复合单位原样显示（如 `mm or %`、`mm/s²`）。`[Default]` 与 `[Range]` 行不再内嵌单位，统一看本行（2026-11-20 裁决，见 [docs/09 §3](../../docs/09-对账-PrintConfig元数据提取与键页注入.md)）。

## Range

键页 `[Range]` 行：源码为该键定义的取值上下限（如 `0–1`、`≥ 0`，单位见 `[Unit]` 行）。仅当 min/max 在 `PrintConfig.cpp` 里有明确定义时才注入此行；没有约束的参数不显示。

## Aliases

键页 `[Aliases]` 行：同一参数的历史键名/别名，旧版配置文件或 3mf 里可能写旧名。仅个别键存在（fork 目前仅 `inner_wall_speed` 一处）。

> [!NOTE]
> 别名与"gcode 嵌入名"是两套标注：嵌入名指序列化进 G-code 注释段时实际落盘的键名（见相关键页 Location 行下方的"gcode 嵌入名"标注）；别名则是 fork 源码层面已废弃的叫法。
