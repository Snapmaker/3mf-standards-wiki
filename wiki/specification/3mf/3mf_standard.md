# 3mf 工程文件规范 v1.0（草案）

← [Wiki 首页](../../home.md)


> 规范性用语：**应 / 不应** = 要求（MUST / MUST NOT）；**宜 / 不宜** = 推荐（SHOULD）；**可** = 允许（MAY）。

## 前言

本规范规定 Snapmaker Orca 保存与导出的工程 `.3mf` 文件格式。工程文件回答"**怎么切**"：一个文件恢复整个切片工程——网格几何与摆放、对象和盘的业务属性、全量参数快照与预设差异。它与回答"切出来的结果"的 [gcode.3mf 规范](../gcode.3mf/gcode_3mf_standard.md) 构成姊妹篇：两者共用同一 OPC 容器家族和 `Metadata/` 约定，工程 `.3mf` 保存工程状态，`.gcode.3mf` 额外携带执行产物。两者的共享约定（配置取值形态、路径与关系规则）以**本规范第 6 章**为准。

工程 `.3mf` 以 3MF Consortium《3MF Core Specification》为基础：几何层（`3D/`）遵循 Core 的模型部件规范，直接保存形态叠加 Production Extension；配置层（`Metadata/`）是 BBS 管线（Bambu Studio 系）沿用的厂商自有层，属 Core 允许的厂商扩展模式（对照见附录 A）。

## 引言

切片工程的可恢复性要求一个自足文件同时携带：网格几何（顶点与三角形）、布局（对象实例在打印板上的摆放）、业务属性（对象名、耗材槽、盘布局）、参数全量快照与参数覆盖关系、以及预设来源差异。散件（STL + ini）无法承载这些结构的关联，通用 3MF 又不含任何打印配置层。

包内各部分的职责一句话：`3D/3dmodel.model` 管"有哪些对象、怎么摆"，`3D/Objects/*.model` 管"网格本体"（外拆时），`Metadata/model_settings.config` 管"对象/零件/盘的业务属性与参数覆盖"，`Metadata/project_settings.config` 管"全局参数快照"，内嵌预设管"参数从哪个预设改出来的"，条件性文件管"变层高等专项功能数据"。

本规范正文（第 1～8 章）规定格式与一致性要求；与官方标准的对照、保存策略、示例剖析、字段字典、与 gcode.3mf 规范的分工见附录 A～E。

## 1 范围

本规范规定了工程 `.3mf` 文件的包结构、模型部件、外拆对象文件、配置文件、参数覆盖规则、版本标识与兼容性要求。

本规范适用于：

- **生产者**——生成工程 `.3mf` 的软件（Snapmaker Orca 的直接保存、通用导出与自动备份三种路径，见附录 B）；
- **消费者**——回读工程 `.3mf` 的软件（Snapmaker Orca 后续版本、按 3MF Core 读取几何的第三方工具）。

本规范不规定：切片算法与参数语义（见[设置参数文档](../../setting/printer/printer_overview.md)）、`.gcode.3mf` 执行产物（由 [gcode.3mf 规范](../gcode.3mf/gcode_3mf_standard.md) 规定）、PrusaSlicer 管线专有配置文件（`Slic3r_PE.config` 等，支持范围待裁决：Q20）、`plate_N.json` 的坐标语义（本版未冻结，见 6.5）。

## 2 规范性引用文件

下列文件中的内容通过文中的规范性引用而构成本文件必不可少的条款。

| 引用 | 版本 / 编号 | 用途 |
|---|---|---|
| 3MF Core Specification | 1.4.0 | OPC 包结构、`[Content_Types].xml`、模型部件（`model`/`resources`/`build`）规范、厂商扩展模式（§2.2.1） |
| 3MF Production Extension | — | 对象 / 组件 / 构建项 UUID（`p:UUID`）、外部部件引用（`p:path`） |
| ISO/IEC 29500-2（OPC） | — | 包、部件、关系的通用规则 |
| W3C Extensible Markup Language (XML) | 1.0（第五版） | XML 部件编码 |
| IETF RFC 8259（JSON） | — | JSON 部件编码 |
| PKWARE ZIP Application Note（APPNOTE） | 6.3.x | ZIP 容器、DEFLATE、ZIP64 |
| PNG（ISO/IEC 15948） | 第二版 | 缩略图编码 |

## 3 术语和定义

| 术语 | 定义 |
|---|---|
| 包（package） | 本规范定义的 ZIP 归档整体，遵循 OPC 规则 |
| 部件（part） | 包内的一个条目（文件），如 `Metadata/project_settings.config` |
| 关系（relationship） | `_rels` 目录下 XML 文件中声明的部件间引用，由 `Id`、`Type`、`Target` 构成 |
| 生产者（producer） | 生成工程 `.3mf` 的软件 |
| 消费者（consumer） | 读取工程 `.3mf` 的软件 |
| 工程（project） | 一次切片任务的完整状态：几何、布局、参数、预设差异的集合 |
| 对象（object） | 可整体操作的模型单位（源码 `ModelObject`），对应 `3dmodel.model` 中一个 `<object>` 与 `model_settings.config` 中一个 `<object>` |
| 零件（part / volume） | 对象内部的组成件（源码 `ModelVolume`），对应 `model_settings.config` 中对象节下的一个 `<part>` |
| 实例（instance） | 对象的一次摆放，对应 `3dmodel.model` 中一条 `<item>`；业务侧在盘节中以 `<model_instance>` 登记 |
| 盘（plate） | 布局与切片的任务单位；每盘对应 `plate_N` 系列缩略图与盘节 |
| 盘号（plate index） | 盘在工程中的原始编号 N，从 1 起 |
| 外拆对象文件（split model） | 直接保存形态下，每对象拆出至 `3D/Objects/` 的独立网格部件 |
| 通用导出（generic export） | 菜单"Export Generic 3MF"产出的、剥离私有扩展的最小 Core 兼容形态 |
| 内嵌预设（embedded preset） | 随包携带的打印机 / 工艺 / 耗材预设差异文件（`*_settings_N.config`） |
| 三层覆盖 | 同一参数键可出现在 project（全局）/ object（对象）/ part（零件）三层的参数覆盖机制 |
| 字段白名单 | 允许写入 `project_settings.config` 的配置键集合（见附录 D） |
| BBS 管线 | `bbs_3mf.cpp` 实现的主读写路径，本产品 3mf 的全部读写并兼容读取 Bambu Studio 同族文件 |

## 4 总体结构

### 4.1 保存形态与目录层次

工程 `.3mf` 是启用 ZIP64 的 ZIP 归档（OPC 包）。包内路径一律使用正斜杠、区分大小写。同一工程存在三种保存形态（生成路径与策略位见附录 B），日常两种对比如下：

| | 直接保存工程 | 通用导出 |
|---|---|---|
| 用途 | 工程原样落盘、可完整恢复 | 分发给第三方软件的 Core 兼容文件 |
| 网格存储 | 外拆 `3D/Objects/<对象名>_<obj_id>.model`，每对象一文件 | 全部内嵌 `3D/3dmodel.model` |
| `3D/_rels/3dmodel.model.rels` | 有（登记外拆部件） | 无 |
| 生产扩展 + UUID | 有（`requiredextensions="p"`） | 无（不声明 `xmlns:p`） |
| 配置层 `Metadata/` | 完整保留 | **现状同样完整保留**（未因"通用"而精简，见 6.7） |

直接保存形态的目录层次：

```text
xxx.3mf                                    ← ZIP 归档（OPC 包，启用 ZIP64）
├── [Content_Types].xml                    ← OPC 内容类型声明（必选）
├── _rels/
│   └── .rels                              ← 包级关系：主模型 + 封面缩略图（必选）
├── 3D/
│   ├── 3dmodel.model                      ← 主模型：对象/组件/实例引用 + 元数据（必选）
│   ├── _rels/
│   │   └── 3dmodel.model.rels             ← 外拆网格登记（外拆时必选）
│   └── Objects/
│       └── <对象名>_<obj_id>.model        ← 外拆网格，每对象一文件（外拆时必选）
├── Auxiliaries/                           ← 嵌入资源目录（可选）
└── Metadata/                              ← 配置层（必选）
    ├── project_settings.config            ← 全量配置快照，JSON（必选）
    ├── model_settings.config              ← 对象/零件/盘索引，XML（必选）
    ├── slice_info.config                  ← 摘要位，当前空壳（必选，去留待裁决：Q16）
    ├── plate_N.png 等缩略图族              ← 按盘出现
    ├── plate_N.json                       ← 盘面布局摘要（2.4.0 起，条件出现）
    ├── *_settings_N.config                ← 内嵌预设（条件出现）
    └── 条件性工程数据文件                   ← 见 6.5
```

通用导出形态：`3D/` 下仅 `3dmodel.model`（网格内嵌、无 `Objects/`、无 `3D/_rels/`），`Metadata/` 与 Auxiliaries 层次同上。

### 4.2 OPC 基础部件

**`[Content_Types].xml`**（XML，必选）：固定声明 4 种扩展名，与 `.gcode.3mf` 包完全一致：

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

**`_rels/.rels`**（XML，必选）：声明主模型关系与封面缩略图关系。主模型关系的 `Type` 为 `http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel`，`Target` 为 `/3D/3dmodel.model`。缩略图、关系 `Id` 唯一性、`Type` URI 两代前缀（`schemas.bambulab.com/package/2021` 与 `schemas.snapmaker.com/package/2026`）等约定与 [gcode.3mf 规范](../gcode.3mf/gcode_3mf_standard.md) 4.2 一致，消费者按 `Type` 后缀匹配兼容接受。

### 4.3 压缩、容量与命名约定

- 归档为标准 ZIP 并默认启用 ZIP64：文本 / XML / JSON 条目使用 DEFLATE 压缩；PNG 等已压缩内容以 STORE 方式写入。
- 外拆网格文件名模板为 `<对象名>_<obj_id>.model`，其中 `<对象名>` 直接取用户输入的对象名拼接，**写入前未做字符清洗**——对象名含 `/`、`\`、Windows 保留字符或超长时行为未定义。规范拟将外拆文件名与对象名解耦（固定模式如 `object_<obj_id>.model`，对象名只存 `model_settings.config`）（待裁决：Q22）。
- `plate_N` 系列命名中的 `N` 一律为**盘号**（从 1 起、可稀疏，不应重新编号）；`*_settings_N.config` 中的 `N` 为同类内嵌预设编号（从 1 起、按类型各自递增），**不是盘号**。
- 条件性文件（6.4、6.5）仅在对应功能被使用且数据非空时写出。

## 5 模型部件

### 5.1 Core 基础约束（摘录）

`3D/3dmodel.model` 是 3MF 主模型部件，其格式由 3MF Core 规范的 Model 章规定。本节摘录直接影响读写的关键约束，完整规则以 Core 规范原文为准：

- 根元素为 `<model>`，核心命名空间 `http://schemas.microsoft.com/3dmanufacturing/core/2015/02`；直接保存形态叠加生产扩展命名空间（见 5.3）。
- `unit` 属性：Core 定义 micron / millimeter / centimeter / inch / foot / meter。本生产者恒写 `millimeter`；消费者**应**按 `unit` 换算，**不应**无条件假定毫米。
- 结构为 `<metadata>`* → `<resources>`（恰一个）→ `<build>`（恰一个）。`<resources>` 内为对象资源（网格或组件引用），`<build>` 内为待构建实例。
- 网格（mesh）由顶点表与三角形索引构成：任一条边**应**至多被两个三角形共享；相邻三角形朝向**应**一致（法向由顶点绕序按右手定则确定）；三角形的三个顶点索引**应**互异。
- 变换（`transform` 属性）：3×4 矩阵的 12 个数值以空格分隔、行主序写出（每列 3 行、共 4 列），缺省为单位变换。
- `<item>` 的 `printable` 属性标识实例是否参与构建。

### 5.2 对象、组件与实例

多零件对象在主模型中表示为"组件引用"：`<object id="N" type="model">` 下挂 `<components>`，每个零件（volume）一条 `<component>`；单零件对象可内嵌 mesh 或同样走组件引用。实例在 `<build>` 中逐条列出：

```xml
<model unit="millimeter" xml:lang="en-US"
       xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
       xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06"
       requiredextensions="p">
 <metadata name="Application">Snapmaker_Orca-2.4.0</metadata>
 <metadata name="Snapmaker_Orca:3mfVersion">1</metadata>
 <resources>
  <object id="1" p:UUID="00000001-61cb-4c03-9d28-80fed5dfa1dc" type="model">
   <components>
    <component p:path="/3D/Objects/立方体_1.model" objectid="2"
               transform="1 0 0 0 1 0 0 0 1 0 0 0"/>
   </components>
  </object>
  <!-- objectid="2" 的网格本体位于外拆文件；内嵌形态则直接写在 <object> 内 -->
 </resources>
 <build>
  <item objectid="1" transform="1 0 0 10 0 1 0 10 0 0 1 0" printable="1"/>
 </build>
</model>
```

约定：

- 同一对象的多个实例 = 同一 `objectid` 的多条 `<item>`，各自带变换。
- **外拆形态**下主模型不含网格本体，`<component>` 与 `<item>` 以 `p:path` 指向外拆部件（见 5.5）；**内嵌形态**（通用导出）下网格写在 `<object>` 内，无 `p:path`。
- 对象编号（`object@id`）与 `model_settings.config` 的 `<object id>` 一一对应——一边是几何，一边是属性，两套编号**不应**各自重排。

### 5.3 生产扩展（p:）

直接保存形态声明生产扩展：`xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06"` 与 `requiredextensions="p"`，并在对象、组件、构建项上写 `p:UUID`。约定：

- `p:UUID` 由内部对象编号加固定后缀**确定性合成**（如对象 UUID 后缀 `-61cb-4c03-9d28-80fed5dfa1dc`、共享网格用备用后缀），不是随机 UUID——同一工程重复保存得到相同 UUID。
- 通用导出**不声明** `xmlns:p`、不写任何 UUID（见 4.1）。
- 消费者遇到声明了自身不支持的必需扩展（`requiredextensions`）且影响模型解释时，**应**报告不支持（与 [gcode.3mf 规范](../gcode.3mf/gcode_3mf_standard.md) 8.4 原则一致）。
- `Snapmaker_Orca:3mfVersion` 元数据键**不应**停写：外拆子模型文件的格式识别依赖该键（加密拆分对象回载需要）。

### 5.4 模型级元数据

元数据以 `<metadata name="键">值</metadata>` 子元素形式写出（值在元素文本中；注意与 `model_settings.config` 的 `key`/`value` 属性形态不同，解析不应混用）：

| 键 | 出现 | 说明 |
|---|---|---|
| `Application` | 必选 | 生成器标识，如 `Snapmaker_Orca-2.4.0`。读取端以该键前缀判别 BBS 系文件（7.3） |
| `Snapmaker_Orca:3mfVersion` | 必选 | 工程格式版本，当前写 `1`。消费者应同时兼容历史键 `BambuStudio:3mfVersion`、`bamboo_slicer:Version3mf`（三键等价读取） |
| `Title` / `Origin` / `Designer` / `DesignerCover` / `Description` / `Copyright` / `License` | 可选 | 模型级信息，可为空 |
| `DesignerUserId` / `CreationDate` / `ModificationDate` | 可选 | **隐私键，恒写空串**（生产者刻意不落盘用户身份与时间信息） |
| `model_id` / `Region` | 条件 | 平台分发元数据（如 MakerWorld 导入件），按存在性读取 |
| `MakerLab` / `MakerLabVersion` | 条件 | 上游遗留键（归入废弃候选，待裁决：Q2） |

**去 Bambu 化**：重新保存时，生产者剥除所有 `BambuStudio:` / `bamboo_slicer:` 前缀的元数据键（源码 `src/libslic3r/Format/bbs_3mf.cpp`，行号锚点见 [3mf_version_management](3mf%20documents/3mf_version_management.md) §3.2）。消费者对残留的历史键按存在性读取、未知则忽略。

### 5.5 外拆对象文件与部件关系

直接保存形态下，网格本体外拆至 `3D/Objects/`：

- **文件名**：`<对象名>_<obj_id>.model`，每对象一个文件（命名安全性见 4.3，待裁决：Q22）。
- **内容**：独立的 `<model>` 根（核心命名空间），内含该对象网格的顶点与三角形；同样写 `Snapmaker_Orca:3mfVersion` 元数据键（子模型格式识别钩子）。顶点坐标以定点十进制写出，精度按 `float` 最大有效数字（保证回读无损）。
- **登记**：每个外拆部件在 `3D/_rels/3dmodel.model.rels` 中登记一条关系；主模型以 `p:path` 引用（5.2）。
- **引用定位**：消费者**应**通过关系文件 + `p:path` 定位网格，**不应**按 `Objects/` 目录文件名猜测。

`ShareMesh` 策略下重复网格共享同一外拆文件（UUID 用备用后缀区分，见 5.3）；去重不影响对象编号对应关系。

## 6 工程配置与参数覆盖

`Metadata/` 为 BBS 管线的厂商配置层，Core 规范未定义其中任何文件（对照见附录 A）。扩展名 `.config` 不代表统一格式：`project_settings.config` 是 JSON，`model_settings.config` / `slice_info.config` 是 XML——**不应凭扩展名选择解析器**。

### 6.1 对象与盘索引：`Metadata/model_settings.config`

XML，必选。根节点 `<config>`，按 object → plate → assemble 顺序组织（工程文件中各节正常出现；`.gcode.3mf` 以 SkipModel 策略导出时仅剩 plate 节）：

```text
config
├── object id="对象编号"                        ← 每对象一节
│   ├── metadata key="name"                     ← 对象名（用户可见）
│   ├── metadata key="module"                   ← 条件出现（源码支持，实测 0 次，待裁决：Q3）
│   ├── metadata key=<对象级参数覆盖>            ← project_settings 键子集，按需
│   └── part id="部件编号" subtype="零件类型"
│       ├── metadata key="name"
│       ├── metadata key="matrix"               ← 4×4 矩阵，16 值空格分隔
│       ├── metadata key="source_file" …        ← 来源 6 键（见下表）
│       ├── metadata key="merged_group_id"      ← 条件（"Assemble"合并组）
│       ├── metadata key=<部件级参数覆盖>
│       └── mesh_stat edges_fixed="…" …         ← 网格修复统计（属性 ×5）
├── plate                                       ← 每盘一节
│   ├── metadata key="plater_id" …              ← 键表见 6.1.2
│   └── model_instance                          ← 每实例一节
│       └── metadata key="object_id" / "instance_id" / "identify_id"
└── assemble                                    ← 条件出现（待裁决：Q4）
    └── assemble_item object_id=… instanceid=… transform=… offset=…
```

#### 6.1.1 对象层与零件层固定键

| 层 | 键 | 含义 | 约定 |
|---|---|---|---|
| object | `name` | 对象名 | 显示用，可为非 ASCII |
| object | `module` | 模块名 | 条件键，语义未定（待裁决：Q3） |
| object / part | 参数覆盖键 | 全局参数的对象 / 零件级覆盖 | 见 6.2 |
| part | `name` | 零件名 | 显示用 |
| part | `matrix` | 零件局部变换（4×4） | 与 `3dmodel.model` 的 3×4 `transform` 是两种矩阵形态，**不应**混用 |
| part | `source_file` / `source_object_id` / `source_volume_id` / `source_offset_x\|y\|z` | 导入来源追溯 | `source_file` 默认仅存文件名不含路径 |
| part | `merged_group_id` | 合并组标识 | "Assemble"设定、"Split to objects"消费 |
| part | `mesh_stat` | 网格修复统计（5 属性） | 诊断信息，不影响几何本体 |

#### 6.1.2 盘节键

| key | 含义 | 约定 |
|---|---|---|
| `plater_id` | 原始盘号 N（1 起） | 与缩略图等 `plate_N` 命名的 N 一致 |
| `plater_name` / `locked` | 盘名 / 编辑器锁定状态 | 展示用 |
| `curr_bed_type` / `print_sequence` / `first_layer_print_sequence` / `other_layers_print_sequence` / `other_layers_print_sequence_nums` / `spiral_mode` | 盘级打印选项 | 条件写入（触发条件逐项确认中，待裁决：Q5） |
| `filament_maps` / `filament_map_mode` | 耗材映射 | **不应作为真实物理喷头 / 料槽映射使用**（当前恒写全 `1` 与固定 `Auto For Flush`，处置待裁决：Q12） |
| `gcode_file` | 盘 G-code 的包内路径 | 仅嵌 G-code 的形态写出（工程直接保存 / 通用导出无此键） |
| `thumbnail_file` / `thumbnail_no_light_file` / `top_file` / `pick_file` / `pattern_bbox_file` | 盘级资源路径 | 按实际存在性读取 |

盘节内的 `<model_instance>` 登记该盘包含的实例：`object_id`（对象编号，与 5.2 一一对应）、`instance_id`（对象内实例序号）、`identify_id`（不透明实例标识，**不应**按数组下标解释，与 `slice_info.config` 的标识域不同）。`<assemble>` 节记录装配视图的实例变换（写入条件为装配模式初始化，实测 7 样本 + 2 对照样本均 0 次出现，待裁决：Q4）。

### 6.2 三层参数覆盖

同一参数键可出现在三层，生效值按覆盖优先级合成：

| 层 | 载体 | 语义 |
|---|---|---|
| project（全局） | `project_settings.config`（6.3） | 工程级基准值 |
| object（对象覆盖） | `model_settings.config` 对象节 | 该对象全部实例生效 |
| part（零件覆盖） | `model_settings.config` 零件节 | 仅该零件生效 |

- 现状优先级为 **part > object > project**（零件 > 对象 > 全局），该规则只存在于读取代码逻辑中，文件本身无任何声明（实测同一键在对象层与零件层并存：`wall_loops` 对象层 ×47、零件层 ×10）（待裁决：Q19 显式化）。
- 覆盖键集合 = `project_settings.config` 键的子集（实测对象层 32 种、零件层 17 种，如 `layer_height`、`wall_loops`、`extruder`、`support_*`、`ironing_*`）。
- **键空间警示**：结构键（`name`、`matrix`、`source_*` 等）与参数覆盖键共用同一 `metadata key` 命名空间，仅靠所在位置区分语义；新增配置键**不应**与既有结构键撞名（撞名清单维护见附录 D）。
- 本版不为局部配置时间戳留位（语义未明，待裁决：Q9）。

### 6.3 全量配置快照：`Metadata/project_settings.config`

JSON，必选。头部元字段：

| 字段 | 值 | 说明 |
|---|---|---|
| `version` | 软件版本（如 `"2.4.0"`） | 生成器版本，非格式版本 |
| `name` | `"project_settings"` | 固定 |
| `from` | `"project"` | 固定 |
| `project_schema_version` | `"1"` | 配置 schema 版本；2.4.0 起落盘，缺失视为 legacy（维护规则待裁决：Q6） |

其后为切片时全部生效参数的扁平键值（实测 500～600 键，按字典序）。**取值形态**（所有标量与数组元素均为字符串，无原生 JSON number / bool / null）：

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

**写入范围**：现状为全量 `FullPrintConfig` 键集落盘、无准入控制（序列化点见 `src/libslic3r/Format/bbs_3mf.cpp`），新增软件参数自动进包。本规范将允许写入的键集定义为**字段白名单**（初始集合 584 键 = 源码定义且落盘 553 + 落盘无静态定义 31，含 18 个序列化别名如 `filament_retract_*` ↔ `retract_*`），六类字段一律禁入（SLA 树脂 / CLI 动作参数 / 运行时派生状态 / GUI 废弃候选 / 预设系统内部 / 打印主机连接），新增配置键须先登记字段字典再落盘——准入流程待团队确认（待裁决：Q18，集合与分类见附录 D）。

**强制禁入项（安全）**：凭据类字段（`print_host`、`printhost_apikey`、`printhost_password`、`printhost_user`、`printhost_port`、`printhost_cafile`）**不应**随包分发——现状 `machine_settings_N.config` 结构性写入这些键（当前样本值为空，用户一旦配置即泄漏），序列化前**应**剔除（待裁决：Q11）。

预设系统痕迹字段（`different_settings_to_system`、`inherits_group`）实测偶发混入本文件，属预设系统内部字段，**不应**写入（待裁决：Q13）。

用途：参数回读、复切、问题排查。约 30 个序列化别名使落盘名 ≠ 源码定义名，解析工具按落盘名理解（别名登记见附录 D）。

### 6.4 内嵌预设：`Metadata/*_settings_N.config`

JSON，条件出现：仅当 3mf 内对官方预设做了修改并保存为项目预设时产出。N 从 1 起、按类型各自递增（与盘号无关）。

| 文件 | 预设类型 | 独有字段（相对 project_settings） |
|---|---|---|
| `machine_settings_N.config` | 打印机预设 | `print_host`、`printhost_*` 凭据族（见 6.3 禁入项）、`inherits` 等 |
| `process_settings_N.config` | 工艺预设 | `compatible_printers*`、`inherits` 等 |
| `filament_settings_N.config` | 耗材预设 | `compatible_printers*` / `compatible_prints*`、`inherits` 等 |

头部含 `name`（预设名）、`version`、`from`（固定 `project`）、`is_custom_defined`、`inherits`。正文按键值形态分两种：

| 形态 | 触发条件 | 内容 |
|---|---|---|
| 差异存根（2～3 字段） | 预设保留继承（`inherits` = 父预设名） | 仅用户修改过的字段 + `inherits` |
| 全量快照（105～318 字段） | 继承断裂（`inherits` 为空串，预设被复制 / 深度修改转为自定义） | 全部字段 |

约定：

- 内嵌预设与 `project_settings.config` 数据约 95% 重复（双写），不一致时谁生效现状未定义（待裁决：Q15）。恢复工程时按各自用途读取，**不应**把包内最后一个配置文件当作最终配置。
- 预设 `version`（如 2.5.0.66）与软件 `version`、`project_schema_version` 是**三套互不相干的版本号**（语义待裁决：Q7，见 7.1）。
- 以官方预设解析继承链可完整解释嵌入字段（实测 embedded-only = 0），"嵌入预设 − 官方链 = 用户真实修改量"；该对账方法论与实证见 [docs/03](../../../docs/03-现状盘点-model_settings与嵌入预设.md)。

### 6.5 条件性工程数据文件

以下文件仅在对应功能使用且数据非空时写出（均在 `Metadata/` 下）：

| 文件 | 格式 | 出现条件与结构 |
|---|---|---|
| `layer_heights_profile.txt` | 文本 | 启用可变层高时。首行 `layer_heights_profile_format_version=2`；其后每对象一行 `object_id=N\|z1;h1;z2;h2...`（z/h 单位 mm）。v2 的 N 是真实 3MF 对象编号；无版本头的 legacy 文件按对象顺序解释 |
| `layer_config_ranges.xml` | XML | 按 Z 区间设置层高时。`<objects><object id><range min_z max_z><option opt_key>`。此处 `object@id` 是**对象顺序号**（从 1 起），与上一条含义不同 |
| `brim_ear_points.txt` | 文本 | 使用鼠耳裙边时。首行 `brim_points_format_version=0`；每对象一行 `object_id=N\|x y z radius ...`（对象顺序号） |
| `custom_gcode_per_layer.xml` | XML | 定义逐层事件（0 换色 / 1 暂停 / 2 换工具 / 3 模板 / 4 自定义）时；按**原盘号**记录 `top_z/type/extruder/color/extra/gcode` |
| `cut_information.xml` | XML | 执行过切割操作时；切割 ID、校验值、连接件数与体积索引 |
| `plate_N.json` | JSON | 2.4.0 起按盘出现。盘面布局摘要（bbox、床型、喷嘴等，自带 `version:2`）；与 `slice_info.config` / plate 节职责重叠（生成代码与字段全集待定位，待裁决：Q1 与 Q16）。字段约定同 [gcode.3mf 规范](../gcode.3mf/gcode_3mf_standard.md) 6.6 |

各文件 `object_id` 的含义不相同（真实对象编号 vs 对象顺序号），读取时以各文件自身的格式头为准。

### 6.6 盘缩略图族与嵌入资源

盘级缩略图族（`plate_N.png` / `plate_N_small.png` / `plate_no_light_N.png` / `top_N.png` / `pick_N.png`）与包级封面（`Auxiliaries/.thumbnails/thumbnail_3mf.png` 等）的约定与 [gcode.3mf 规范](../gcode.3mf/gcode_3mf_standard.md) 6.7、7.4 一致：实际尺寸以 PNG IHDR 为准；缺失降级为默认图，不影响工程恢复。

`Auxiliaries/` 目录（可选）承载包级封面、模型展示图、作者图片与用户附加资源。现状对用户图片**无数量与大小上限**（实测单包 12 张用户照片、单缩略图 >600KB；约束方向待裁决：Q17）。消费者对未知内容应"允许存在、按需取用、未知则忽略"。

### 6.7 通用导出的配置层

通用导出的菜单语义是"去掉 3mf 私有扩展、便于第三方软件读取"，但现状清洗只发生在 3D 几何层（去生产扩展 / UUID / 外拆网格）；`Metadata/` 全套配置（`project_settings.config` 数百字段、`model_settings.config`、盘缩略图）**字节级原样带出**（对照实测见附录 C）。第三方拿到"通用"文件即拿到完整切片工程配置，包括 6.3 所列泄漏面（凭据键、预设痕迹、预设元数据污染——后者待裁决：Q14）。

本规范立场：通用导出**宜**剥离 `Metadata/` 配置层，或仅保留几何引用必需项；剥离范围待裁决（Q21）。

## 7 版本与兼容

### 7.1 五层版本标识

工程 `.3mf` 同时携带五层版本，各管一段语义：

| # | 版本层 | 载体 | 当前值 | 主要用途 |
|---|---|---|---|---|
| 1 | 文件格式版本 | `3dmodel.model` 内 `<metadata name="Snapmaker_Orca:3mfVersion">` | 1（兼容上限 2） | 子模型格式识别；超限检查已禁用 |
| 2 | 生成器（应用）版本 | `<metadata name="Application">Snapmaker_Orca-x.y.z` | 随构建 | BBS 系判别；旧版热床迁移门槛（<1.5.9） |
| 3 | 配置 schema 版本 | `project_settings.config` 内 `project_schema_version` | 1 | 新版文件升级提示（提示不拦截；递增规则待裁决：Q6） |
| 4 | 子格式版本头 | 各内嵌文件首行 / 字段（`layer_heights_profile_format_version=2`、`brim_points_format_version=0`、`plate_N.json` 的 `version:2` 等） | 2 / 0 / 2 不等 | 对应解析器分支 |
| 5 | 预设版本 | 内嵌预设 JSON `version`；vendor profile `version` | Semver | 预设系统门控（语义待裁决：Q7） |

另有 `slice_info.config` 的调试头 `X-SM-Client-*`（全宽版本格式），仅诊断用。

### 7.2 写入端约定

每次保存**应**：

1. 写 `Snapmaker_Orca:3mfVersion` = 1（**不应**停写，子模型识别依赖，见 5.3）；
2. 写 `Application` = `Snapmaker_Orca-<软件版本>`，不伪装 Bambu Studio——使其他切片器不把本文件当作 Bambu 工程；
3. 剥除 `BambuStudio:` / `bamboo_slicer:` 前缀元数据键（历史键只作读取兼容）；
4. 隐私键（`DesignerUserId` / `CreationDate` / `ModificationDate`）恒置空；
5. 条件性文本文件带首行版本头（格式演进走版本头，不隐式变更）。

历史教训：格式版本 v2 曾启用后回滚至 1（兼容上限仍为 2，下次变更**应**直接用 3）；版本号一旦发布，回滚成本极高。

### 7.3 读取端行为

**双管线**：BBS 管线（`bbs_3mf.cpp`）承担本产品 3mf 的全部读写并兼容读取 Bambu Studio 同族文件；Prusa 管线（`3mf.cpp`）仅嗅探并只读 PrusaSlicer 3mf（只读几何、不加载配置）。判据：包内存在 `3D/_rels/3dmodel.model.rels` → 不是 Prusa；`Application` 含 `PrusaSlicer` → 是 Prusa。Prusa 兼容路径的支持范围待裁决（Q20）。

**BBS 系判别只看 `Application` 前缀**（`Snapmaker_Orca-` / `BambuStudio-`）；版本键命中不再置该标志。判别结果决定后续行为：BBS 系全量加载；通用 Core 文件（`From_Other`）仅加载几何并触发多实例拆分。

**版本门现状（审计结论）**：当前**没有任何一道"版本过新即拒载"的硬门槛**——格式版本超限检查、生成器主版本门、未识别键弹窗等均已注释或禁用（清单见 [3mf_version_management](3mf%20documents/3mf_version_management.md) §4.2）。仍在岗的版本行为仅三处：Prusa 判别只读几何、`<1.5.9` 热床尺寸迁移、`project_schema_version` 升级提示（提示，不拦截）。

**配置加载失败语义（关键风险）**：`load_from_json` 遇未知键抛异常后整体中止（后续键不再处理）——主配置失败即整包拒载、无提示无降级；对象 / 零件级覆盖的 `set_deserialize` 异常无捕获穿透，同样中止整个导入。即"新增配置键 = 所有已发布旧版打不开新文件"，这是发布窗口必须冻结新键的原因（改进方向：逐键容忍，见 [3mf_version_management](3mf%20documents/3mf_version_management.md) §5、§9）。

### 7.4 兼容性矩阵

实际生效行为（✅ 正常 / ⚠️ 降级或有条件 / ❌ 拒载）：

| 场景 | 行为 | 机制 |
|---|---|---|
| 旧版文件 → 新程序 | ✅ 尽力迁移 | 无版本视为 0；legacy 改名表；数组折叠 |
| 新版文件 → 旧程序（未知新键） | ❌ **打不开** | `load_from_json` 未知键中止；无提示、无降级 |
| 新版文件 → 旧程序（已知键值变化） | ⚠️ 取决于反序列化 | 标量读双值取前缀（静默丢尾）；向量遇 `nil`（≤2.3.6）抛异常 |
| schema 升版文件 → 旧程序（≥2.4.0） | ⚠️ 弹提示继续加载 | `handle_newer_3mf_schema`；≤2.3.x 无此代码，无感知 |
| Bambu Studio 3mf → 本程序 | ✅ 完整加载 | `Application` 前缀判别；`nil` 已容忍（2026-09 修复） |
| 本程序 3mf → Bambu Studio | ✅ 按非 BBS 项目处理 | `Application` 不再写 `BambuStudio-` |
| PrusaSlicer 3mf → 本程序 | ✅ 仅几何 | Prusa 分支重置配置 |
| 通用 3MF Core → 本程序 | ✅ 仅几何 | `From_Other`；多实例拆分 |
| 本程序 → PrusaSlicer / 通用查看器 | ✅ Core 几何可读 | 通用导出 / Core 兼容几何层 |

### 7.5 变更检查清单

改动 3mf 相关代码 / 格式时逐项核对（细则与源码落点见 [3mf_version_management](3mf%20documents/3mf_version_management.md) §8）：

| 项 | 要点 |
|---|---|
| A 新增配置键 | 先登记字段字典（附录 D 准入）；评估前向破坏（旧版拒载）；读取路径不假设键存在 |
| B 修改键类型 | 标量↔向量双向检查；对象 / 零件级覆盖是暴露面；枚举只增不删，改名走 legacy 改名表 |
| C 改内嵌文件结构 | 新增文件安全（登记 Content_Types 与读取路由）；删改既有文件名 / 元素名禁止；平面文本演进加首行版本头 |
| D 动 schema | 仅"旧程序无法正确理解新文件"的不兼容变更才递增；提示不拦截，正确性靠读端迁移 |
| E 品牌 / 判别键 | 版本键不可停写；新增品牌同步扩展三键等价表与 `Application` 前缀判别 |
| F 发布前回归 | 新版开：自家旧版、Bambu Studio 各代、Prusa、MakerWorld 件、通用 Core；旧版开新版件须有明确错误信息而非静默半载 |

## 8 一致性要求

### 8.1 生产者要求

生产者生成的工程包**应**：

1. 遵循第 4 章的目录层次、压缩方式与 ZIP64 约定；写出 4.2 规定的 `[Content_Types].xml`（不扩充）与 `_rels/.rels`；
2. 主模型遵循 5.1 摘录的 Core 约束（`unit="millimeter"`、流形网格、一致朝向、3×4 变换）；
3. 直接保存形态正确声明生产扩展并以 `p:path` + 关系文件登记外拆部件；通用导出形态不写任何私有扩展（几何层）；
4. 写出 `Application` 与 `Snapmaker_Orca:3mfVersion` 元数据（7.2 全部约定）；
5. 保持编号一一对应：`3dmodel.model` 对象编号 ↔ `model_settings.config` 对象编号 ↔ 外拆文件 `<obj_id>`；按**原始盘号**命名 `plate_N` 系列资源；
6. 三层覆盖仅写差异键（覆盖层为稀疏差异，不重复全局值）；
7. `project_settings.config` 仅写白名单内键（附录 D），凭据类字段序列化前剔除（6.3 禁入项）；
8. 条件性文件带各自的版本头（6.5）；内嵌预设按 6.4 两形态之一写出；
9. 隐私键置空、历史 Bambu 品牌键剥除（7.2）。

### 8.2 消费者要求

消费者**应**：

1. 按普通 ZIP 解包，先读 `[Content_Types].xml` 与 `_rels/.rels`，不因未声明扩展名拒绝已知文件；
2. 通过关系文件 + `p:path` 定位外拆网格，通过包级关系定位主模型，**不应**按目录文件名猜测部件；
3. 按 `unit` 换算坐标，不假定毫米；
4. 按 part > object > project 合成三层覆盖（6.2；现状为隐式规则，待裁决：Q19）；
5. 对缺失的可选资源（缩略图、预设、条件性文件、Auxiliaries 内容）保持容忍，未知则忽略；
6. **不应**凭 `.config` 扩展名假定统一格式（6.3 JSON / 6.1 XML）；
7. **不应**将 `filament_maps`、`identify_id`、`plate_N.json` 的 `id` 当作物理喷头 / 料槽编号使用；
8. 对声明了不支持的必需扩展且影响模型解释的包，报告不支持而非静默丢弃几何。

消费者**宜**：对未知配置键逐键容忍并记录（当前实现整体中止，属已知缺陷而非约定，见 7.3）；`project_schema_version` 高于自身支持时提示升级。

### 8.3 校验模型

工程常规形态（直接保存 / 通用导出）无 G-code / MD5 执行数据——那是 `.gcode.3mf` 的四层校验，见 [gcode.3mf 规范](../gcode.3mf/gcode_3mf_standard.md) 8.3（自动备份形态嵌 G-code，见附录 B）。工程包完整性校验分三层：

| 层级 | 机制 | 能发现 | 局限 |
|---|---|---|---|
| ZIP 传输层 | 每条目自带 CRC32，解压时自动校验 | 传输 / 存储损坏 | 重打包即可通过 |
| 结构层 | 编号交叉验证：`3dmodel.model` 对象编号 ↔ `model_settings.config` 对象节 ↔ 外拆文件 `<obj_id>` ↔ 关系文件 Target + ZIP 条目实际存在 | 编号错配、部件缺失、外拆登记错乱 | 须显式核对，不应按 XML 节点顺序配对 |
| 配置层（可选） | 键字典校验：键 ∈ 白名单、取值形态合法、覆盖键允许集合 | 白名单外键、形态错误、撞名 | 语义正确性不在此层（依赖字段字典维护） |

另可参考 `<mesh_stat>` 网格修复统计做几何健康诊断（诊断信息，非校验）。

### 8.4 版本与兼容

| 情况 | 读取约定 |
|---|---|
| 模型版本键 | 当前写 `Snapmaker_Orca:3mfVersion`；应兼容 `BambuStudio:3mfVersion`、`bamboo_slicer:Version3mf`（三键等价） |
| 版本五层分开读取 | 格式版本 / 生成器版本 / schema 版本 / 子格式版本头 / 预设版本互不相干（7.1），**不应**用其一推断其余 |
| 未知配置键 | 目标态：逐键容忍并记录；现状：整体中止（已知缺陷，见 7.3） |
| legacy 层高文件 | 无版本头的 `layer_heights_profile.txt` 按对象顺序解释，不套用 v2 对象编号 |
| `Content_Types` 不完整 | 已知配置文件未全覆盖；按实际内容格式读取 |
| 通用 Core 文件（无版本键） | 仅加载几何，多实例对象拆分；**不应**期待配置层存在 |
| 未知的必需扩展 | 影响模型解释时报告不支持 |

## 附录 A（资料性）与 3MF Core / Production Extension 的对照

| 维度 | 官方标准 | 本规范工程文件 | 说明 |
|---|---|---|---|
| 容器 | Core：OPC（ISO/IEC 29500-2）ZIP 包 | 完全遵循 | `[Content_Types].xml`、`_rels`、ZIP64 |
| 模型语言 | Core：`model`/`resources`/`build`、mesh、3×4 transform | 完全遵循，`unit` 固定 millimeter | 通用导出形态即纯 Core 文件 |
| 生产扩展 | Production Extension：`p:UUID` 追踪、`p:path` 外部部件 | 直接保存形态采用 | UUID 为确定性合成（非随机）；外拆网格依赖 `p:path` 引用机制 |
| `Metadata/` 配置层 | Core 未定义 | 厂商自有层（BBS 管线） | 属 Core 允许的包内附加部件 + 厂商扩展模式（gcode.3mf 规范附录 A 已引用的 §2.2.1 厂商约定同族） |
| 工具曲线命名 | Core §2.2.1 厂商约定（`.vendor.3mf` 模式） | `.3mf`（工程）/ `.gcode.3mf`（执行产物） | 双扩展名沿用厂商命名模式 |
| 与 Bambu Studio 关系 | — | 同族格式，读端全兼容、写端去品牌 | 见 7.2 去 Bambu 化与 7.4 矩阵 |

结论：几何层"站在标准内"，配置层"站在标准允许的扩展区"。与 Toolpath 扩展路线的对照见 [gcode.3mf 规范](../gcode.3mf/gcode_3mf_standard.md) 附录 A。

## 附录 B（资料性）保存形态与策略位

三种保存路径与策略位掩码（源码 `src/libslic3r/Format/bbs_3mf.hpp` 的 `SaveStrategy`，行号锚点见 [3mf_version_management](3mf%20documents/3mf_version_management.md) §3.3）：

| 形态 | 入口 | 策略组合 | 产物特征 |
|---|---|---|---|
| 直接保存工程 | 保存工程（`Snapmaker_Orca.cpp` 保存链） | `SplitModel \| ShareMesh \| UseLoadedId` | 外拆网格 + 生产扩展 + UUID |
| 通用导出 | 菜单 Export Generic 3MF（`Plater::export_core_3mf`） | `Silence` | 网格内嵌、无任何私有扩展（几何层） |
| 自动备份 | 定时备份 | `Backup = WithGcode \| Silence \| SkipStatic \| SplitModel` | 外拆 + 嵌 G-code 的完整快照 |

`SaveStrategy` 相关位：`Zip64`（ZIP64 容量）、`ProductionExt`（生产扩展）、`WithGcode`（嵌 G-code，工程直接保存不带）、`SplitModel`（外拆，隐含 `ProductionExt`）、`ShareMesh`（重复网格共享外拆文件）、`SkipModel`（仅写盘节——`.gcode.3mf` 导出用）、`SkipStatic` / `Silence` / `UseLoadedId`（行为开关）。备份 / 恢复对应 `LoadStrategy::Restore`。

## 附录 C（资料性）示例文件剖析

### C.1 对照样本：同一工程两种导出

同一工程（Snapmaker_Orca-2.4.0）分别直接保存与通用导出，逐一 MD5 对比（[docs/04](../../../docs/04-问题清单-切片软件团队对齐.md) E 节）：

| 维度 | 直接保存 | 通用导出 |
|---|---|---|
| 包内条目数 | 15 | 11 |
| 网格存储 | 外拆 `3D/Objects/立方体_1.model`（对象名入文件名，中文实测） | 内嵌 `3D/3dmodel.model` |
| `3D/_rels/3dmodel.model.rels` | 有（登记 3 个外部部件） | 无 |
| 生产扩展 + UUID | 有（`requiredextensions="p"`，对象/组件/实例全带） | 无（`xmlns:p` 未声明） |
| `Metadata/` 8 个公共文件 | **字节级完全相同** | 同左 |

结论：两种形态的差异全部集中在 3D 几何层；"通用导出未清洗配置层"由此实证（6.7，待裁决：Q21）。

### C.2 样本统计（7 个实测导出样本）

- `model_settings.config`：对象 130 个、零件 515 个、盘 42 个；`assemble_item` 0 次；
- 对象层覆盖键 32 种（`wall_loops`×47）、零件层 17 种（`extruder`×396）——三层覆盖实证见 6.2；
- `project_settings.config`：584 键（553 定义且落盘 + 31 落盘无静态定义），同版本样本间差异仅 2 个偶发痕迹字段；
- `slice_info.config`：仅 HTTP 风格 header，无实质内容；
- 条件性文件覆盖：`custom_gcode_per_layer.xml`×2、`layer_heights_profile.txt`×1、`brim_ear_points.txt`×1、`Auxiliaries/` 用户图片×2、`plate_N.json`（2.4.0 样本）。

样本清单与逐文件证据见 [docs/01](../../../docs/01-现状盘点-切片软件3mf配置文件.md)、[docs/03](../../../docs/03-现状盘点-model_settings与嵌入预设.md)；入门级文件作用总览见 [3mf 内部文件组成与作用](3mf%20documents/3mf_file_structure.md)。

## 附录 D（规范性）字段字典与写入白名单

`project_settings.config` 及内嵌预设的完整键值以配置字段字典为准（源码静态定义 786 项 × 实测落盘 584 项对账，含类型、默认值、落盘观测与六类归属），随本规范同源维护：[字段字典 CSV](../../../docs/data/field-dictionary-project-settings-v0.csv)；对账方法与结论见 [docs/02](../../../docs/02-字段字典对账-project_settings.md)。切片参数的逐键讲解见[设置参数文档](../../setting/printer/printer_overview.md)（printer / filament / process 三目录）。

**白名单初始集合**：553 项"源码定义且样本落盘" + 31 项"落盘但无静态定义"（其中 18 项为序列化别名，本规范正式登记：`filament_retract_*` 族 ↔ 源码 `retract_*` 族、`machine_max_{acceleration,jerk,speed}_*` 12 项；别名映射的维护机制与新增参数的统一别名规则待确认，待裁决：Q8）。

**六类禁入**（源码定义但不允许进项目文件）：

| 类别 | 数量 | 例 |
|---|---|---|
| SLA 树脂流程专用 | 77 | `pad_*`、`hollowing_*`、曝光 / 校正类 |
| CLI 动作参数 | 52 | `load_*`、`export_*`、`cut_*`、`rotate/scale/split` |
| 运行时派生状态 | 52 | `print_time`、`total_*`、`extruded_*`（结果非设置） |
| GUI 内部 / 废弃候选 | 25 | `zhop`、`brim_ears`、`adaptive_layer_height`（待逐项定论，Q2） |
| 预设系统内部 | 19 | `compatible_*`、`inherits`、`uptodate_*` |
| 打印主机连接（凭据） | 7 | `printhost_*`、`print_host`（安全禁入，Q11） |

**准入流程**（待团队确认，Q18）：新增工艺参数**应**先登记字段字典（含类型、默认值、覆盖层允许性、与结构键撞名检查），登记后方可进入落盘白名单；与切片团队"新增一个工艺配置需要做哪些事"检查单合并维护。字典未收录的键按 6.3 的形态约定处理；字典自身待补录 2.4.0 新增字段的定义位置（待裁决：Q10）。

## 附录 E（资料性）与 gcode.3mf 规范的分工

| 内容 | 本规范 | [gcode.3mf 规范](../gcode.3mf/gcode_3mf_standard.md) | 以谁为准 |
|---|---|---|---|
| OPC 骨架 / Content_Types / 关系约定 | 4.2（引用对方 4.2） | 4.2 | 两文一致，任一 |
| 模型部件（SkipModel 元数据壳） | 5（完整工程几何） | 5（空壳定位） | 各管各形态 |
| 盘索引 plate 节 | 6.1.2 | 6.2 | 键表一致；实例节仅工程包出现 |
| 配置取值形态 / project_settings | 6.3 | 7.1 | **本规范**（共享约定 owner） |
| 内嵌预设 | 6.4 | 7.2 | 本规范 |
| 条件性工程数据文件 | 6.5 | 7.3 | 本规范 |
| 盘缩略图 / Auxiliaries | 6.6 | 6.7 / 7.4 | 两文一致 |
| G-code / MD5 / slice_info 摘要 | —（不涉及） | 6.3～6.5 | gcode 规范 |
| 版本五层 | 7.1 | 8.4（子集） | 本规范 |
| 一致性与校验 | 8 | 8 | 各自包型适用 |

工程 `.3mf` 以 SkipModel 之外的全量策略保存，与 `.gcode.3mf` 互不可替代：前者恢复工程，后者执行打印。两规范的版本演进**应**同步评审（7.5 变更清单对两者同时生效）。

## 参考文献

- 3MF Consortium, *3MF Core Specification* 1.4.0（2025-02-06）
- 3MF Consortium, *3MF Production Extension*
- 3MF Consortium, *3MF Toolpath Extension — Specification & Reference Guide* 1.0.0 RC（2026-09-03）（路线对照）
- GB/T 1.1—2020《标准化工作导则 第 1 部分：标准化文件的结构和起草规则》（体例参考）
- 证据链：[docs/01 现状盘点](../../../docs/01-现状盘点-切片软件3mf配置文件.md)、[docs/02 字段字典对账](../../../docs/02-字段字典对账-project_settings.md)、[docs/03 model_settings 与嵌入预设](../../../docs/03-现状盘点-model_settings与嵌入预设.md)、[docs/04 问题清单](../../../docs/04-问题清单-切片软件团队对齐.md)
- 深度调研：[3MF 版本管理细则](3mf%20documents/3mf_version_management.md)、[3mf 内部文件组成与作用](3mf%20documents/3mf_file_structure.md)
