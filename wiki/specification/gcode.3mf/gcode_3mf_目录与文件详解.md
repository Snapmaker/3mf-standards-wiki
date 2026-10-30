# `.gcode.3mf` 目录与文件详解

> 适用软件:Snapmaker Orca(基线 2.4.x,源码提交 `1bff8daec7dc9daaf3addec9b4c234e8b74f474c`)
> 依据:真实导出包解包实测(`青衣三节棍 v78_4_PLA_4h52m.gcode.3mf`,14 盘、8 耗材、含内嵌预设)+ 源码 `src/libslic3r/Format/bbs_3mf.cpp` / `bbs_3mf.hpp` + 配套规范(《gcode_3mf 文件格式标准》《Snapmaker Orca 3mf 规范 0.9.9》《固件交付技术规范 v0.9》)。
> 本文按包内**目录顺序**逐个介绍文件:位置、作用、内部格式、实测示例与解析要点。

---

## 0. 总览:目录层次

`.gcode.3mf` 本质是一个 **ZIP 归档(OPC 包)**,按 ZIP64 组织;文本类条目用 DEFLATE 压缩,PNG 用 STORE(不二次压缩)。包内路径一律用正斜杠、区分大小写;OPC 关系中的 Target 带前导 `/` 表示包根绝对路径。

```text
job.gcode.3mf                                 ← ZIP 归档(OPC 包,启用 ZIP64)
│
├── [Content_Types].xml                       ← OPC 内容类型声明(固定 4 种扩展名)
│
├── _rels/
│   └── .rels                                 ← 包级关系:主模型 + 封面缩略图
│
├── 3D/
│   └── 3dmodel.model                         ← 3MF 主模型(仅元数据壳,无几何)
│
├── Auxiliaries/                              ← ★ 包根级,与 Metadata 平级
│   ├── .thumbnails/                          ← 包级封面缩略图(3 张)
│   ├── Model Pictures/                       ← 工程内嵌模型图片(可选)
│   └── Profile Pictures/                     ← 工程内嵌作者/预设图片(可选)
│
└── Metadata/                                 ← ★ 核心内容全在此
    ├── model_settings.config                 ← 盘索引:盘号 → 各文件的映射(XML)
    ├── _rels/
    │   └── model_settings.config.rels        ← G-code 条目的 OPC 关系声明
    ├── slice_info.config                     ← 切片结果摘要:耗时/重量/用量/告警(XML)
    ├── plate_N.gcode                         ← ★ 打印执行输入(纯文本 G-code)
    ├── plate_N.gcode.md5                     ← G-code 的 MD5 校验值(32 位大写十六进制)
    ├── plate_N.json                          ← 首层包围盒/标定信息(JSON)
    ├── plate_N.png                           ← 盘渲染缩略图(512×512,带光照)
    ├── plate_N_small.png                     ← 小缩略图(128×128)
    ├── plate_no_light_N.png                  ← 无光照白模渲染图
    ├── top_N.png                             ← 俯视图(打印机屏显)
    ├── pick_N.png                            ← 拾取图(俯视轮廓,屏显)
    ├── project_settings.config               ← 全量打印配置快照(JSON,500+ 键)
    ├── process_settings_N.config             ← 内嵌工艺预设(JSON,条件出现)
    ├── filament_settings_N.config            ← 内嵌耗材预设(JSON,条件出现)
    ├── machine_settings_N.config             ← 内嵌打印机预设(JSON,条件出现)
    ├── layer_heights_profile.txt             ← 可变层高表(条件出现)
    ├── layer_config_ranges.xml               ← 层高区间配置(条件出现)
    ├── brim_ear_points.txt                   ← 鼠耳裙边控制点(条件出现)
    ├── custom_gcode_per_layer.xml            ← 逐层自定义 G-code(条件出现)
    └── cut_information.xml                   ← 模型切割信息(条件出现)
```

命名规则速记:

- **`plate_N` 系列**:`N` = 项目中的**原始盘号,从 1 起**。只导出第 3 盘时就是 `plate_3.gcode`,包内可能没有 plate_1——读取端不能固定假设 plate_1 存在。未切片/切片失败的盘不产出对应条目。
- **`*_settings_N.config` 系列**:`N` 是**同类内嵌预设的编号**(从 1 起、按类型各自递增),**不是盘号**。如实测包中 `filament_settings_1~4` 是 4 套耗材预设,与 14 个盘无关。
- 条件性文件仅在对应功能被使用且数据非空时写出,普通包中通常没有。

---

## 1. `[Content_Types].xml` —— 包的"清单"

**位置**:包根。**格式**:XML。**必选**。

声明各扩展名对应的内容类型,是 OPC 包的标准入口。固定声明 4 种扩展名,所有导出一致:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
 <Default Extension="png" ContentType="image/png"/>
 <Default Extension="gcode" ContentType="text/x.gcode"/>
</Types>
```

**要点**:
- 声明了 `gcode` 扩展名,是"3MF 容器 + 打印扩展"的标识之一;但它**只是类型声明,不构成可执行性证明**——判断可打印要看 Metadata 内容。
- 2.4.x 的 Content Types 未覆盖全部配置文件(如 `.config`、`.json`、`.txt`),已知文件应按实际内容格式解析,不能因未声明而拒绝。

---

## 2. `_rels/.rels` —— 包级关系(包入口)

**位置**:`_rels/.rels`。**格式**:XML。**必选**。

声明包级部件关系:主模型入口 + 封面缩略图。实测内容:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/3D/3dmodel.model" Id="rel-1"
   Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
 <Relationship Target="/Auxiliaries/.thumbnails/thumbnail_3mf.png" Id="rel-2"
   Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/thumbnail"/>
 <Relationship Target="/Metadata/plate_1.png" Id="rel-4"
   Type="http://schemas.bambulab.com/package/2021/cover-thumbnail-middle"/>
 <Relationship Target="/Metadata/plate_1_small.png" Id="rel-5"
   Type="http://schemas.bambulab.com/package/2021/cover-thumbnail-small"/>
</Relationships>
```

**要点**:
- `Id`(rel-1 等)只要求在关系文件内唯一,**不能当作业务标识写死**;消费端按 `Type` + `Target` 匹配。
- `Type` 里的 URI(微软/ bambulab / snapmaker 域名)**只是标识字符串,不会联网解析**。新版 Snapmaker 导出用 `schemas.snapmaker.com/package/2026/...`,本实测包(2.4.0)仍写 `schemas.bambulab.com/package/2021/...`——读取端对两种前缀应**按后缀匹配兼容接受**。
- 这里的封面缩略图只用于**预览**,不参与执行目标(选盘)的确定。

---

## 3. `3D/3dmodel.model` —— 3MF 主模型(元数据壳)

**位置**:`3D/3dmodel.model`。**格式**:3MF XML。**必选**。

gcode.3mf 以 `SkipModel` 策略导出,`<resources>` 与 `<build>` **为空,没有任何几何**;文件只剩 `<metadata>` 元数据,作用是让通用 3MF 工具能识别包骨架。实测内容(节选):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xml:lang="en-US"
       xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
       xmlns:BambuStudio="http://schemas.bambulab.com/package/2021"
       xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06"
       requiredextensions="p">
 <metadata name="Application">Snapmaker_Orca-2.4.0</metadata>
 <metadata name="BambuStudio:3mfVersion">1</metadata>
 <metadata name="Title">全内构可变形-青衣-惊堂木-三节棍1:1模型道具</metadata>
 <metadata name="Designer">Shigure42</metadata>
 <metadata name="License">MakerWorld Exclusive License</metadata>
 <metadata name="Description">(长 HTML 文本,转义存储)</metadata>
 <metadata name="Thumbnail_Middle">/Metadata/plate_1.png</metadata>
 <metadata name="Thumbnail_Small">/Metadata/plate_1_small.png</metadata>
 <resources>
 </resources>
 <build/>
</model>
```

**要点**:
- 常见键:`Application`(生成器,如 `Snapmaker_Orca-2.4.0`)、`Title`/`Designer`/`Description`/`License`/`CreationDate`(多为空)。MakerWorld 下载的工程还会带 `DesignModelId`、`DesignProfileId`、`ProfileTitle` 等平台元数据。
- 格式版本键当前写 `Snapmaker_Orca:3mfVersion=1`;读取端需兼容历史键 `BambuStudio:3mfVersion`、`bamboo_slicer:Version3mf`(本实测包即写 Bambu 键)。该值是**工程格式标记,不是固件执行协议版本**。
- 固件**无需解析几何**,也不要指望从这里恢复网格——真正要读的内容全在 `Metadata/`。

---

## 4. `Auxiliaries/` —— 嵌入资源目录(包根级)

**位置**:包根下 `Auxiliaries/`,与 `Metadata/` **平级**(不在 Metadata 之内)。**格式**:按资源类型。**可选**。

源码定义(`bbs_3mf.cpp:168-191`):路径常量均以 `/Auxiliaries/` 开头,OPC Target 前导 `/` 即包根。

```text
Auxiliaries/
├── .thumbnails/
│   ├── thumbnail_3mf.png        ← 3MF 封面(包级,_rels/.rels 的 thumbnail 关系指向它)
│   ├── thumbnail_middle.png     ← 中图封面
│   └── thumbnail_small.png      ← 小图封面
├── Model Pictures/              ← 工程内嵌的模型展示图(本实测包为 .webp,来自 MakerWorld)
└── Profile Pictures/            ← 作者/预设图片
```

**要点**:
- 包级封面在 `Auxiliaries/.thumbnails/`,**盘级预览在 `Metadata/plate_N.png`**——两种缩略图位置不同,勿混淆。
- 内容与子目录名不固定(图片、字体等都可能进),读取端应"允许存在、按需取用、未知则忽略"。
- 仅缺封面图不影响几何与配置的正常读取。

---

## 5. `Metadata/` —— 核心目录

### 5.1 `model_settings.config` —— 盘索引(盘 → 文件的主映射)

**格式**:XML。**必选**。根节点 `<config>`,每盘一个 `<plate>` 节,字段全部以 `<metadata key="..." value="..."/>` 写出。实测内容:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<config>
  <plate>
    <metadata key="plater_id" value="1"/>
    <metadata key="plater_name" value="PLA灰"/>
    <metadata key="locked" value="true"/>
    <metadata key="filament_map_mode" value="Auto For Flush"/>
    <metadata key="filament_maps" value="1 1 1 1 1 1 1 1"/>
    <metadata key="gcode_file" value="Metadata/plate_1.gcode"/>
    <metadata key="thumbnail_file" value="Metadata/plate_1.png"/>
    <metadata key="thumbnail_no_light_file" value="Metadata/plate_no_light_1.png"/>
    <metadata key="top_file" value="Metadata/top_1.png"/>
    <metadata key="pick_file" value="Metadata/pick_1.png"/>
    <metadata key="pattern_bbox_file" value="Metadata/plate_1.json"/>
  </plate>
  <!-- 每盘一个 <plate>,plater_id 递增;实测包含 14 盘 -->
</config>
```

关键字段含义:

| key | 含义 | 注意 |
|---|---|---|
| `plater_id` | 原始盘号 N(1 起) | 与 `slice_info.config` 的 `index` 是同一个 N |
| `plater_name` | 盘名(可为空、可中文) | 仅显示用 |
| `locked` | 编辑器中盘锁定状态 | 展示用,不是设备权限锁 |
| `filament_maps` | 耗材映射 | **当前写出全 1,不能当真实物理喷头/料槽映射用** |
| `gcode_file` | 本盘 G-code 的包内路径 | **★ 核心指针**;部分盘可为空(未切片) |
| `thumbnail_file` 等 | 各预览资源路径 | 可选,按实际存在性读取 |
| `pattern_bbox_file` | 指向 `plate_N.json` | 增强功能(首层定位)用 |

**要点**:
- 可能列出项目**全部**盘(含未切片的);"出现 `<plate>` 节" ≠ 可打印,须联合 `gcode_file` 非空 + ZIP 条目实际存在验证。
- gcode.3mf 中只有 `<plate>` 节(工程 `.3mf` 里额外的 `<object>/<part>/<assemble>` 在 SkipModel 导出时省略)。

### 5.2 `Metadata/_rels/model_settings.config.rels` —— G-code 关系声明

**格式**:XML。**必选**(有 G-code 时)。OPC 惯例:部件自己的关系放在该部件目录的 `_rels/` 子目录下。每份 G-code 一条:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/Metadata/plate_1.gcode" Id="rel-1" Type="http://schemas.bambulab.com/package/2021/gcode"/>
 <Relationship Target="/Metadata/plate_2.gcode" Id="rel-2" Type="http://schemas.bambulab.com/package/2021/gcode"/>
 <!-- 每盘一条;新版导出 Type 为 .../snapmaker.com/package/2026/gcode,按后缀兼容 -->
</Relationships>
```

**要点**:定位 G-code 优先走这个关系文件,比猜测文件名可靠;关系本身**不携带盘号/机型/MD5**,最终仍以 ZIP 实际条目存在为准。

### 5.3 `slice_info.config` —— 切片结果摘要

**格式**:XML。根 `<config>`,含一个 `<header>` 和每个**切片有效**盘一个 `<plate>`(注意:只列有效盘,范围与 model_settings 不同)。实测内容:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<config>
  <header>
    <header_item key="X-BBL-Client-Type" value="slicer"/>
    <header_item key="X-BBL-Client-Version" value=""/>
  </header>
  <plate>
    <metadata key="index" value="1"/>                        <!-- 原盘号 N -->
    <metadata key="printer_model_id" value="SM_U1"/>         <!-- 机型 ID -->
    <metadata key="nozzle_diameters" value="0.4,0.4,0.4,0.4"/>
    <metadata key="timelapse_type" value="0"/>               <!-- 0 传统/1 平滑/-1 不可用 -->
    <metadata key="prediction" value="23139"/>               <!-- 预计耗时,秒 -->
    <metadata key="weight" value="171.19"/>                  <!-- 预计耗材重量,克 -->
    <metadata key="outside" value="false"/>                  <!-- 路径越界标记 -->
    <metadata key="support_used" value="true"/>
    <metadata key="label_object_enabled" value="false"/>
    <metadata key="filament_maps" value="1 1 1 1 1 1 1 1"/>
    <object identify_id="1724" name="青衣三节棍  v85_4" skipped="false"/>
    <object identify_id="1900" name="青衣三节棍 v87.step" skipped="false"/>
    <filament id="1" tray_info_idx="GFSL991" type="PLA" color="#505050"
              used_m="57.40" used_g="171.19"/>
    <warning msg="bed_temperature_too_high_than_filament" level="1" error_code="1000C001"/>
  </plate>
  <!-- 实测包含 14 个有效盘 -->
</config>
```

子节点说明:

| 子节点 | 字段 | 含义 |
|---|---|---|
| `<object/>` | `identify_id` / `name` / `skipped` | 盘上对象清单;identify_id 是不透明实例标识,**不按数组下标解释** |
| `<filament/>` | `id` / `tray_info_idx` / `type` / `color` / `used_m` / `used_g` | 逐逻辑耗材用量(米/克,固定两位小数);`id` 是统计索引+1,**不是物理喷头号**;列表可能稀疏(实测盘 2 出现 id=1、id=5) |
| `<warning/>` | `msg` / `level` / `error_code` | `level`:0 提示 / 1 警告 / 2 错误;`msg` 是枚举串不是本地化文案 |

**要点**:
- `index` 与 `plater_id` 是同一个 N,二者 + `gcode_file` + 实际条目应**四方一致**;不一致应拒绝而非按节点顺序纠正。
- `prediction`/`weight` 是估计值,缺失或为空时显示"未知",不当作 0;`outside=true` 或 `level=2` 建议阻止启动。
- 兼容提示:header 键存在 `X-SM-Client-*` 与 `X-BBL-Client-*` 两种历史写法(实测 2.4.0 包写 `X-BBL-*`),版本值可能为空,读取端两者都要认。

### 5.4 `plate_N.gcode` —— 打印执行输入(核心)

**格式**:纯文本 G-code。每盘一份,由源 G-code 文件以二进制方式原样压入 ZIP,**封装阶段不重写命令**。文件自描述,首尾带结构化注释块:

```text
; HEADER_BLOCK_START
; generated by Snapmaker Orca 2.4.0 on 2026-10-28 at 10:38:35
; total layer number: 1155
; filament_density: 1.24,1.24,1.24,1.25,1.24,1.24,1.24,1.24   ← 逐耗材
; filament_diameter: 1.75,1.75,...                            ← 逐耗材
; max_z_height: 231.05
; HEADER_BLOCK_END

; THUMBNAIL_BLOCK_START
; thumbnail begin 48x48 868
; iVBORw0KGgo...          ← base64 PNG(本包含 48×48 与 300×300 两块)
; thumbnail end
; THUMBNAIL_BLOCK_END

<G-code 指令主体>
(实测单盘约 232 万行;方言、工具切换、起止宏由机型预设决定)

; CONFIG_BLOCK_START        ← 尾部配置块(约数百行 "; key = value" 完整参数)
; layer_height = 0.25
; first_layer_bed_temperature = 65
; bed_shape = 0.5x1,270.5x1,270.5x271,0.5x271
; CONFIG_BLOCK_END
```

**要点**:
- 执行内容 = 文本 G-code;**容器解析通过 ≠ 机型能执行全部指令**,能力由预设/G-code 方言决定。
- 校验或执行前**不得**做换行符转换、字符集转换、去注释等任何字节改写(会破坏 MD5)。

### 5.5 `plate_N.gcode.md5` —— 完整性校验

**格式**:32 字节 ASCII,与同盘 G-code 一一对应。实测内容(整个文件就这一行,无换行):

```text
1C7E3513A7E0F4F38C1E50C6895344D3
```

精确定义:

| 项 | 定义 |
|---|---|
| 摘要输入 | `plate_N.gcode` **解压后的完整原始字节**(不是压缩流,不是整个 3mf 包) |
| 算法/编码 | MD5,16 字节摘要按 `%02X` 写成 **32 个大写十六进制字符** |
| 文件长度 | 恰好 32,无换行、BOM、文件名或 NUL |
| 失败处理 | 缺失/非法/不符 → 在执行任何指令前拒绝启动 |

注意:通用 `md5sum` 命令的输出带文件名和换行,与包内格式不同,校验代码不能直接整行比对。MD5 与 ZIP 条目自带的 CRC32 只验证传输完整性,**不是防篡改签名**。

### 5.6 `plate_N.json` —— 首层包围盒/标定信息

**格式**:JSON(单行)。供打印机端首层定位、图案标定、图形化提示。实测内容(格式化后):

```json
{
  "bbox_all": [88.26, 94.32, 177.36, 177.68],          // 整盘首层包围盒 [minX,minY,maxX,maxY]
  "bbox_objects": [                                     // 逐对象首层包围盒
    { "id": 2853, "name": "青衣三节棍  v85_4",
      "bbox": [136.31, 142.18, 177.12, 177.18],
      "area": 477.57, "layer_height": 0.25 },
    ...
  ],
  "bed_type": "textured_plate",
  "filament_colors": [],
  "filament_ids": [],
  "first_extruder": 0,
  "is_seq_print": false,                                // 是否逐对象打印
  "nozzle_diameter": 0.4,
  "version": 2                                          // 数据结构版本
}
```

**要点**:`id` 与 slice_info 的 `identify_id` 属不同标识域;`filament_colors` 等字段可能为空,展示侧需容忍。本版基础执行规范未冻结该文件的坐标约定,增强功能(首层检测等)接入前需另行确认。

### 5.7 `plate_N.png` / `plate_N_small.png` —— 盘渲染缩略图

**格式**:PNG(STORE 方式存储)。正常生成时 `plate_N.png` 为 512×512 带光照正交渲染,`plate_N_small.png` 为 128×128 降采样版,用于 APP/设备列表显示。实际尺寸**以 PNG IHDR 为准**,不要按固定值假设。可选资源:缺失或损坏时降级为默认图,不影响执行。

### 5.8 `plate_no_light_N.png` —— 无光照白模图

**格式**:PNG。同角度的无光照渲染(白模),备用预览。可选。

### 5.9 `top_N.png` —— 俯视图

**格式**:PNG。首层布局俯视示意,打印机屏显用。可选。

### 5.10 `pick_N.png` —— 拾取图

**格式**:PNG。俯视轮廓图,用于屏显对象拾取提示。可选。

> 5.8–5.10 属于增强资源;是否识别、坐标如何对应,本版基础规范未定义,固件需要时须另行冻结接口。

### 5.11 `project_settings.config` —— 全量打印配置快照

**格式**:**JSON**(注意:扩展名是 `.config`,内容是 JSON;同目录的 model_settings/slice_info 则是 XML——不能凭扩展名选解析器)。切片时所有生效参数的完整扁平键值(实测 500+ 键,按键名字典序排列):

```json
{
    "accel_to_decel_enable": ["1"],
    "accel_to_decel_factor": ["50%"],
    "activate_air_filtration": ["0","0","0","0","0","0","0","0"],
    "adaptive_bed_mesh_margin": "0",
    "bed_shape": "0.5x1,270.5x1,270.5x271,0.5x271",
    "filament_type": ["PLA","PLA","PLA","PLA","PLA","PLA","PLA","PLA"],
    "layer_height": "0.25",
    "printer_settings_id": "...",
    "...": "……"
}
```

取值约定(与工程 3mf 规范一致):

| 类型 | 写法 | 说明 |
|---|---|---|
| 数值 | `"3"`、`"0.2"` | 一律字符串,按字段含义转数字 |
| 布尔 | `"0"` / `"1"` | 不是 JSON true/false |
| 百分比 | `"15%"` | 带 %,不能与绝对值混同 |
| 数组 | `["200","220"]` | 元素仍是字符串;可空字段可能含 `"nil"`(≠ 0) |
| 点/点列表 | `"10,20"` / `["0x0","270x0"]` | 单点逗号分隔,点列表每项用 x 分隔 |

头部元字段:`version`(切片器版本)、`name: "project_settings"`、`from: "project"`、`project_schema_version: "1"`。用途:拖回软件恢复参数/复切、问题排查。**固件不从这里重新切片,也不据此改写 G-code**。

### 5.12 `process_settings_N.config` / `filament_settings_N.config` / `machine_settings_N.config` —— 内嵌预设

**格式**:JSON。**条件出现**:仅当项目激活了"项目内嵌预设"(典型:MakerWorld 下载的工程)时导出。N 从 1 起按类型各自递增(实测包:filament×4 + machine×1 + process×1,对应工程里 4 套耗材预设 + 1 套机器 + 1 套工艺)。

| 文件 | 预设类型 | 内容 |
|---|---|---|
| `machine_settings_N.config` | 打印机预设 | 机型、喷嘴、打印区域、起止 G-code 模板等 |
| `process_settings_N.config` | 工艺预设 | 层高/壁厚/填充/速度/支撑等 |
| `filament_settings_N.config` | 耗材预设 | 温度/回抽/冷却/流量比等 |

结构同 project_settings,头部多 `name`(预设名)/`version`/`is_custom_defined`;可能只含相对父预设的差异项。普通导出没有这些文件。

### 5.13 条件性文件(按需出现)

| 文件 | 格式 | 出现条件与内部结构 |
|---|---|---|
| `layer_heights_profile.txt` | 文本 | 对象启用可变层高时;首行 `layer_heights_profile_format_version=2`,其后每对象一行 `object_id=N\|z1;h1;z2;h2...`(z/h 单位 mm)。v2 的 N 是真实 3MF 对象 id;无版本头的 legacy 文件按对象顺序解释 |
| `layer_config_ranges.xml` | XML | 按 Z 区间设置层高时;`<objects><object id><range min_z max_z><option opt_key>`。此处 object@id 是**对象顺序号**(从 1 起),与上一条的 id 含义不同 |
| `brim_ear_points.txt` | 文本 | 使用鼠耳裙边时;首行 `brim_points_format_version=0`,每对象一行 `object_id=N\|x y z radius ...`(对象顺序号) |
| `custom_gcode_per_layer.xml` | XML | 定义了逐层事件(换色/暂停/模板/自定义)时;按原盘号记录 `top_z/type/extruder/color/extra/gcode`,`type`:0 换色/1 暂停/2 换工具/3 模板/4 自定义 |
| `cut_information.xml` | XML | 执行过切割操作时;切割 ID、校验值、连接件数与体积索引 |

---

## 6. 盘号关联:四方交叉验证

同一个盘 N 在四处出现,读取端应交叉核对,**不能按 XML 节点顺序配对**,也不能把"有 plate 节点"当可打印:

```text
model_settings.config  plater_id="3"
   ↔  slice_info.config  index="3"
   ↔  model_settings.config  gcode_file="Metadata/plate_3.gcode"
   ↔  .rels 关系 Target + ZIP 内实际条目存在(含 .md5)
```

多盘包必须明确选盘(或由用户选);单盘包可自动选中唯一可打印盘,但**保留其原始 N**(只导出第 3 盘时执行的就是 `plate_3.gcode`,不得转成第 1 盘)。

---

## 7. 实测兼容性备注(2.4.0 真实导出包)

以下差异来自实测,读取端实现时需要覆盖:

1. **关系 URI 前缀混用**:`_rels/.rels` 与 `model_settings.config.rels` 实际写的是 `schemas.bambulab.com/package/2021/...`,而非新版文档描述的 `schemas.snapmaker.com/package/2026/...`。应按 URI **后缀**(如 `/gcode`、`/cover-thumbnail-middle`)匹配,两种前缀都接受。
2. **格式版本键混用**:`3dmodel.model` 写的是 `BambuStudio:3mfVersion`,不是 `Snapmaker_Orca:3mfVersion`;三个键(Snapmaker_Orca/BambuStudio/bamboo_slicer)都要认,值当前都是 1。
3. **slice_info 头键**:实测写 `X-BBL-Client-Type` / `X-BBL-Client-Version`(且版本值为空),规范文档描述为 `X-SM-Client-*`。两种都按"客户端来源标识"处理,仅用于诊断,不作为准入条件。
4. **稀疏耗材列表**:slice_info 的 `<filament>` 节点 id 可能跳号(实测盘 2 只有 id=1 和 id=5),节点位置不等于 id。
5. **Content Types 不完整**:`.config`/`.json`/`.txt` 等未声明类型,属已知现状,按实际内容格式解析。

---

## 8. 参考资料

- 源码:`src/libslic3r/Format/bbs_3mf.cpp`(格式常量 L109-191、写出策略、MD5 与配置导出)、`bbs_3mf.hpp`(文件名模板)、`src/slic3r/GUI/Plater.cpp`(导出入口)、`PartPlate.cpp`(有效盘筛选)
- 固定提交:`1bff8daec7dc9daaf3addec9b4c234e8b74f474c`(https://github.com/Snapmaker/OrcaSlicer)
- 3MF Consortium Core Specification / Production Extension
- 配套文档:《gcode_3mf 文件格式标准.md》《Snapmaker Orca 3mf 规范 0.9.9.md》《Snapmaker_Orca_2.4.1_gcode.3mf_固件交付技术规范_v0.9》
