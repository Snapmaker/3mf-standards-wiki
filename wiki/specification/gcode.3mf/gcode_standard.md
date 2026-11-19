# G-code 文件规范 v1.0（草案）

← [Wiki 首页](../../home.md)


> 规范性用语：**应 / 不应** = 要求（MUST / MUST NOT）；**宜 / 不宜** = 推荐（SHOULD）；**可** = 允许（MAY）。
>
> 与 [gcode.3mf 规范](gcode_3mf_standard.md) 的分工：容器规范规定"G-code 怎么装进包"（部件、关系、MD5），本规范规定"G-code 文件本身长什么样"（结构、行法、指令、标记、统计）。裸导出的 `.gcode` 与 `.gcode.3mf` 内嵌的 `Metadata/plate_N.gcode` 是同一产物，同受本规范约束。

## 目录

- [前言](#前言)
- [引言](#引言)
- [1 范围](#1-范围)
- [2 规范性引用文件](#2-规范性引用文件)
- [3 术语和定义](#3-术语和定义)
- [4 文件总体结构](#4-文件总体结构)
  - [4.1 布局总览](#41-布局总览)
  - [4.2 字符编码与换行](#42-字符编码与换行)
  - [4.3 数值与精度](#43-数值与精度)
- [5 行语法与指令集](#5-行语法与指令集)
  - [5.1 行的构成](#51-行的构成)
  - [5.2 指令核心子集](#52-指令核心子集)
  - [5.3 坐标系、单位与模态约定](#53-坐标系单位与模态约定)
- [6 注释标记体系](#6-注释标记体系)
  - [6.1 标记行与普通注释](#61-标记行与普通注释)
  - [6.2 层标记](#62-层标记)
  - [6.3 特征标记：TYPE / WIDTH / HEIGHT](#63-特征标记type--width--height)
  - [6.4 对象标记与对象取消](#64-对象标记与对象取消)
  - [6.5 事件标记](#65-事件标记)
  - [6.6 保留标记字](#66-保留标记字)
- [7 自描述块与统计](#7-自描述块与统计)
  - [7.1 头部摘要：HEADER_BLOCK](#71-头部摘要header_block)
  - [7.2 缩略图：THUMBNAIL_BLOCK](#72-缩略图thumbnail_block)
  - [7.3 流量摘要行](#73-流量摘要行)
  - [7.4 尾部统计](#74-尾部统计)
  - [7.5 参数快照：CONFIG_BLOCK](#75-参数快照config_block)
  - [7.6 内部占位符](#76-内部占位符)
- [8 一致性要求](#8-一致性要求)
  - [8.1 生产者要求](#81-生产者要求)
  - [8.2 消费者要求](#82-消费者要求)
  - [8.3 校验与解析容错](#83-校验与解析容错)
- [附录 A（资料性）示例文件剖析](#附录-a资料性示例文件剖析)
- [附录 B（资料性）与固件方言的关系](#附录-b资料性与固件方言的关系)
- [附录 C（资料性）源码索引](#附录-c资料性源码索引)
- [参考文献](#参考文献)

## 前言

本规范规定 Snapmaker Orca 面向 **Snapmaker 机型**切片导出的文本 G-code 文件的格式，基准机型 **Snapmaker U1**（Klipper 方言，预设继承链 `fdm_U1`）。技术内容基于 fork 2.4.x 源码导出路径、U1 机型预设与真实导出包实测编纂。

本文件与 [gcode.3mf 规范](gcode_3mf_standard.md)（容器）、[3mf 工程文件规范](../3mf/3mf_standard.md)（工程文件）构成一组：工程 `.3mf` 保存"怎么切"，`.gcode.3mf` 打包"切出来的结果"，本规范描述其中执行主体——G-code 本身。

## 引言

切片产物需要一个既能让机器直接执行、又能被 APP / 查看器 / 后处理工具理解的文本文件。本格式在"给机器的指令流"之外，用纯注释承载元数据：

- **头部**：生成器、总层数、耗材密度 / 丝径、最大打印高度、base64 缩略图——供设备选文件、显示预览；
- **主体**：逐层组织，层 / 特征 / 对象边界都有标记注释，G1 运动流为核心——供固件执行、查看器逐层回放、取消对象插件定位；
- **尾部**：耗时与耗材统计、完整参数快照（CONFIG_BLOCK）——供完成提示、问题排查、参数回读。

一句话：**指令行是给机器的，注释是给所有人的**；注释全部以 `;` 开头，机器天然忽略，人 / 工具各取所需。

## 1 范围

本规范规定了 G-code 文件的布局、字符与行语法、数值精度、指令核心子集、注释标记体系、自描述块与统计行，以及生产者 / 消费者的一致性要求。

本规范适用于：

- **生产者**——生成 G-code 的切片软件（Snapmaker Orca）；
- **消费者**——执行或解析 G-code 的打印机固件、上位机、查看器、后处理与统计工具。

本规范不规定：机型方言与私有指令（由机型预设的起始 / 结束 G-code 与目标固件决定，见附录 B）、G-code 语言的完整文法（历史上继承自 NIST RS274NGC，事实标准见参考文献）、传输与封装完整性（属容器规范，见 [gcode.3mf 规范](gcode_3mf_standard.md) 第 6.5、8.3 节）。

## 2 规范性引用文件

| 引用 | 版本 / 编号 | 用途 |
|---|---|---|
| IETF RFC 3629（UTF-8） | — | 注释中文本字符编码 |
| IETF RFC 4648（Base64） | — | 缩略图块编码 |
| PNG（ISO/IEC 15948） | 第二版 | 默认缩略图图像编码 |

## 3 术语和定义

| 术语 | 定义 |
|---|---|
| 行（line） | 以 `\n` 结束的文本序列，是文件的最小组成单位 |
| 命令字 | 行首的可执行指令：`G<n>`、`M<n>` 或 `T<n>` |
| 参数字 | 命令字后的"字母 + 数值"对，如 `X100.5`、`S210` |
| 模态（modal） | 参数字可省略、值延续到后续行的性质（如 G1 的轴坐标与 F） |
| 注释（comment） | `;` 起至行尾的文本，机器不执行 |
| 标记行（tag line） | 格式与语义固定的结构化注释，如 `;LAYER_CHANGE`、`;TYPE:Top surface` |
| 块（block） | 一对起止标记行包住的注释区，如 HEADER_BLOCK、CONFIG_BLOCK |
| 方言（flavor） | 目标固件家族（Marlin / Klipper / RepRapFirmware 等），决定少量指令差异；U1 为 Klipper |
| 生产者 / 消费者 | 同 [gcode.3mf 规范](gcode_3mf_standard.md) 第 3 章 |

## 4 文件总体结构

### 4.1 布局总览

完整布局自上而下：

```text
xxx.gcode
├── ; HEADER_BLOCK_START … HEADER_BLOCK_END          ← 文件摘要（7.1）
├── ; THUMBNAIL_BLOCK_START … END（0..N 幅）         ← base64 缩略图（7.2）
├── ; … extrusion width = …（每打印区域 6 行）        ← 流量摘要（7.3）
├── ; EXECUTABLE_BLOCK_START
│   ├── 对象取消定义（Klipper：EXCLUDE_OBJECT_DEFINE，见 6.4）
│   ├── 热床 / 喷头预热（Marlin 方言自动补写；U1 为 Klipper，预热由起始 G-code 的宏负责）
│   ├── ;TYPE:Custom
│   ├── 机型起始 G-code（预设注入，占位符已展开；U1 为 PRINT_START 宏族）
│   ├── 通用 preamble：G90 → G21 → M82|M83 → G92 E0（见 5.3）
│   ├── T<初始工具>
│   └── 逐层主体（每层见 6.2；层内为 G1/G2/G3 运动流与标记行）
├── 机型结束 G-code → postamble（关温度 / 风扇等）
├── ; EXECUTABLE_BLOCK_END
├── ; filament used … / ; total … 统计行             ← 尾部统计（7.4）
└── ; CONFIG_BLOCK_START … CONFIG_BLOCK_END          ← 参数快照（7.5）
```

`EXECUTABLE_BLOCK_START` / `EXECUTABLE_BLOCK_END` 之间是机器执行语义的完整范围；两标记之外全部为注释。事件标记（6.5）与对象标记（6.4）出现在逐层主体内部。

### 4.2 字符编码与换行

- 文件为文本文件：指令、参数与数值均为 ASCII；注释中的对象名等文本可为 UTF-8。不含 BOM。
- 行结束符一律为 `\n`（LF）。生产者导出时强制小数点为 `.` 的区域设置，全文件不得出现其他小数分隔符。
- 进入 `.gcode.3mf` 容器时按原始字节压入，任何换行符 / 字符集转换都会破坏容器侧 MD5 校验（见容器规范 6.5）。

### 4.3 数值与精度

| 内容 | 精度 | 说明 |
|---|---|---|
| 运动参数 `X/Y/Z/I/J/F` | ≤3 位小数 | 导出前量化到 0.001；无尾随零 |
| 挤出参数 `E` | ≤5 位小数 | 量化到 0.00001；E 与 XY 精度差约两个数量级是物理必然（丝截面远小于挤出截面） |
| 标记行 `;Z:` `;HEIGHT:` `;WIDTH:` | `%g` 有效数字 | 无尾随零，如 `;Z:0.25` |
| 统计行 | 两位小数 / 整数 | 如 `171.19`、`1155` |
| 温度 `S`、风扇 `S`、工具号 | 整数 | — |

数值格式：十进制、可选前导 `-`、必须 `.` 作小数点；不使用科学计数法与 `+` 前缀。

## 5 行语法与指令集

### 5.1 行的构成

```text
[空白] 命令字 参数字… [";" 注释] "\n"
```

- 空行与纯注释行合法且大量存在；机器对二者均无动作。
- 命令字与参数字母大写；参数字内字母与数值之间无空白。
- **不使用行号（`N`）与校验和（`*`）**：行号仅为开发用隐藏选项，默认关闭；固件不得依赖二者。
- 逐行注释有两种：普通注释（人读，如 Verbose G-code 开启时运动行尾的用途说明）与标记行（结构化，第 6 章）。

### 5.2 指令核心子集

切片核心产生的可执行行只含下表指令；预设注入的起始 / 结束 G-code 不受此限（见附录 B）。

**运动与坐标**

| 指令 | 参数 | 语义 |
|---|---|---|
| `G1` | `X Y Z E F`（均可省略） | 直线运动 + 挤出。**空走与挤出统一用 G1**，区别仅在是否带 E；F 为模态 |
| `G2` / `G3` | `X Y I J E F` | 顺 / 逆时针圆弧。仅启用"圆弧拟合"选项时出现；`I/J` 为起点到圆心的相对偏移，语义与 Marlin / Klipper 一致 |
| `G4` | `P` / `S` | 驻留（毫秒 / 秒），见预设与事件 |
| `G10` / `G11` | — | 固件回抽 / 回填，仅"使用固件回抽"方言启用时替代 `G1 E-…` 形式 |
| `G21` | — | 单位 mm（preamble 固定输出） |
| `G90` | — | 绝对坐标（preamble 固定输出） |
| `G91` | — | 相对坐标（仅预设注入使用） |
| `G92` | `E0` | 归零 E 计数（preamble 与绝对 E 模式下周期性输出） |

**温度**

| 指令 | 参数 | 语义 |
|---|---|---|
| `M104` / `M109` | `S T` | 喷头设定 / 设定并等待（自动补热与逐层首层温度） |
| `M140` / `M190` | `S`（或 `R`） | 热床设定 / 设定并等待 |
| `M141` / `M191` | `S` | 腔体温度设定 / 等待（机型支持时） |

> [!NOTE] U1 实况
> U1 为 Klipper 方言，切片核心**不**自动补写温度指令（预热完全由起始 G-code 的 `PRINT_START` 宏族完成，见附录 B）；上表 M 指令在 U1 文件中出现时通常来自预设注入或换工具流程。

**风扇与工具**

| 指令 | 参数 | 语义 |
|---|---|---|
| `M106` | `S`(0–255) | 部件风扇转速 |
| `M107` | — | 部件风扇关闭 |
| `T<id>` | — | 切换挤出工具；多盘多耗材打印的换色由工具排序生成 T 命令组 |
| `M486` / `EXCLUDE_OBJECT_*` | 见 6.4 | 对象取消（按方言二选一） |

### 5.3 坐标系、单位与模态约定

- 长度单位 mm；`F` 进给率为 **mm/min**（内部计算 mm/s × 60 写出）；温度 ℃。
- 坐标系为机器打印空间：XYZ 右手系、Z 向上；输出前已扣除所选盘的原点偏移。床原点取床中心还是左下角由机型预设决定，**本文件不自证原点，消费者不应假设**。
- 位置模态：G1 行只写发生变化的轴；省略的轴保持当前值。F 同理。
- 挤出模式由 preamble 声明，默认 `M83`（相对 E，每行 E 为增量）；`M82`（绝对 E）时 E 为累积坐标并周期性 `G92 E0` 归零。消费者应按实际声明解析 E。
- 抬升（z-hop）与螺旋抬升体现为普通 G1/G2/G3 行，无专门指令。

## 6 注释标记体系

### 6.1 标记行与普通注释

标记行是**格式与语义固定**的注释，供查看器、设备屏幕与统计工具消费。规范形式为 `;<标记字><载荷>`，标记字取值见 6.6。标记行不得被任何后处理工具删除或改写其相对顺序（层内首条特征标记必须在首个挤出运动行之前）。

### 6.2 层标记

每个打印层以三行固定开场：

```text
;LAYER_CHANGE
;Z:23.10
;HEIGHT:0.25
```

| 行 | 载荷 | 约定 |
|---|---|---|
| `;LAYER_CHANGE` | 无 | 层边界；查看器层回放、层数统计（`m_layer_id` 计数）都以此为准 |
| `;Z:<z>` | 层顶绝对 Z（mm） | 与层内 G1 Z 值一致 |
| `;HEIGHT:<h>` | 本层厚度（mm） | 首层 = 首层 Z 本身，其后 = 本层 Z − 上层 Z；可变层高时逐层不同 |

用户配置的"每层变更 G-code"（`before_layer_change_gcode` / `layer_change_gcode`）紧随其后注入，可引用 `layer_num`、`layer_z` 占位变量。U1 预设在此注入 `G92 E0`（相对 E 下防累积漂移）、`TIMELAPSE_TAKE_FRAME`（延时摄影）与 `SET_PRINT_STATS_INFO TOTAL_LAYER=<n> CURRENT_LAYER=<n>`（固件层数上报；其中 `TOTAL_LAYER` 数值会被导出器改写为实测层数，与头部 `total layer number` 同源）。

### 6.3 特征标记：TYPE / WIDTH / HEIGHT

层内挤出特征切换时输出（只在值变化时输出）：

```text
;TYPE:Outer wall
;WIDTH:0.42
```

| 行 | 载荷 | 约定 |
|---|---|---|
| `;TYPE:<role>` | 特征角色名 | 枚举见下表；`;TYPE:Custom` 另用于起始 / 结束 G-code 区段 |
| `;WIDTH:<w>` | 当前线宽（mm） | 线宽变化时输出 |
| `;HEIGHT:<h>` | 当前层高（mm） | 层高变化（可变层高 / 特征内变化）时输出，语义同 6.2 |

角色枚举（源码基准为英文；生成端映射经过本地化层，非英文 UI 环境可能输出本地化值——**消费者应未知则忽略，不应依赖 TYPE 值做流程控制**）：

| `;TYPE:` 值 | 含义 | 值 | 含义 |
|---|---|---|---|
| `Outer wall` | 外壁 | `Top surface` | 顶面 |
| `Inner wall` | 内壁 | `Bottom surface` | 底面 |
| `Overhang wall` | 悬垂壁 | `Bridge` | 桥接 |
| `Sparse infill` | 疏松填充 | `Internal Bridge` | 内部桥接 |
| `Internal solid infill` | 内部实心填充 | `Ironing` | 熨平 |
| `Gap infill` | 缝隙填充 | `Skirt` | 裙边 |
| `Brim` | 底盘（象脚） | `Support` | 支撑主体 |
| `Support interface` | 支撑接口层 | `Support transition` | 支撑过渡 |
| `Prime tower` | 调色塔（擦料塔） | `Custom` | 自定义区段 |
| `Multiple` / `Undefined` | 混合 / 未定义 | | |

### 6.4 对象标记与对象取消

**对象标记注释**（`gcode_label_objects` 选项，默认开启）：逐对象打印或对象切换时输出

```text
; printing object 支架 id:0 copy 0
; stop printing object 支架 id:0 copy 0
```

`id` 为工程内对象序号，`copy` 为实例序号；名称可含非 ASCII。

**对象取消指令**按方言注入（定义块位于执行块开头，起止指令包裹各对象的打印区段）。U1 为 Klipper 方言，走 EXCLUDE_OBJECT 一族：

| 方言 | 定义 | 开始 / 结束 |
|---|---|---|
| **Klipper（U1）** | `EXCLUDE_OBJECT_DEFINE NAME=<名> CENTER=<x>,<y> POLYGON=<顶点串>` | `EXCLUDE_OBJECT_START NAME=<名>` / `EXCLUDE_OBJECT_END NAME=<名>` |
| Marlin / RRF | `M486 S<序号>` + `M486 A<名>`（RRF 合并为一行 `A"<名>"`）+ `M486 S-1` 收尾 | `M486 S<序号>` 开始（无显式结束指令） |

### 6.5 事件标记

逐层事件（暂停、自定义 G-code、模板 G-code）以标记行 + 注入内容成对出现：

| 标记行 | 后随内容 | 触发 |
|---|---|---|
| `;PAUSE_PRINT` | 机型"暂停打印 G-code"（`machine_pause_gcode`；U1 预设为 `M600`） | 用户插入的暂停点 |
| `;CUSTOM_GCODE` | 用户自定义文本，原样注入 | 用户插入的自定义 / 模板 G-code |
| `; MANUAL_TOOL_CHANGE T<id>` | 手动换料模式下的 T 命令前缀 | `manual_filament_change` 开启 |

换色 / 换工具不在事件标记之列：多耗材换色由工具排序生成 T 命令组 + 调色塔 / 冲洗路径，属于普通运动流。

### 6.6 保留标记字

生成端内部使用一套保留标记字（源码 `GCodeProcessor::Reserved_Tags_compatible`，Snapmaker 机型走此表）。约定：

1. 最终文件**不应**出现内部占位标记（`_GP_*_PLACEHOLDER` 等）——导出管线会替换或整行删除（见 7.6）；
2. 生产者应拒绝包含保留标记字的自定义 G-code（防注入冲突）；
3. 本规范正文使用的标记字全集：

| 语义 | 标记字 |
|---|---|
| 层切换 | `;LAYER_CHANGE` |
| 层 Z | `;Z:` |
| 层高 | `;HEIGHT:` |
| 特征类型 | `;TYPE:` |
| 线宽 | `;WIDTH:` |
| 暂停 | `;PAUSE_PRINT` |
| 换色 | `;COLOR_CHANGE` |
| 自定义 | `;CUSTOM_GCODE` |
| 手动换料 / 排风扇 / 擦塔 | `; MANUAL_TOOL_CHANGE` / `;_DURING_PRINT_EXHAUST_FAN` / `; WIPE_TOWER_START|END` |

## 7 自描述块与统计

### 7.1 头部摘要：HEADER_BLOCK

文件首块（缩略图格式选 BTT_TFT 时整块不写）：

```text
; HEADER_BLOCK_START
; generated by Snapmaker Orca 2.4.1 on 2026-11-19 at 10:38:35
; total layer number: 1155
; filament_density: 1.24,1.24,1.24,1.24
; filament_diameter: 1.75,1.75,1.75,1.75
; max_z_height: 231.05
; HEADER_BLOCK_END
```

| 行 | 载荷 | 约定 |
|---|---|---|
| `generated by` | 生成器名 + 本地时间戳 | 生成器名固定为 `Snapmaker Orca <版本>`，用于来源追溯 |
| `total layer number` | 实际写出的层数 | 为导出管线统计校正值，非切片前估计 |
| `filament_density` / `filament_diameter` | 逐耗材列表（g/cm³、mm），逗号分隔 | 供重量估算；与容器 `slice_info.config` 的 `weight` 同源数据 |
| `max_z_height` | 最高打印 Z（mm，两位小数） | 全部对象顶层的最大 print_z |

### 7.2 缩略图：THUMBNAIL_BLOCK

紧跟头部，每幅一块，默认两幅（48×48 与 300×300，PNG）：

```text
; THUMBNAIL_BLOCK_START
;
; thumbnail begin 48x48 868
; iVBORw0KGgoAAAA…（每行 ≤78 字符的 base64）
; thumbnail end
; THUMBNAIL_BLOCK_END
```

| 要素 | 约定 |
|---|---|
| `begin` 行 | `; <tag> begin <宽>x<高> <base64 字节数>`；`tag` 按图像格式取 `thumbnail`（PNG）、`thumbnail_JPG`、`thumbnail_QOI` 等 |
| 载荷行 | 每行以 `; ` 起头，base64 续行，单行 ≤78 字符 |
| 尺寸声明 | `begin` 行的 `宽x高`；**实际解码尺寸以图像数据本身为准** |
| 解码失败 | 降级为默认图，不应影响执行 |

### 7.3 流量摘要行

头部之后、执行块之前，每个打印区域输出一组线宽摘要（两位小数，单位 mm）：

```text
; external perimeters extrusion width = 0.42mm
; perimeters extrusion width = 0.45mm
; infill extrusion width = 0.45mm
; solid infill extrusion width = 0.45mm
; top infill extrusion width = 0.42mm
; support material extrusion width = 0.48mm   ← 有支撑时
; first layer extrusion width = 0.50mm        ← 配置了首层线宽时
```

### 7.4 尾部统计

执行块结束后依次输出：

```text
; filament used [mm] = 13792.40, 0, 0, 0
; filament used [cm3] = 33.12, 0, 0, 0
; filament used [g] = 41.13, 0, 0, 0
; filament cost = 12.34, 0, 0, 0             ← 配置了单价时
; total filament used [g] = 41.13
; total filament cost = 12.34
; total filament change = 3                  ← 大于 0 时输出
; total layers count = 1155
; estimated printing time (normal mode) = 6h 25m 39s
; estimated first layer printing time (normal mode) = 8m 12s
; estimated printing time (silent mode) = …   ← 静音机型才输出
```

| 约定 | 说明 |
|---|---|
| 逐耗材列表 | 逗号 + 空格分隔，**未参与打印的挤出机补 0**；长度随耗材槽数，解析不应写死 |
| 时间格式 | `Dd Hh Mm Ss` 自高位起省略零值单位，如 `6h 25m 39s`、`45s` |
| `total layers count` | 实际写出层数，与头部 `total layer number` 应一致 |
| 用途 | 仅展示与预估；消费者不应据此做执行控制。与容器 `slice_info.config` 的 `prediction` / `weight` 可交叉核对 |

### 7.5 参数快照：CONFIG_BLOCK

文件末块：

```text
; CONFIG_BLOCK_START
; layer_height = 0.25
; …（切片时全部生效参数，500～600 键，字典序）
; first_layer_bed_temperature = 55
; bed_shape = 0.5x1,270.5x1,270.5x271,0.5x271
; first_layer_temperature = 215
; first_layer_height = 0.250
; CONFIG_BLOCK_END
```

- 行格式 `; <键> = <值>`；起止两行本身也写成键值样式是历史兼容（老版查看器按配置行解析）。
- 正文键集与取值形态与工程侧 `project_settings.config` 一致（全部字符串形态、数组元素亦然），形态细则见 [gcode.3mf 规范](gcode_3mf_standard.md) 7.1。
- 尾部附加 `bed_shape`（打印区域顶点串，`x` 分隔点、逗号分隔点列）与 `first_layer_height`（三位小数）四个兼容键，供旧工具回读。
- 消费者**不应**据本块重新切片或改写 G-code（同容器规范 8.2）。

### 7.6 内部占位符

导出过程中头部 / 尾部先写入形如 `;_GP_…_PLACEHOLDER`、`;_GP_FIRST_LINE_M73…` 的内部占位行，随后由统计处理器替换为实际统计（耗时、层数、逐耗材用量）或整行删除。**最终交付文件不应残留任何占位行**；解析工具遇 `_*_PLACEHOLDER` 字样应视为生产者缺陷，不应视作数据。

## 8 一致性要求

### 8.1 生产者要求

生产者生成的 G-code **应**：

1. 遵守 4.2 / 4.3 的编码、换行与小数约定；
2. 按 4.1 布局组织块与标记，保证标记行与实际内容一致（层 Z、层数、统计值）；
3. 运动参数与 E 值按 4.3 精度量化；不写行号与校验和（开发选项除外）；
4. preamble 如 5.3 声明坐标系与挤出模式；`G92 E0` 归零策略与声明的 E 模式匹配；
5. 自定义 G-code 注入前完成占位符展开，并拒绝包含保留标记字的内容；
6. 交付文件不含内部占位行；
7. CONFIG_BLOCK 置于文件尾部（7.5）。

### 8.2 消费者要求

消费者**应**：

1. 按行解析；空行、纯注释行跳过；**未知注释 / 未知标记行一律忽略**，不得报错中断；
2. 按 `M82/M83` 实际声明解析 E；按模态规则延续省略的轴与 F；F 按 mm/min 处理；
3. 不假设床原点、不假设逐耗材统计列表长度、不依赖 `;TYPE:` 值做流程控制（6.3）；
4. 统计行与 CONFIG_BLOCK 仅作展示 / 回读，不据此重新切片或改写 G-code；
5. 遇 `_GP_*_PLACEHOLDER` 残留按缺陷处理，不当作数据。

消费者**宜**：解码失败时缩略图降级；对象标记用于逐对象取消时以方言指令（M486 / EXCLUDE_OBJECT）为准、注释仅为辅助。

### 8.3 校验与解析容错

- 行级语法错误的处理由目标固件方言决定，本规范不作强制（Marlin 家族通常报错拒行，Klipper 报错停机）；解析工具（查看器 / 统计）**宜**跳过无法解析的行并计数报告。
- 传输完整性（CRC32 / MD5）由容器层承担，见 [gcode.3mf 规范](gcode_3mf_standard.md) 8.3；裸 `.gcode` 无内建校验，重要场景宜伴随侧车摘要（如 `.md5`）。

## 附录 A（资料性）示例文件剖析

以下为 U1（Klipper 方言）输出的代表性片段（示意，数值为编造的合理值；`PRINT_START` / `TIMELAPSE_TAKE_FRAME` 等宏为 U1 机型预设注入，由固件侧定义）：

```text
; HEADER_BLOCK_START
; generated by Snapmaker Orca 2.4.1 on 2026-11-19 at 10:38:35
; total layer number: 1155
; filament_density: 1.24,1.24,1.24,1.24
; filament_diameter: 1.75,1.75,1.75,1.75
; max_z_height: 231.05
; HEADER_BLOCK_END

; THUMBNAIL_BLOCK_START
;
; thumbnail begin 48x48 868
; iVBORw0KGgo…
; thumbnail end
; THUMBNAIL_BLOCK_END

; external perimeters extrusion width = 0.42mm
; …
; EXECUTABLE_BLOCK_START
EXCLUDE_OBJECT_DEFINE NAME=支架 CENTER=135.20,141.71 POLYGON=…
;TYPE:Custom
PRINT_START
DEFECT_DETECTION_START
…
G90
G21
M83 ; use relative distances for extrusion
G92 E0
T0
;LAYER_CHANGE
;Z:0.25
;HEIGHT:0.25
;BEFORE_LAYER_CHANGE
;0.25
G92 E0
TIMELAPSE_TAKE_FRAME
;AFTER_LAYER_CHANGE
;0.25
SET_PRINT_STATS_INFO TOTAL_LAYER=1155 CURRENT_LAYER=1
;TYPE:Skirt
;WIDTH:0.50
G1 X110.302 Y110.884 F6000
G1 X115.442 Y110.129 E0.05124 F900
…
EXCLUDE_OBJECT_START NAME=支架
;TYPE:Outer wall
;WIDTH:0.42
G1 X111.229 Y111.539 F12000
G1 X112.844 Y110.053 E0.00689 F300
…
EXCLUDE_OBJECT_END NAME=支架
…
PRINT_END
TIMELAPSE_STOP
; EXECUTABLE_BLOCK_END

; filament used [mm] = 13792.40, 0, 0, 0
; total filament used [g] = 41.13
; total layers count = 1155
; estimated printing time (normal mode) = 6h 25m 39s
; CONFIG_BLOCK_START
; layer_height = 0.25
; …
; CONFIG_BLOCK_END
```

## 附录 B（资料性）与固件方言的关系

目标固件家族（`gcode_flavor`）只影响少量差异点，其余输出一致：

| 差异点 | 触发条件 | 影响 |
|---|---|---|
| **U1 现状** | 基准机型 | `gcode_flavor = klipper`（预设继承链 `fdm_U1`）；起始 / 结束 G-code 为 `PRINT_START` / `PRINT_END` 宏族，每层 G-code 注入 `TIMELAPSE_TAKE_FRAME` 与 `SET_PRINT_STATS_INFO`（6.2） |
| 回抽形式 | "使用固件回抽"开启 | `G10/G11` 替代 `G1 E±` |
| 圆弧拟合 | `enable_arc_fitting`（默认关） | 曲线段输出 `G2/G3`；Klipper 上建议关闭（固件会重新拆分为线段） |
| 对象取消指令 | 方言为 Klipper / Marlin / RRF | EXCLUDE_OBJECT 系 vs M486 系（6.4） |
| 机器参数指令 | 预设注入（非核心） | `M201/M204/M205`（加速度 / jerk）、`M900/M572`（压力提前）、`M593`（输入整形）等按方言写入起始 G-code |
| 自动补热 | 方言为 Klipper 时不自动补 | 热床 / 喷头预热完全交给起始 G-code |

方言相关指令由机型预设决定，本规范不背书其全集；消费者以目标固件文档为准（参考文献）。

## 附录 C（资料性）源码索引

本规范条款与 fork 源码（仓库 iesteem/OrcaSlicer）的对应关系：

| 条款 | 源码定位 |
|---|---|
| 文件布局、头部 / 尾部块 | `src/libslic3r/GCode.cpp`（`GCode::do_export` / `_do_export`） |
| 运动行生成与精度 | `src/libslic3r/GCodeWriter.cpp` + `GCodeWriter.hpp`（`GCodeFormatter`，XYZF=3 位、E=5 位） |
| 层 / 特征 / 事件标记 | `src/libslic3r/GCode.cpp`（`process_layer`、`GCode::extrude`、`ProcessLayer` 命名空间） |
| 标记字表 | `src/libslic3r/GCode/GCodeProcessor.cpp`（`Reserved_Tags_compatible`） |
| 缩略图块 | `src/libslic3r/GCode/Thumbnails.hpp` / `Thumbnails.cpp`（`export_thumbnails_to_file`） |
| 统计行与占位符替换 | `src/libslic3r/GCode/GCodeProcessor.cpp`（`process_temporary_line`）、`Print.cpp`（`PrintStatistics::*Mask`） |
| TYPE 角色枚举 | `src/libslic3r/ExtrusionEntity.cpp`（`role_to_string`） |

## 参考文献

- RepRap Wiki, *G-code*
- Marlin Firmware Documentation, *G-code Index*
- Klipper Documentation, *G-Codes*
- NIST, *RS-274NGC Interpreter — Version 3*（G-code 语言历史源流）
- Snapmaker Orca 2.4.x 源码导出路径与 U1 机型预设实测（附录 C）
