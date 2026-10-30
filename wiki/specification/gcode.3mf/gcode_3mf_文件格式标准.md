# `.gcode.3mf` 文件格式标准

> 适用软件:Snapmaker Orca(本仓库 `Snapmaker_Orca`)
> 依据:源码 `src/libslic3r/Format/bbs_3mf.cpp` / `bbs_3mf.hpp`、`src/slic3r/GUI/Plater.cpp`、`src/slic3r/GUI/PartPlate.cpp`,并对真实导出文件(单盘 1 例、4 盘 1 例)解包验证。
> 本文档同时向下兼容读取 Bambu Studio 导出的同名格式(历史命名空间差异见 §7.2)。

---

## 1. 概述

`.gcode.3mf` 是切片完成后由软件导出的**可打印文件包**,本质是一个 **ZIP 归档**,内部遵循两套约定的组合:

| 约定层次 | 内容 | 作用 |
|---|---|---|
| OPC(Open Packaging Conventions) | `[Content_Types].xml`、`_rels/.rels` | ZIP 作为"包"的标准骨架,声明内容类型与部件关系 |
| 3MF(3D Manufacturing Format) | `3D/3dmodel.model` 作为包主部件 | 使文件在 3MF 生态(Windows 3D 查看器等)中可被识别 |
| BBS 扩展(Bambu Studio 系约定) | `Metadata/` 目录 | 存放盘(Plate)数据、G-code、配置、切片摘要、缩略图 |
| Snapmaker 扩展 | 自有 Relationship 命名空间 | 区分自家导出的 gcode/封面缩略图关系声明 |

**生成入口**:菜单 `文件 → 导出 → Export plate sliced file`(导出当前盘)或 `Export all plate sliced file`(导出全部盘),实现于 [Plater.cpp:20460](../src/slic3r/GUI/Plater.cpp#L20460),保存策略为
`SaveStrategy::Silence | SplitModel | WithGcode | SkipModel` —— 即**带 G-code、跳过模型几何**,这是它与普通项目 `.3mf` 的根本区别(详见 §6)。

**设计目的(一句话)**:把"给机器执行的数据(G-code)"和"给人/APP 看的信息(缩略图、耗时、重量、耗材用量、完整参数)"打包成**一个文件、一份拷贝、一次传输**,并原生支持**多盘**。

---

## 2. 解压后的目录结构

把 `.gcode.3mf` 用 ZIP 工具直接解压(或将扩展名改为 `.zip`)即可看到以下结构。**单盘**实测样例:

```text
xxx.gcode.3mf                              ← ZIP 归档(OPC 包)
├── [Content_Types].xml                    ← OPC 内容类型声明(固定 4 种扩展名)
├── _rels\
│   └── .rels                              ← 包级关系:主模型 + 封面缩略图
├── 3D\
│   └── 3dmodel.model                      ← 3MF 主模型文件(此处仅元数据,无网格)
└── Metadata\
    ├── plate_1.png                        ← 盘 1 渲染缩略图(带光照,正交相机)
    ├── plate_1_small.png                  ← 盘 1 小缩略图(128×128,屏显/列表用)
    ├── plate_no_light_1.png               ← 盘 1 无光照渲染缩略图
    ├── top_1.png                          ← 盘 1 俯视图(首层布局示意)
    ├── pick_1.png                         ← 盘 1 拾取图(俯视轮廓)
    ├── plate_1.json                       ← 盘 1 首层包围盒 / 标定信息(JSON)
    ├── plate_1.gcode                      ← 盘 1 的 G-code 主体
    ├── plate_1.gcode.md5                  ← 盘 1 G-code 的 MD5 校验值
    ├── _rels\
    │   └── model_settings.config.rels     ← model_settings.config 的关系:gcode 引用
    ├── model_settings.config              ← 盘元数据索引(每盘一节)
    ├── slice_info.config                  ← 切片结果摘要(耗时/重量/耗材/警告)
    └── project_settings.config            ← 全量打印配置(JSON,500+ 参数)
```

各文件作用速查表:

| 文件 | 格式 | 作用 | 简述 |
|---|---|---|---|
| `[Content_Types].xml` | XML | OPC 声明 `rels`/`model`/`png`/`gcode` 四种扩展名的内容类型 | 包的"清单" |
| `_rels/.rels` | XML | 声明主模型 `3D/3dmodel.model`、封面缩略图的关系 | 包入口 |
| `3D/3dmodel.model` | XML | 3MF 主模型;gcode.3mf 中 `<resources>`/`<build>` 为空,仅保留 `Application`、版本等元数据 | 3MF 兼容骨架 |
| `Metadata/plate_N.png` | PNG | 盘 N 的 3D 渲染缩略图 | 预览图 |
| `Metadata/plate_N_small.png` | PNG | 盘 N 缩略图的 128×128 降采样版 | 小图 |
| `Metadata/plate_no_light_N.png` | PNG | 盘 N 无光照渲染图(白模) | 备用预览 |
| `Metadata/top_N.png` | PNG | 盘 N 俯视图 | 打印机屏显 |
| `Metadata/pick_N.png` | PNG | 盘 N 拾取图 | 打印机屏显 |
| `Metadata/plate_N.json` | JSON | 盘 N 首层包围盒(整盘+逐对象)、耗材颜色、首层挤出机等 | 首层定位/标定 |
| `Metadata/plate_N.gcode` | 文本 | 盘 N 的 G-code(deflate 压缩存储) | 打印数据 |
| `Metadata/plate_N.gcode.md5` | 文本 | 盘 N G-code 的 32 位十六进制 MD5 | 完整性校验 |
| `Metadata/_rels/model_settings.config.rels` | XML | 把每个 `plate_N.gcode` 声明为 gcode 类型关系 | gcode 索引 |
| `Metadata/model_settings.config` | XML | 每盘的名称、锁、G-code/缩略图文件路径、对象实例归属 | 盘索引 |
| `Metadata/slice_info.config` | XML | 每盘切片摘要:机型、喷嘴、预计耗时、重量、逐耗材用量、对象清单、警告 | 结果摘要 |
| `Metadata/project_settings.config` | JSON | 切片时的完整合并配置(全参数) | 复切/回读配置 |

**条件性出现**的文件(视项目功能而定,普通 gcode.3mf 中通常没有;详见 §4.3 与 §6):

```text
Metadata\
├── layer_heights_profile.txt      ← 逐对象可变层高表(使用了自定义层高时)
├── layer_config_ranges.xml        ← 逐对象层高区间配置(按区间设置层高时)
├── brim_ear_points.txt            ← 耳形裙边控制点(使用该功能时)
├── custom_gcode_per_layer.xml     ← 逐层自定义 G-code(换色/暂停等)
├── cut_information.xml            ← 模型切割信息(执行过切割时)
├── process_settings_N.config      ← 内嵌工艺预设(JSON,§5)
├── filament_settings_N.config     ← 内嵌耗材预设(JSON,§5)
├── machine_settings_N.config      ← 内嵌打印机预设(JSON,§5)
Auxiliaries\                       ← 嵌入资源目录(项目内嵌图片/字体/封面等)
```

> 命名规则中的 `N` 一律为**盘号,从 1 开始**(代码中以 `plate_index + 1` 格式化,见 [bbs_3mf.hpp:22-31](../src/libslic3r/Format/bbs_3mf.hpp#L22-L31))。

---

## 3. G-code 的存储形式(单盘 / 多盘)

### 3.1 所在目录与命名

所有 G-code 统一存放在 `Metadata/` 目录,命名模板:`Metadata/plate_%d.gcode`,`%d` 为盘号(1 起)。每份 G-code 伴随一个同名 `.gcode.md5`。

### 3.2 单盘(导出当前盘)

菜单"Export plate sliced file"只包含**当前盘**的 G-code:

```text
Metadata\
├── plate_1.gcode          ← 唯一的 G-code
├── plate_1.gcode.md5      ← 对应 MD5
├── (其余 plate_1.* 缩略图/JSON 若干)
└── model_settings.config  ← 仍会列出所有盘,但只有本盘的 gcode_file 值非空
```

### 3.3 多盘(导出全部盘)

菜单"Export all plate sliced file"包含**每个已切片成功的盘**各一份 G-code(4 盘实测样例):

```text
Metadata\
├── plate_1.gcode (3.7 MB)   ├── plate_1.gcode.md5   ├── plate_1.png / _small / no_light_1 / top_1 / pick_1 / plate_1.json
├── plate_2.gcode (5.5 MB)   ├── plate_2.gcode.md5   ├── plate_2.png ...
├── plate_3.gcode (4.8 MB)   ├── plate_3.gcode.md5   ├── plate_3.png ...
└── plate_4.gcode (3.2 MB)   ├── plate_4.gcode.md5   ├── plate_4.png ...
```

要点:

- **逐盘独立**:每盘一份完整 G-code,各自校验、各自可单独取用;未切片或切片失败的盘不出 `plate_N.gcode` 与 `plate_N.gcode.md5`。
- **盘与文件的映射**记录在两处,一一对应:
  - `Metadata/model_settings.config`:`<metadata key="gcode_file" value="Metadata/plate_2.gcode"/>`
  - `Metadata/_rels/model_settings.config.rels`:每个 gcode 一条 `<Relationship Target="/Metadata/plate_N.gcode" ... Type=".../gcode"/>`
- 盘的取舍逻辑见 [PartPlate.cpp:5963-5997](../src/slic3r/GUI/PartPlate.cpp#L5963-L5997):当前盘 / 全部盘 / 指定盘。
- 写入实现:`_add_gcode_file_to_archive`([bbs_3mf.cpp:8019](../src/libslic3r/Format/bbs_3mf.cpp#L8019)),各盘并行压缩后并入主包;PNG 以**存储(不压缩)**方式写入,其余文本用 deflate。

### 3.4 G-code 文件自身的内容组织

`plate_N.gcode` 解压后是纯文本 G-code,首尾带有结构化注释块:

```text
; HEADER_BLOCK_START          ← 头信息块
; generated by Snapmaker Orca 2.4.0 on 2026-10-27 at ...
; total layer number: 336     ← 总层数
; filament_density: 1.32,...  ← 耗材密度(逐耗材)
; filament_diameter: 1.75,... ← 耗材线径
; max_z_height: 27.04         ← 最大打印高度
; HEADER_BLOCK_END

; THUMBNAIL_BLOCK_START       ← 内嵌缩略图(base64 PNG,如 48×48、300×300)
; thumbnail begin 300x300 5892
; iVBORw0KGgo...
; THUMBNAIL_BLOCK_END

<G-code 指令主体>

; CONFIG_BLOCK_START(约 500 行)  ← 尾部配置块:完整打印参数 "; key = value"
; layer_height = 0.08
; filament_type = PLA
; print_settings_id = ...
; CONFIG_BLOCK_END
```

即:**G-code 文件本身就是"指令 + 自描述元数据"的载体**;`.gcode.3mf` 再把它与多盘结构、校验值、富配置打包。

### 3.5 MD5 校验文件

`Metadata/plate_N.gcode.md5` 为 32 个字符的十六进制 MD5(无换行),由导出时对源 G-code 计算([bbs_3mf.cpp:6188-6208](../src/libslic3r/Format/bbs_3mf.cpp#L6188-L6208))。打印机/传输端解包后可用它校验 G-code 是否在传输中损坏。

---

## 4. 配置文件详解

### 4.1 `Metadata/project_settings.config` —— 全量打印配置(JSON)

**作用**:切片时所有生效参数的**完整快照**(系统预设 + 用户修改合并后的最终值)。软件重新加载 `.gcode.3mf` 时用它恢复/核对打印参数,也是"复切"与问题排查的依据。

**结构**:

- 头部三个元字段:`version`(切片器版本号)、`name`(固定 `project_settings`)、`from`(固定 `project`);
- 之后约 500~600 个**扁平键值**:标量为字符串,多值参数(逐耗材/逐对象)为字符串数组。

**示例**(节选,实测文件共 579 键):

```json
{
    "version": "2.4.0",
    "name": "project_settings",
    "from": "project",
    "layer_height": "0.08",
    "first_layer_height": "0.24",
    "nozzle_diameter": "0.4 0.4 0.4 0.4",
    "bed_shape": "0.5x1,270.5x1,270.5x271,0.5x271",
    "filament_type": ["PLA", "PLA", "PLA", "PLA"],
    "filament_colour": ["#D9A63A", "#D9A63A", "#F4E2C1", "#ED1C24"],
    "filament_settings_id": ["Snapmaker PLA Silk @U1", "..."],
    "print_settings_id": "0.08 Extra Fine @Snapmaker U1 (0.4 nozzle)",
    "printer_settings_id": "Snapmaker U1 (0.4 nozzle)",
    "curr_bed_type": "Textured PEI Plate",
    "print_sequence": "by layer",
    "spiral_mode": "0",
    "wall_loops": "3",
    "...": "……"
}
```

### 4.2 `Metadata/model_settings.config` —— 盘/对象元数据索引(XML)

**作用**:描述"包里有哪些盘、每盘引用哪些文件、盘上放了哪些对象实例"。加载端据此把 `plate_N.gcode`、缩略图与盘号对应起来。

**结构**(gcode.3mf 中因跳过模型,仅含 `<plate>` 节;项目 3mf 中还含 `<object>`/`<part>`/`<assemble>`,见 §6.2):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<config>
  <plate>
    <metadata key="plater_id" value="1"/>            <!-- 盘号,从 1 起 -->
    <metadata key="plater_name" value=""/>           <!-- 盘命名(可空) -->
    <metadata key="locked" value="false"/>           <!-- 盘是否锁定 -->
    <metadata key="bed_type" value="textured_plate"/><!-- 热床类型(如有) -->
    <metadata key="print_sequence" value="by layer"/><!-- 逐层/逐对象打印 -->
    <metadata key="filament_map_mode" value="Auto For Flush"/>
    <metadata key="filament_maps" value="1 1 1 1"/>  <!-- 逐耗材→挤出机映射 -->
    <metadata key="gcode_file" value="Metadata/plate_1.gcode"/>       <!-- ★ gcode 指针 -->
    <metadata key="thumbnail_file" value="Metadata/plate_1.png"/>
    <metadata key="thumbnail_no_light_file" value="Metadata/plate_no_light_1.png"/>
    <metadata key="top_file" value="Metadata/top_1.png"/>
    <metadata key="pick_file" value="Metadata/pick_1.png"/>
    <metadata key="pattern_bbox_file" value="Metadata/plate_1.json"/>
    <model_instance>                                  <!-- 盘上对象实例(有模型数据时才有) -->
      <metadata key="object_id" value="2"/>
      <metadata key="instance_id" value="0"/>
      <metadata key="identify_id" value="55"/>
    </model_instance>
  </plate>
  <!-- 多盘时依次重复 <plate> 节,plater_id 递增 -->
</config>
```

伴随文件 `Metadata/_rels/model_settings.config.rels` 把每个 G-code 登记为关系(OPC 惯例:部件之间的关系放该部件自己的 `_rels` 子目录):

```xml
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/Metadata/plate_1.gcode" Id="rel-1" Type="http://schemas.snapmaker.com/package/2026/gcode"/>
 <!-- 多盘时每盘一条,Id 递增 -->
</Relationships>
```

### 4.3 `Metadata/slice_info.config` —— 切片结果摘要(XML)

**作用**:每盘切片完成后的"成绩单",供打印机/APP 在不解析 G-code 的情况下直接展示预计耗时、重量、耗材用量、对象清单与切片警告。

**示例**(单盘实测):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<config>
  <header>
    <header_item key="X-SM-Client-Type" value="slicer"/>
    <header_item key="X-SM-Client-Version" value="2.4.0"/>
  </header>
  <plate>
    <metadata key="index" value="1"/>                       <!-- 盘号 -->
    <metadata key="printer_model_id" value="SM_U1"/>        <!-- 机型 ID -->
    <metadata key="nozzle_diameters" value="0.4,0.4,0.4,0.4"/>
    <metadata key="timelapse_type" value="0"/>              <!-- 延时摄影类型,-1 表示不可用 -->
    <metadata key="prediction" value="10541"/>              <!-- 预计耗时,秒 -->
    <metadata key="weight" value="29.42"/>                  <!-- 预计耗材重量,克 -->
    <metadata key="outside" value="false"/>                 <!-- 是否有工具路径越界 -->
    <metadata key="support_used" value="false"/>            <!-- 是否使用支撑 -->
    <metadata key="label_object_enabled" value="false"/>    <!-- 是否启用对象标签 -->
    <metadata key="filament_maps" value="1 1 1 1"/>
    <object identify_id="55" name="立方体" skipped="false"/> <!-- 盘上对象(identify_id 唯一) -->
    <filament id="1" tray_info_idx="1195313935011" type="PLA"
              color="#D9A63A" used_m="5.37" used_g="17.04"/> <!-- 逐耗材用量:米/克 -->
    <warning msg="bed_temperature_too_high_than_filament" level="1" error_code="1000C001"/>
  </plate>
</config>
```

### 4.4 `Metadata/plate_N.json` —— 首层包围盒/标定信息(JSON)

**作用**:记录盘 N 首层的整体与逐对象包围盒、耗材颜色、首层挤出机、热床类型等,供打印机端首层定位、图案标定与图形化提示使用。

**示例**(实测):

```json
{
  "bbox_all": [8.07, 122.5, 149.0, 254.13],        // 整盘首层包围盒 [minX, minY, maxX, maxY]
  "bbox_objects": [                                 // 逐对象首层包围盒
    { "id": 90,   "name": "立方体",     "bbox": [122.0, 122.5, 149.0, 149.5],
      "area": 729.0, "layer_height": 0.24 },
    { "id": 1000, "name": "wipe_tower", "bbox": [8.07, 209.57, 47.93, 254.13],
      "area": 729.0, "layer_height": 0.24 }
  ],
  "bed_type": "textured_plate",
  "filament_colors": ["#D9A63A", "#D9A63A", "#F4E2C1", "#ED1C24"],
  "filament_ids": [0, 1, 2, 3],
  "first_extruder": 1,
  "is_seq_print": false,                            // 是否逐对象打印
  "nozzle_diameter": 0.4,
  "version": 2                                      // 数据结构版本
}
```

### 4.5 其余条件性配置文件

| 文件 | 格式 | 出现条件与作用 |
|---|---|---|
| `Metadata/layer_heights_profile.txt` | 文本 | 对象启用"自定义层高(可变层高)"时;首行 `layer_heights_profile_format_version=2`,其后每对象一行 `object_id=N|z1;h1;z2;h2...` |
| `Metadata/layer_config_ranges.xml` | XML | 对象按 Z 区间设置层高时;`<objects><object id><range min_z max_z><option opt_key>` |
| `Metadata/brim_ear_points.txt` | 文本 | 使用耳形裙边时;首行 `brim_points_format_version=0`,每对象一行 `object_id=N|x y z r ...` |
| `Metadata/custom_gcode_per_layer.xml` | XML | 定义了逐层自定义 G-code(换色/暂停/模板)时;按盘记录 `top_z/type/extruder/color/extra/gcode` |
| `Metadata/cut_information.xml` | XML | 模型执行过"切割"操作时;记录切割面与关联件 |

这些文件**仅在对应功能使用且数据非空时写入**,故普通 gcode.3mf 中一般看不到。

### 4.6 OPC 基础文件

- `[Content_Types].xml`(固定内容,所有导出一致):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
 <Default Extension="png" ContentType="image/png"/>
 <Default Extension="gcode" ContentType="text/x.gcode"/>
</Types>
```

- `_rels/.rels`:声明主模型关系 + 封面缩略图(普通缩略图、中图、小图三条)。
- `3D/3dmodel.model`:gcode.3mf 中仅剩元数据,例:

```xml
<model unit="millimeter" xml:lang="en-US"
       xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
       xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06" requiredextensions="p">
 <metadata name="Application">Snapmaker_Orca-2.4.0</metadata>
 <metadata name="Snapmaker_Orca:3mfVersion">1</metadata>
 <metadata name="Title"></metadata>
 ... (Copyright / CreationDate / Description / Designer / License 等模型级元数据,多为空)
 <resources>
 </resources>
 <build/>
</model>
```

---

## 5. 预设文件(内嵌预设)

当项目中激活了**项目内嵌预设**(常见于从 MakerWorld 等打包工程导入的自定义预设,`PresetBundle::get_current_project_embedded_presets`)时,导出包会在 `Metadata/` 下附带预设原文,命名与含义如下(编号 N 从 1 起、按类型各自递增):

| 文件名 | 表示的预设类型 | 内容 |
|---|---|---|
| `Metadata/machine_settings_N.config` | **打印机预设**(machine) | 该预设的全部打印机参数 |
| `Metadata/process_settings_N.config` | **工艺预设**(process,即打印过程参数) | 层高/壁厚/填充/速度/支撑等 |
| `Metadata/filament_settings_N.config` | **耗材预设**(filament) | 温度/回抽/冷却/耗材适配等 |

> 命名提示:代码中 `process_settings_*` 对应"工艺预设"(历史上也叫打印预设/print preset);`machine_settings_*` 对应打印机预设;`filament_settings_*` 对应耗材预设。另有一个旧前缀 `print_setting_` 仅存在于历史定义,新导出不使用。

**文件内容**(JSON):头部 `name`(预设名)/`version`(预设版本)/`from`(固定 `project`)/`is_custom_defined`,后接该类型全部参数键值,结构同 §4.1:

```json
{
    "name": "0.20mm Standard @Snapmaker U1",
    "version": "1.0.0",
    "from": "project",
    "layer_height": "0.2",
    "wall_loops": "2",
    "sparse_infill_density": "15%",
    "inner_wall_speed": "200",
    "...": "……"
}
```

普通导出(未内嵌预设)的 `.gcode.3mf` 与项目 `.3mf` 中**没有**这些文件。

---

## 6. 标准 3MF 与 `.gcode.3mf` 的关系与区别

### 6.1 三层关系

1. **标准 3MF**(3D Manufacturing Format,3D Consortium 规范):一个基于 OPC 包的**三角形网格交换格式**,主部件为 `3D/3dmodel.model`,定义 `<resources><object><mesh>`(顶点/三角面)与 `<build><item>`(实例摆放)。它只管几何,不懂切片,更没有 G-code 的概念。
2. **项目 `.3mf`**(本软件的工程文件):用标准 3MF 作**容器**,几何按规范存放,同时在 `Metadata/` 里通过 BBS 扩展附加盘结构、配置、缩略图。它是**可编辑、可重切片**的"源文件"。
3. **`.gcode.3mf`**(切片导出产物):同一容器的**只读投递形态**——去掉几何、装入 G-code。它面向打印机与传输场景,软件加载后仅提供预览与参数回读,不可再编辑模型。

三者是"同一容器家族的两种制品":`项目.3mf` 保存"怎么切",`xxx.gcode.3mf` 保存"切出来的结果"。

### 6.2 内容差异对照(实测对比)

| 维度 | 项目 `.3mf` | `.gcode.3mf` |
|---|---|---|
| 网格几何 `3D/3dmodel.model` | ✅ `<object><components>` + `<build><item>`(实例变换) | ❌ 空的 `<resources>`/`<build>`,仅元数据 |
| 分片网格 `3D/Objects/*.model` | ✅ 每对象一个子模型文件 | ❌ 无 |
| `3D/_rels/3dmodel.model.rels` | ✅ 指向各子模型 | ❌ 无 |
| G-code `Metadata/plate_N.gcode(.md5)` | ❌ 无 | ✅ 核心,逐盘一份 |
| 缩略图 `Metadata/plate_*.png` 等 | ✅ | ✅ |
| `Metadata/project_settings.config` | ✅ | ✅(一致) |
| `Metadata/model_settings.config` | `<object>`/`<part>`(矩阵、来源、网格统计)+ `<plate>` + `<assemble>` | 仅 `<plate>` |
| `Metadata/slice_info.config` | 通常仅 `<header>`(未切片) | ✅ 每盘完整摘要 |
| `Metadata/plate_N.json` | 切片后才有 | ✅ |
| `Auxiliaries/` 嵌入资源 | 可能有 | 可能有 |
| 保存策略(SaveStrategy) | `SplitModel \| ShareMesh \| FullPathSources` | `SplitModel \| WithGcode \| SkipModel \| Silence` |
| 用途 | 编辑/协作/备份 | 发送到打印机、U 盘拷贝、上传 |

项目 `.3mf` 的主模型示例(可见真实几何与实例变换):

```xml
<resources>
 <object id="2" p:UUID="..." type="model">
  <components>
   <component p:path="/3D/Objects/圆柱体_1.model" objectid="1" transform="1 0 0 0 1 0 0 0 1 0 0 0"/>
  </components>
 </object>
</resources>
<build p:UUID="...">
 <item objectid="2" transform="1 0 0 0 1 0 0 0 1 135.5 136 13.5" printable="1"/>
</build>
```

### 6.3 为什么会出现 `.gcode.3mf`

- **单一文件、一次传输**:打印机/U 盘/APP 需要一个自足的文件同时携带 G-code、缩略图、元数据(耗时/重量/耗材)与完整参数;裸 `.gcode` 虽在注释块里带缩略图与配置,但无法承载多盘、无结构化校验、扩展性差。
- **多盘任务的自然容器**:多盘打印(一盘一刀)需要把 N 份 G-code 连同各自的预览与摘要统一打包,并保持逐盘独立可取;OPC 包 + 关系文件天然满足"一个包、多个部件、按关系索引"。
- **复用 3MF/OPC 生态**:沿用 3MF 容器后,通用 3MF 工具能识别包骨架与缩略图;自家读取端则通过 `[Content_Types].xml` 中声明的 `gcode` 扩展与自定义 Relationship 类型定位打印数据——扩展规范而不破坏规范。
- **可回读、可复切**:保留 `project_settings.config` 与切片摘要,用户把 `.gcode.3mf` 拖回软件即可预览并恢复当时参数重新切片(加载端检测到模型为空、含 gcode 关系时进入 gcode.3mf 只读模式)。
- **完整性校验**:每盘 MD5 随包携带,传输后可验证 G-code 未损坏。

一句话:**`.gcode.3mf` = 3MF 容器 + BBS/Snapmaker 扩展 + "以 G-code 为核心的切片产物集"**,它是标准 3MF 在 3D 打印"最后一公里"上的工程化延伸,而不是一个新的通用标准。

---

## 7. 补充约定

### 7.1 压缩与容量

- 归档为标准 ZIP;文本/XML/JSON/G-code 使用 deflate 压缩,PNG/JPG 等已是压缩格式的内容以**存储方式**(不二次压缩)写入。
- 默认启用 **Zip64**,单个 G-code 条目可超过 4 GiB(实现上限 16 GiB),支持超长大件。

### 7.2 版本与命名空间兼容

- 版本键:`3D/3dmodel.model` 中 `Snapmaker_Orca:3mfVersion`(当前值 `1`)。读取端同时兼容历史键 `BambuStudio:3mfVersion`、`bamboo_slicer:Version3mf`。
- Relationship 类型:新版导出使用 `http://schemas.snapmaker.com/package/2026/gcode` 与 `.../cover-thumbnail-middle|small`;读取端对 `schemas.bambulab.com` 与 `schemas.snapmaker.com` 前缀**均按后缀匹配接受**(如 `.../package/2021/gcode` 的 Bambu 历史文件可正常读取)。这些 URI 仅为 OPC 标识符,不会联网解析。
- `Application` 元数据标识生成器,如 `Snapmaker_Orca-2.4.0`、`BambuStudio-2.3.5`,用于来源追溯。

### 7.3 阅读与解析建议(面向工具开发者)

1. 按普通 ZIP 解包;先读 `[Content_Types].xml` 确认类型声明,再读 `_rels/.rels` 找到主模型与封面图。
2. 盘清单解析 `Metadata/model_settings.config` 的 `<plate>` 节;需要 gcode 时优先走 `Metadata/_rels/model_settings.config.rels`(比正则猜测文件名更可靠)。
3. 展示信息取 `Metadata/slice_info.config`;参数回读取 `Metadata/project_settings.config`;首层定位取 `Metadata/plate_N.json`。
4. 使用 G-code 前校验 `plate_N.gcode.md5`。
5. 对缺失文件保持容忍:几何、预设、条件性配置都可能不存在,以关系文件与 `model_settings.config` 为准,而非假定固定文件集。
