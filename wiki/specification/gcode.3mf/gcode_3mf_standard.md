# gcode.3mf 规范 v1.0（草案）

← [Wiki 首页](../../home.md)


> 规范性用语：**应 / 不应** = 要求（MUST / MUST NOT）；**宜 / 不宜** = 推荐（SHOULD）；**可** = 允许（MAY）。

## 目录

- [前言](#前言)
- [引言](#引言)
- [1 范围](#1-范围)
- [2 规范性引用文件](#2-规范性引用文件)
- [3 术语和定义](#3-术语和定义)
- [4 总体结构](#4-总体结构)
  - [4.1 包与目录层次](#41-包与目录层次)
  - [4.2 OPC 基础部件](#42-opc-基础部件)
  - [4.3 压缩、容量与命名约定](#43-压缩容量与命名约定)
- [5 模型部件](#5-模型部件)
  - [5.1 定位](#51-定位)
  - [5.2 元数据键](#52-元数据键)
- [6 盘与打印数据](#6-盘与打印数据)
  - [6.1 盘的标识与盘号分配](#61-盘的标识与盘号分配)
  - [6.2 盘索引：Metadata/model_settings.config](#62-盘索引metadatamodel_settingsconfig)
  - [6.3 G-code 关系声明：Metadata/_rels/model_settings.config.rels](#63-g-code-关系声明metadata_relsmodel_settingsconfigrels)
  - [6.4 切片结果摘要：Metadata/slice_info.config](#64-切片结果摘要metadataslice_infoconfig)
  - [6.5 G-code 部件与完整性校验](#65-g-code-部件与完整性校验)
  - [6.6 首层信息：Metadata/plate_N.json](#66-首层信息metadataplate_njson)
  - [6.7 盘级缩略图族](#67-盘级缩略图族)
- [7 工程配置与预设](#7-工程配置与预设)
  - [7.1 全量配置快照：Metadata/project_settings.config](#71-全量配置快照metadataproject_settingsconfig)
  - [7.2 内嵌预设：Metadata/*_settings_N.config](#72-内嵌预设metadata_settings_nconfig)
  - [7.3 条件性工程数据文件](#73-条件性工程数据文件)
  - [7.4 嵌入资源目录：Auxiliaries/](#74-嵌入资源目录auxiliaries)
- [8 一致性要求](#8-一致性要求)
  - [8.1 生产者要求](#81-生产者要求)
  - [8.2 消费者要求](#82-消费者要求)
  - [8.3 校验模型](#83-校验模型)
  - [8.4 版本与兼容](#84-版本与兼容)
- [附录 A（资料性）与 3MF Core / Toolpath 扩展的对照](#附录-a资料性与-3mf-core--toolpath-扩展的对照)
- [附录 B（资料性）背景：为什么是 .gcode.3mf](#附录-b资料性背景为什么是-gcode3mf)
- [附录 C（资料性）示例文件剖析](#附录-c资料性示例文件剖析)
  - [C.1 单盘包（导出当前盘）](#c1-单盘包导出当前盘)
  - [C.2 G-code 文件自描述结构](#c2-g-code-文件自描述结构)
  - [C.3 实测备注（2.4.x 真实导出包）](#c3-实测备注24x-真实导出包)
- [附录 D（规范性）字段字典](#附录-d规范性字段字典)
- [参考文献](#参考文献)

## 前言

本规范规定 Snapmaker Orca 切片导出的 `.gcode.3mf` 文件格式。它基于 `.3mf` 文件格式进行扩展，两者共用同一 OPC 容器家族和 `Metadata/` 约定：工程 `.3mf` 保存"怎么切"，`.gcode.3mf` 额外保存"切出来的结果"。两者的共享约定（配置取值形态、路径与关系规则）以[3mf 工程文件规范](../3mf/3mf_standard.md)第 6 章为准，冲突时以各自文件的用途为准。


## 引言

切片完成后，打印任务需要一个自足的文件同时携带：给机器执行的 G-code、给人 / APP 看的预览与摘要（耗时、重量、耗材用量）、以及完整参数快照。裸 `.gcode` 无法承载多盘任务，也没有结构化校验入口。`.gcode.3mf` 以 3MF 容器为基础，将上述内容打包为一个文件、一份拷贝、一次传输，并原生支持多盘。

包内各部分的职责一句话：`Metadata/model_settings.config` 回答"有哪些盘"，`Metadata/slice_info.config` 回答"打得怎么样"，`Metadata/plate_N.gcode`（配 `.md5`）是唯一执行来源，`Metadata/project_settings.config` 是参数快照，缩略图族负责展示。

本规范正文（第 1～8 章）规定格式与一致性要求；背景动机、与 3MF 联盟路线的对照、示例剖析、接入 FAQ 见附录 A～E。

## 1 范围

本规范规定了 `.gcode.3mf` 文件的包结构、部件定义、字段约定、校验规则与版本兼容性要求。

本规范适用于：

- **生产者**——生成 `.gcode.3mf` 的切片软件（Snapmaker Orca，向下兼容读取 Bambu Studio 同族导出）；
- **消费者**——读取或执行 `.gcode.3mf` 的打印机固件、上位机、嵌入式设备、APP 及第三方工具。

本规范不规定：G-code 指令集与方言（由机型预设决定）、网格几何与坐标变换（属工程 `.3mf` 文件，本规范不涉及）、`plate_N.json` 的坐标语义（本版未冻结，见 6.6）。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。

| 引用 | 版本 / 编号 | 用途 |
|---|---|---|
| 3MF Core Specification | 1.4.0 | 包结构、`[Content_Types].xml`、OPC 部件与关系、命名约定 |
| ISO/IEC 29500-2（OPC） | — | 包、部件、关系的通用规则 |
| W3C Extensible Markup Language (XML) | 1.0（第五版） | XML 部件编码 |
| IETF RFC 8259（JSON） | — | JSON 部件编码 |
| IETF RFC 1321（MD5） | — | G-code 完整性校验摘要算法 |
| PKWARE ZIP Application Note（APPNOTE） | 6.3.x | ZIP 容器、DEFLATE、ZIP64 |
| PNG（ISO/IEC 15948） | 第二版 | 缩略图编码与 IHDR 尺寸声明 |

## 3 术语和定义

| 术语 | 定义 |
|---|---|
| 包（package） | 本规范定义的 ZIP 归档整体，遵循 OPC 规则 |
| 部件（part） | 包内的一个条目（文件），如 `Metadata/plate_1.gcode` |
| 关系（relationship） | `_rels` 目录下 XML 文件中声明的部件间引用，由 `Id`、`Type`、`Target` 构成 |
| 生产者（producer） | 生成 `.gcode.3mf` 的软件 |
| 消费者（consumer） | 读取或执行 `.gcode.3mf` 的软件或设备 |
| 盘（plate） | 切片与打印的任务单位；每盘对应一份独立的 G-code 及其伴随文件 |
| 盘号（plate index） | 盘在工程中的原始编号 N，从 1 起；用于 `plate_N` 系列命名与索引字段 |
| 内嵌预设（embedded preset） | 随包携带的打印机 / 工艺 / 耗材预设差异文件（`*_settings_N.config`） |
| 可打印盘 | `gcode_file` 非空且对应 ZIP 条目（含 `.md5`）实际存在、校验通过的盘 |
| OPC Target 前导 `/` | 表示包根绝对路径；无前导为相对关系所属部件目录的路径 |

## 4 总体结构

### 4.1 包与目录层次

`.gcode.3mf` 是启用 ZIP64 的 ZIP 归档（OPC 包）。包内路径一律使用正斜杠、区分大小写。目录层次如下：

```text
xxx.gcode.3mf                              ← ZIP 归档（OPC 包，启用 ZIP64）
├── [Content_Types].xml                    ← OPC 内容类型声明（必选）
├── _rels/
│   └── .rels                              ← 包级关系：主模型 + 封面缩略图（必选）
├── 3D/
│   └── 3dmodel.model                      ← 3MF 主模型，元数据壳（必选）
├── Auxiliaries/                           ← 嵌入资源目录（可选）
└── Metadata/                              ← 核心目录（必选）
    ├── model_settings.config              ← 盘索引（必选）
    ├── _rels/model_settings.config.rels   ← G-code 关系声明（有 G-code 时必选）
    ├── slice_info.config                  ← 切片结果摘要（必选）
    ├── plate_N.gcode / .gcode.md5         ← 执行数据与校验（每可打印盘一份）
    ├── plate_N.json                       ← 首层信息（每可打印盘一份）
    ├── plate_N.png 等缩略图族              ← 可选
    ├── project_settings.config            ← 全量配置快照（必选）
    ├── process_settings_N.config          ← 内嵌工艺预设（条件出现）
    ├── filament_settings_N.config         ← 内嵌耗材预设（条件出现）
    ├── machine_settings_N.config          ← 内嵌打印机预设（条件出现）
    └── 条件性工程数据文件                  ← 见 7.3
```

### 4.2 OPC 基础部件

**`[Content_Types].xml`**（XML，必选）：固定声明 4 种扩展名，所有导出一致：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
 <Default Extension="png" ContentType="image/png"/>
 <Default Extension="gcode" ContentType="text/x.gcode"/>
</Types>
```

生产者不应扩充此清单；消费者不应因已知配置文件（`.config`、`.json`、`.txt`）未在清单中声明而拒绝解析——按各章规定的实际内容格式解析。

**`_rels/.rels`**（XML，必选）：声明主模型关系与封面缩略图关系（缩略图、中图、小图可各一条）。

```xml
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/3D/3dmodel.model" Id="rel-1"
   Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
 <Relationship Target="/Metadata/plate_1.png" Id="rel-4"
   Type="http://schemas.bambulab.com/package/2021/cover-thumbnail-middle"/>
</Relationships>
```

约定：

- 关系的 `Id` 仅要求在所属关系文件内唯一，不应作为业务标识使用；消费者按 `Type` + `Target` 匹配。
- `Type` 的 URI 是标识字符串，不联网解析。生产者新导出使用 `schemas.snapmaker.com/package/2026/...`，历史包使用 `schemas.bambulab.com/package/2021/...`；消费者对两种前缀应按**后缀匹配**兼容接受（如 `.../gcode`、`.../cover-thumbnail-middle`）。
- 包级封面缩略图只用于预览，不参与选盘（执行目标的确定见第 6 章）。

### 4.3 压缩、容量与命名约定

- 归档为标准 ZIP 并默认启用 ZIP64：文本 / XML / JSON / G-code 条目使用 DEFLATE 压缩；PNG 等已压缩内容以 STORE 方式写入。
- 命名模板中的 `N` 一律为**盘号**（见 6.1）；`*_settings_N.config` 中的 `N` 为同类内嵌预设的编号（从 1 起、按类型各自递增），**不是盘号**。
- 条件性文件（7.2、7.3）仅在对应功能被使用且数据非空时写出。

## 5 模型部件

### 5.1 定位

`3D/3dmodel.model` 为 3MF 主模型部件，使包在 3MF 生态（Windows 3D 查看器等通用工具）中可被识别。`.gcode.3mf` 以 `SkipModel` 策略导出：`<resources>` 与 `<build>` 应为空，不含任何几何。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xml:lang="en-US"
       xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
       xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06"
       requiredextensions="p">
 <metadata name="Application">Snapmaker_Orca-2.4.1</metadata>
 <metadata name="Snapmaker_Orca:3mfVersion">1</metadata>
 <resources>
 </resources>
 <build/>
</model>
```

### 5.2 元数据键

| 键 | 出现 | 说明 |
|---|---|---|
| `Application` | 必选 | 生成器标识，如 `Snapmaker_Orca-2.4.1`、`BambuStudio-2.3.5`，用于来源追溯 |
| `Snapmaker_Orca:3mfVersion` | 必选 | 工程格式版本，当前写 `1`。消费者应同时兼容历史键 `BambuStudio:3mfVersion`、`bamboo_slicer:Version3mf`。该值是工程格式标记，**不是**固件执行协议版本 |
| `Title` / `Designer` / `Description` / `License` / `Copyright` | 可选 | 模型级元数据，可为空 |
| `Thumbnail_Middle` / `Thumbnail_Small` | 可选 | 指向 `Metadata/plate_1.png` 等的包内路径 |

从 MakerWorld 等平台导入的工程可附带 `DesignModelId`、`DesignProfileId`、`ProfileTitle` 等平台元数据，消费者按存在性读取、未知则忽略。

消费者不应尝试从此部件恢复网格几何；执行所需内容全部位于 `Metadata/`。

## 6 盘与打印数据

### 6.1 盘的标识与盘号分配

- 盘号 N 为工程中的**原始盘号，从 1 起**，用于 `plate_N` 系列文件命名、`plater_id` 与 `index` 字段。
- 只导出第 N 盘时包内可能没有 `plate_1`：盘号可稀疏，消费者不应假设 `plate_1` 存在，不应重新编号。
- 未切片或切片失败的盘不产出 `plate_N.gcode` 及伴随文件；`model_settings.config` 中仍可列出该盘（见 6.2）。
- 多盘包应由用户显式选盘；单盘包可自动选中唯一可打印盘，但应**保留其原始盘号 N**（只导出第 3 盘时执行的就是 `plate_3.gcode`，不得转为第 1 盘）。

### 6.2 盘索引：`Metadata/model_settings.config`

XML，必选。根节点 `<config>`，每盘一个 `<plate>` 节，字段以 `<metadata key="..." value="..."/>` 写出：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<config>
  <plate>
    <metadata key="plater_id" value="1"/>
    <metadata key="plater_name" value="PLA灰"/>
    <metadata key="locked" value="true"/>
    <metadata key="filament_map_mode" value="Auto For Flush"/>
    <metadata key="filament_maps" value="1 1 1 1"/>
    <metadata key="gcode_file" value="Metadata/plate_1.gcode"/>
    <metadata key="thumbnail_file" value="Metadata/plate_1.png"/>
    <metadata key="top_file" value="Metadata/top_1.png"/>
    <metadata key="pick_file" value="Metadata/pick_1.png"/>
    <metadata key="pattern_bbox_file" value="Metadata/plate_1.json"/>
  </plate>
  <!-- 每盘一个 <plate>，plater_id 递增 -->
</config>
```

字段约定：

| key | 含义 | 约定 |
|---|---|---|
| `plater_id` | 原始盘号 N（1 起） | 与 `slice_info.config` 的 `index`（6.4）为同一 N |
| `plater_name` | 盘名 | 仅显示用，可为空、可非 ASCII |
| `locked` | 编辑器盘锁定状态 | 展示用，不是设备权限锁 |
| `filament_maps` | 耗材映射 | **不应作为真实物理喷头 / 料槽映射使用**（当前导出固定写全 1，见附录 C.3） |
| `gcode_file` | 本盘 G-code 的包内路径 | ★ 核心指针；未切片的盘可为空 |
| `thumbnail_file` / `thumbnail_no_light_file` / `top_file` / `pick_file` | 各预览资源路径 | 可选，按实际存在性读取 |
| `pattern_bbox_file` | 指向 `plate_N.json` | 增强功能用（6.6） |

可打印性判定：`<plate>` 节的出现**不构成**可打印证明；可打印盘须同时满足 `gcode_file` 非空、ZIP 条目实际存在（含 `.md5`）、校验通过（8.3）。

`.gcode.3mf` 中本文件仅含 `<plate>` 节；工程 `.3mf` 中额外的 `<object>` / `<part>` / `<assemble>` 节在本导出策略下不出现。

### 6.3 G-code 关系声明：`Metadata/_rels/model_settings.config.rels`

XML，有 G-code 时必选。按 OPC 惯例，部件自身的关系统一放在该部件目录的 `_rels/` 子目录下。每份 G-code 一条：

```xml
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/Metadata/plate_1.gcode" Id="rel-1" Type="http://schemas.bambulab.com/package/2021/gcode"/>
 <Relationship Target="/Metadata/plate_2.gcode" Id="rel-2" Type="http://schemas.bambulab.com/package/2021/gcode"/>
</Relationships>
```

消费者定位 G-code **宜优先遍历本关系文件**（按 `Type` 后缀 `gcode` 匹配），不应依赖文件名猜测。关系本身不携带盘号、机型或 MD5 信息，最终以 `model_settings.config` 的指针与 ZIP 实际条目为准。

### 6.4 切片结果摘要：`Metadata/slice_info.config`

XML，必选。根 `<config>`，含一个 `<header>` 与每个**切片有效**盘一个 `<plate>`（只列有效盘，列出的范围与 `model_settings.config` 不同）：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<config>
  <header>
    <header_item key="X-BBL-Client-Type" value="slicer"/>
    <header_item key="X-BBL-Client-Version" value=""/>
  </header>
  <plate>
    <metadata key="index" value="1"/>
    <metadata key="printer_model_id" value="SM_U1"/>
    <metadata key="nozzle_diameters" value="0.4,0.4,0.4,0.4"/>
    <metadata key="prediction" value="23139"/>
    <metadata key="weight" value="171.19"/>
    <metadata key="outside" value="false"/>
    <metadata key="support_used" value="true"/>
    <object identify_id="1724" name="青衣三节棍 v85_4" skipped="false"/>
    <filament tray_info_idx="GFSL991" type="PLA" color="#505050" used_m="57.40" used_g="171.19"/>
    <warning msg="bed_temperature_too_high_than_filament" level="1" error_code="1000C001"/>
  </plate>
</config>
```

| 元素 / 字段 | 含义 | 约定 |
|---|---|---|
| `<plate>@index` | 原始盘号 N | 与 `plater_id` 同一 N；四方一致性见 8.3 |
| `printer_model_id` | 机型 ID（如 `SM_U1`） | 与 `project_settings.config` 的 `printer_model`（如 `Snapmaker U1`）是两套命名，表示同一机型 |
| `prediction` / `weight` | 预计耗时（秒）/ 耗材重量（克） | 估计值；缺失或为空时显示"未知"，不应按 0 处理 |
| `outside` | 路径越界标记 | 为 `true` 时消费者宜阻止启动 |
| `<object>@identify_id` | 对象实例标识 | 不透明标识，不应按数组下标解释 |
| `<filament>@id` | 逻辑耗材统计索引（从 1 起） | **不是物理喷头号**；列表可稀疏 |
| `<filament>@used_m` / `used_g` | 逐耗材用量（米 / 克） | 固定两位小数 |
| `<warning>@level` | 0 提示 / 1 警告 / 2 错误 | `msg` 是枚举串，不是本地化文案；`level=2` 时消费者宜阻止启动 |

`<header>` 键存在 `X-SM-Client-*` 与 `X-BBL-Client-*` 两代写法，版本值可为空；消费者对两种前缀均应识别。

### 6.5 G-code 部件与完整性校验

**`plate_N.gcode`**（纯文本，每可打印盘一份）：由源 G-code 文件以二进制方式**原样**压入 ZIP，封装阶段不应重写任何命令。文件自描述，首尾带结构化注释块（完整示例见附录 C.2）：

- 头部 `HEADER_BLOCK`：生成器与时间、总层数、逐耗材密度 / 丝径、最大 Z 高度；
- 头部 `THUMBNAIL_BLOCK`：base64 PNG 内嵌缩略图；
- 尾部 `CONFIG_BLOCK`：完整打印参数的 `; key = value` 文本快照。

执行内容以文本 G-code 为准。**容器解析通过不等于机型可执行全部指令**——能力由机型预设与 G-code 方言决定。校验或执行前，任何人（生产者封装、消费者解包）**不应**做换行符转换、字符集转换、去注释等字节改写，否则 MD5 校验（下条）失效。

**`plate_N.gcode.md5`**（32 字节 ASCII，与同盘 G-code 一一对应）：

| 项 | 定义 |
|---|---|
| 摘要输入 | `plate_N.gcode` **解压后的完整原始字节**（不是压缩流，不是整个包） |
| 算法 / 编码 | MD5（RFC 1321），16 字节摘要写为 **32 个大写十六进制字符**（`%02X`） |
| 文件长度 | 恰好 32，无换行、BOM、文件名或 NUL |
| 失败处理 | 缺失、非法或与计算值不符时，消费者应在**执行任何指令前**拒绝启动 |

注意：通用 `md5sum` 输出带文件名与换行，与本格式不同，校验代码不应整行比对。MD5 与 ZIP 自带 CRC32 只验证传输完整性，**不是防篡改签名**（见 8.3）。

### 6.6 首层信息：`Metadata/plate_N.json`

JSON（单行），每可打印盘一份。记录整盘与逐对象首层包围盒、床型、首层挤出机等，供打印机端首层定位、图案标定与图形化提示：

```json
{
  "bbox_all": [88.26, 94.32, 177.36, 177.68],
  "bbox_objects": [
    { "id": 2853, "name": "青衣三节棍 v85_4",
      "bbox": [136.31, 142.18, 177.12, 177.18],
      "area": 477.57, "layer_height": 0.25 }
  ],
  "bed_type": "textured_plate",
  "filament_colors": [],
  "filament_ids": [],
  "first_extruder": 0,
  "is_seq_print": false,
  "nozzle_diameter": 0.4,
  "version": 2
}
```

约定：

- `bbox_all` 为 `[minX, minY, maxX, maxY]`；`bbox_objects` 逐对象同构。
- `id` 与 `slice_info.config` 的 `identify_id` 属**不同标识域**，不应混用。
- `filament_colors` 等字段可为空，展示侧应容忍。
- 本版未冻结该文件的坐标约定与 `version` 演进规则；将其用于增强功能（首层检测等）前，须由生产者与消费端另行冻结接口。

### 6.7 盘级缩略图族

| 文件 | 内容 | 约定 |
|---|---|---|
| `plate_N.png` | 512×512 带光照正交渲染 | 正常生成时的尺寸参考值；**实际尺寸以 PNG IHDR 为准**，不应按固定值假设 |
| `plate_N_small.png` | 128×128 降采样 | APP / 设备列表显示 |
| `plate_no_light_N.png` | 同角度无光照白模 | 备用预览 |
| `top_N.png` | 俯视图 | 打印机屏显 |
| `pick_N.png` | 俯视轮廓拾取图 | 屏显对象拾取提示 |

缩略图族均为可选资源：缺失或损坏时降级为默认图，不影响执行。包级封面缩略图位于 `Auxiliaries/.thumbnails/`（7.4），与盘级缩略图位置不同，不应混淆。

## 7 工程配置与预设

### 7.1 全量配置快照：`Metadata/project_settings.config`

JSON，必选。注意：扩展名为 `.config` 而内容是 JSON；同目录的 `model_settings.config` / `slice_info.config` 是 XML——**不应凭扩展名选择解析器**。

头部元字段：`version`（切片器版本）、`name`（固定 `project_settings`）、`from`（固定 `project`）、`project_schema_version`（当前 `"1"`）。其后为切片时全部生效参数的扁平键值（实测 500～600 键，按字典序）：

```json
{
    "accel_to_decel_enable": ["1"],
    "bed_shape": "0.5x1,270.5x1,270.5x271,0.5x271",
    "layer_height": "0.25",
    "filament_type": ["PLA","PLA","PLA","PLA"],
    "printer_model": "Snapmaker U1"
}
```

**取值形态**（所有标量与数组元素均为字符串，无原生 JSON number / bool / null）：

| 形态 | 写法示例 | 约定 |
|---|---|---|
| 数值 | `"3"`、`"0.2"` | 按字段含义转数字 |
| 布尔 | `"0"` / `"1"` | 与数值同形二义，须按键名语义区分 |
| 百分比 | `"15%"` | 不与绝对值混同 |
| 数组 | `["200","220"]` | 元素仍是字符串；可空字段可含 `"nil"`（≠ 0）；**长度有语义且随机型变化**，解析不应写死长度 |
| 点 / 点列表 | `"10,20"` / `["0x0","270x0"]` | 单点逗号分隔；点列表每项以 `x` 分隔 |
| 枚举 / G-code 片段 | `"monotonic"` | 按原样字符串处理 |
| 空字符串 / 空数组 | `""`、`[]` | 与 `"nil"` 是两种"空" |
| 元素内嵌换行 | `["0,0", "\n0.2,0.4444"]` | 解析前先 trim |

用途：参数回读、复切、问题排查。执行不依赖本文件：固件**不应**据此重新切片或改写 G-code（见 8.2）。

### 7.2 内嵌预设：`Metadata/*_settings_N.config`

JSON，条件出现：仅当 3mf 内对官方预设做了修改并保存为项目预设时产出。N 从 1 起、按类型各自递增（与盘号无关）。

| 文件 | 预设类型 | 内容 |
|---|---|---|
| `machine_settings_N.config` | 打印机预设 | 机型、喷嘴、打印区域、起止 G-code 模板等 |
| `process_settings_N.config` | 工艺预设 | 层高 / 壁厚 / 填充 / 速度 / 支撑等 |
| `filament_settings_N.config` | 耗材预设 | 温度 / 回抽 / 冷却 / 流量比等 |

头部含 `name`（预设名）、`version`、`from`（固定 `project`）、`is_custom_defined`；正文结构与 7.1 一致，但**只含相对父预设的差异项**，不保证完整参数集。恢复工程时按各自用途读取，不应把包内最后一个配置文件当作最终配置。

### 7.3 条件性工程数据文件

以下文件仅在对应功能使用且数据非空时写出（均在 `Metadata/` 下）：

| 文件 | 格式 | 出现条件与结构 |
|---|---|---|
| `layer_heights_profile.txt` | 文本 | 启用可变层高时。首行 `layer_heights_profile_format_version=2`；其后每对象一行 `object_id=N\|z1;h1;z2;h2...`（z/h 单位 mm）。v2 的 N 是真实 3MF 对象 id；无版本头的 legacy 文件按对象顺序解释 |
| `layer_config_ranges.xml` | XML | 按 Z 区间设置层高时。`<objects><object id><range min_z max_z><option opt_key>`。此处 `object@id` 是**对象顺序号**（从 1 起），与上一条含义不同 |
| `brim_ear_points.txt` | 文本 | 使用鼠耳裙边时。首行 `brim_points_format_version=0`；每对象一行 `object_id=N\|x y z radius ...`（对象顺序号） |
| `custom_gcode_per_layer.xml` | XML | 定义逐层事件（0 换色 / 1 暂停 / 2 换工具 / 3 模板 / 4 自定义）时；按**原盘号**记录 `top_z/type/extruder/color/extra/gcode` |
| `cut_information.xml` | XML | 执行过切割操作时；切割 ID、校验值、连接件数与体积索引 |

各文件 `object_id` 的含义不相同（真实对象 id vs 对象顺序号），读取时以各文件自身的格式头为准。

### 7.4 嵌入资源目录：`Auxiliaries/`

位于包根，与 `Metadata/` 平级。可选。典型内容：

```text
Auxiliaries/
├── .thumbnails/          ← 包级封面（thumbnail_3mf.png / thumbnail_middle.png / thumbnail_small.png）
├── Model Pictures/       ← 工程内嵌模型展示图（可选）
└── Profile Pictures/     ← 作者 / 预设图片（可选）
```

内容与子目录名不固定（图片、字体等均可进入）。消费者对未知内容应"允许存在、按需取用、未知则忽略"。仅缺封面图不影响几何与配置的读取。

## 8 一致性要求

### 8.1 生产者要求

生产者生成的包**应**：

1. 遵循第 4 章的目录层次、压缩方式与 ZIP64 约定；
2. 写出 4.2 规定的 `[Content_Types].xml`（不扩充）与 `_rels/.rels`；
3. 以 `SkipModel` 策略产出空 `<resources>`/`<build>` 的主模型，并写入 `Application` 与 `3mfVersion` 元数据；
4. 按**原始盘号**命名 `plate_N` 系列文件；未切片的盘不产出执行文件，但在盘索引中如实列出；
5. 将源 G-code 原样压入，不做任何字节改写；同时写出正确的 `.gcode.md5`（大写、32 字符、无换行）；
6. 保证四方一致性（8.3）：`plater_id` ↔ `index` ↔ `gcode_file` ↔ `.rels` Target ↔ ZIP 条目实际存在；
7. `project_settings.config` 以字符串形态写出全部生效参数。

### 8.2 消费者要求

消费者**应**：

1. 按普通 ZIP 解包，先读 `[Content_Types].xml` 与 `_rels/.rels`，不因未声明扩展名拒绝已知文件；
2. 以 `model_settings.config` 枚举盘，走 `.rels` 定位 G-code（不猜文件名）；
3. 执行前完成 8.3 的校验；校验失败在执行任何指令前拒绝启动；
4. 对 `Type` URI 的两代前缀（`schemas.bambulab.com/package/2021` 与 `schemas.snapmaker.com/package/2026`）按后缀兼容接受；
5. 对缺失的可选资源（缩略图、预设、条件性文件）保持容忍，以关系文件与盘索引为准，不假定固定文件集；
6. **不应**依据 `project_settings.config` 重新切片或改写 G-code；
7. **不应**将 `filament_maps`、`<filament>@id`、`plate_N.json` 的 `id` 当作物理喷头 / 料槽编号使用；
8. 对超出本规范定义的字段与资源，未知则忽略。

消费者**宜**：`outside=true` 或 `warning level=2` 时阻止启动；`prediction`/`weight` 缺失时显示"未知"而非 0。

### 8.3 校验模型

完整性校验分四层，逐层递进：

| 层级 | 机制 | 能发现 | 局限 |
|---|---|---|---|
| ZIP 传输层 | 每条目自带 CRC32，解压时自动校验 | 传输 / 存储损坏 | 重打包即可通过 |
| 内容层 | `plate_N.gcode.md5` 对解压后完整字节求 MD5 | 导出后 G-code 被意外改动 | G-code 与 md5 被一同改写时失效 |
| 结构层 | 四方交叉验证：`plater_id` ↔ `index` ↔ `gcode_file` ↔ `.rels` Target + ZIP 条目存在（含 `.md5`） | 盘号错配、文件缺失、包结构错乱 | 须显式核对，不应按 XML 节点顺序配对 |
| 语义层（可选） | 解析 G-code 头部 `HEADER_BLOCK` | 展示信息与合理性检查 | 属解析，不属校验 |

四方不一致时消费者应拒绝该盘，不应按节点顺序纠正。MD5 / CRC32 均非数字签名：防篡改须依赖包外机制（数字签名 / 白名单），包内不提供。

### 8.4 版本与兼容

| 情况 | 读取约定 |
|---|---|
| 模型版本键 | 当前写 `Snapmaker_Orca:3mfVersion`；应兼容 `BambuStudio:3mfVersion`、`bamboo_slicer:Version3mf` |
| 模型版本与配置版本 | 两者分开读取：模型版本当前为 1；`project_schema_version` 当前为 `"1"` |
| legacy 层高文件 | 无版本头的 `layer_heights_profile.txt` 按对象顺序解释，不套用 v2 对象 id |
| `Content_Types` 不完整 | 2.4.x 未覆盖全部配置文件；已知文件按实际内容格式读取 |
| 关系 `Type` 两代前缀 | 按后缀匹配兼容接受 |
| 未知的必需扩展 | 影响模型解释时，读取器应报告不支持 |

## 附录 A（资料性）与 3MF Core / Toolpath 扩展的对照

`.gcode.3mf` 与 3MF 联盟 Toolpath Extension 解决同一问题——"切片完了，怎么把打印任务交给机器"——但交换产物的深度不同：

| 维度 | gcode.3mf（本规范） | 3MF Toolpath 扩展（1.0.0 RC，2026-09） |
|---|---|---|
| 核心数据 | G-code 文本（最终代码） | 每层一个 XML（结构化数据） |
| 最终指令由谁生成 | 切片器（切完即定） | 机器端（装载后再编译） |
| 工艺参数 | 写在 G-code 行内 + CONFIG_BLOCK 快照 | profile 集中声明 + 0–1 比例因子调制 |
| 防错手段 | MD5 + 四方交叉验证（字节层） | 装载期校验能力与参数包络（语义层） |
| FFF 完整度 | 完整（即 G-code 本身） | 残缺（温度 / 风扇 / 回抽无标准槽位） |
| 状态 | 量产使用多年 | RC，主攻激光金属打印（LPBF），无消费级落地 |

`.gcode.3mf` 双扩展名恰合 3MF Core 1.4.0 §2.2.1 厂商约定（`.vendor.3mf`）的模式。Toolpath RC 的"参数包络提前声明"与"厂商元数据安全禁令"设计已被记为阶段二参考。逐机制对照与互转可行性分析见 [docs/06](../../../docs/06-对账-gcode.3mf与3MF-Toolpath扩展.md)。

## 附录 B（资料性）背景：为什么是 .gcode.3mf

1. **单一文件、一次传输**：机器 / U 盘 / APP 需要一个自足文件同时携带 G-code、缩略图、摘要与完整参数；裸 `.gcode` 无法承载多盘、无结构化校验。
2. **多盘任务的自然容器**：多盘打印需要把 N 份 G-code 连同各自预览与摘要统一打包、逐盘独立可取；OPC 包 + 关系文件天然满足"一个包、多个部件、按关系索引"。
3. **复用 3MF / OPC 生态**：通用 3MF 工具能识别包骨架与缩略图；自家读取端通过 `gcode` 内容类型与自有 Relationship 类型定位打印数据——扩展规范而不破坏规范。
4. **可回读、可复切**：保留 `project_settings.config` 与切片摘要，拖回软件即可预览并恢复参数重新切片。
5. **完整性校验**：每盘 MD5 随包携带，传输后可验证 G-code 未损坏。

一句话：`.gcode.3mf` = 3MF 容器 + BBS/Snapmaker 扩展 + 以 G-code 为核心的切片产物集。

## 附录 C（资料性）示例文件剖析

### C.1 单盘包（导出当前盘）

菜单"导出当前盘"只含当前盘的执行文件；`model_settings.config` 仍列出工程全部盘，但仅本盘 `gcode_file` 非空：

```text
Metadata/
├── plate_1.gcode / plate_1.gcode.md5      ← 唯一执行文件 + 校验
├── plate_1.png / plate_1_small.png / plate_no_light_1.png / top_1.png / pick_1.png
├── plate_1.json
├── model_settings.config / slice_info.config / project_settings.config
```

### C.2 G-code 文件自描述结构

```text
; HEADER_BLOCK_START
; generated by Snapmaker Orca 2.4.0 on 2026-10-28 at 10:38:35
; total layer number: 1155
; filament_density: 1.24,1.24,...                          ← 逐耗材
; filament_diameter: 1.75,1.75,...
; max_z_height: 231.05
; HEADER_BLOCK_END
; THUMBNAIL_BLOCK_START
; thumbnail begin 48x48 868
; iVBORw0KGgo...                                           ← base64 PNG
; THUMBNAIL_BLOCK_END
<G-code 指令主体>
; CONFIG_BLOCK_START                                       ← 尾部 "; key = value" 参数快照
; layer_height = 0.25
; CONFIG_BLOCK_END
```

### C.3 实测备注（2.4.x 真实导出包）

- 14 盘样例：`model_settings.config` 列出全部 14 盘；`filament_settings_1~4` 是 4 套耗材预设（编号与盘数无关）；`filament_maps` 全部写 `1 1 1 ...`，证实 6.2 "不可当物理映射"的约定。
- 盘号稀疏实测：只导出第 3 盘时包内仅有 `plate_3.*` 系列，无 `plate_1`。
- MD5 实测：`plate_1.gcode.md5` 内容 `24ECD16D2325B63E76B128F2DB707BC9`（32 字符大写、无换行），与解压后字节计算值一致。
- `slice_info.config` 的 `prediction` 与 G-code 头部 `estimated printing time` 一致、`weight` 与 `filament used [g]` 一致，可交叉核对。

## 附录 D（规范性）字段字典

`project_settings.config` 及内嵌预设的完整键值以配置字段字典为准（699 个注册字段，含中文说明、预设类别与 JSON 版本），随本规范同源维护；切片参数的逐键讲解见 [设置参数文档](../../settings/printer/printer_overview.md)（printer / filament / process 三目录）。字典未收录的键按 7.1 的形态约定处理。

## 参考文献

- 3MF Consortium, *3MF Core Specification* 1.4.0（2025-02-06）
- 3MF Consortium, *3MF Toolpath Extension — Specification & Reference Guide* 1.0.0 RC（2026-09-03）
- GB/T 1.1—2020《标准化工作导则 第 1 部分：标准化文件的结构和起草规则》（体例参考）
