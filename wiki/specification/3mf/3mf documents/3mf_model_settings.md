# model_settings.config：对象与打印板信息

← [Wiki 首页](../../../home.md)

> 工程文件必选的 XML 部件：记录对象、零件、打印板与实例的业务属性。

## 目录

- [前言](#前言)
- [引言](#引言)
- [1 范围](#1-范围)
- [2 术语和定义](#2-术语和定义)
- [3 概念关系图解](#3-概念关系图解)
  - [3.1 实例布局与对象构成](#31-实例布局与对象构成)
  - [3.2 基数关系](#32-基数关系)
- [4 两侧对照：几何侧与属性侧](#4-两侧对照几何侧与属性侧)
  - [4.1 几何侧](#41-几何侧)
  - [4.2 属性侧](#42-属性侧)
  - [4.3 编号对应关系](#43-编号对应关系)
- [5 键清单：按写入行为分类](#5-键清单按写入行为分类)
- [6 参数覆盖优先级](#6-参数覆盖优先级)
- [7 易混淆要点速查](#7-易混淆要点速查)
- [附录（资料性）深入阅读](#附录资料性深入阅读)

## 前言

本文讲解工程 `.3mf` 的必选部件 `Metadata/model_settings.config`。对象与零件的命名及参数覆盖、实例的打印板归属、打印板的布局信息，均记录于该文件。

逐键定义与一致性要求见 [3mf 工程文件规范](../3mf_standard.md) 6.1～6.2；本文为该规范的图解配套文档，两者不一致时以规范为准。

## 引言

恢复一个切片工程，仅有几何并不足够：`3D/3dmodel.model` 仅描述对象的几何构成与摆放变换；对象的名称与耗材槽分配、实例的打印板归属等业务属性均由本文件描述。对象的编号与主模型一一对应：几何侧描述形状与摆放，属性侧描述业务信息。

四层职责概述：object 节描述对象（名称、耗材槽、参数覆盖），part 节描述零件（位置矩阵、来源追溯、网格统计），plate 节描述打印板（板名、耗材映射、缩略图），model_instance 节登记实例摆放（对象编号、实例编号、不透明标识）。

本文第 1 章划定范围；第 2～4 章建立概念（术语定义、图解、两侧对照）；第 5～6 章说明键的写入行为与参数覆盖机制；第 7 章汇总易混淆要点；深入阅读入口见文末附录。

## 1 范围

本文阐述 `Metadata/model_settings.config` 的四层结构、与几何侧的编号对应关系、键的写入行为分类与参数覆盖优先级，并汇总常见误读。

本文适用于初次接触 3mf 内部结构、需要读取或解析该文件的读者。

本文不涉及：几何侧模型部件的格式细节（见 [3mf 工程文件规范](../3mf_standard.md) 第 5 章）、全局参数文件的字段级说明（见 [project_settings.config：全局打印设置](3mf_project_settings.md)）、逐键规范表与一致性要求（见规范 6.1 与第 8 章）。

## 2 术语和定义

| 层 | 源码对应 | 职责 | 典型内容 |
|---|---|---|---|
| object（对象） | `ModelObject` | 一个可整体操作的模型 | 名称、耗材槽；可按需覆盖全局参数 |
| part（零件） | `ModelVolume` | 对象内部的组成件 | 位置矩阵、来源追溯、网格统计；同样支持参数覆盖 |
| plate（打印板） | —（工程级概念，不属对象侧类） | 一块打印板的布局 | 板名、耗材映射、缩略图文件名 |
| model_instance（实例） | `ModelInstance` | 对象的每次摆放 | 对象编号、实例编号、identify_id（不透明标识） |

**part 在源码中称为 volume**：该层命名最易混淆——文件侧为对象节下的 `<part>`，源码侧为 `ModelVolume`（字面义为"体积"，指同一实体）。写入时，对象内的 volume 按顺序逐个序列化为 `<part>`；读取时反向重建。part 层元数据的 `source_volume_id` 键名即沿用代码侧命名；对象/零件两层的参数覆盖，序列化的正是源码中 `ModelObject::config` / `ModelVolume::config` 两级配置。

## 3 概念关系图解

以一个最小工程为例：对象「小鸭子」由两个零件（身体、嘴）组成，在打印板 1 摆放两个实例、打印板 2 摆放一个实例。

### 3.1 实例布局与对象构成

三个实例均为同一对象的摆放副本，几何数据仅存储一份：

```text
盘 1 ════════════════════════════════════════════════════
      [实例 #0 小鸭子 · 旋转 30°]      [实例 #1 小鸭子 · 原姿态]
盘 2 ════════════════════════════════════════════════════
      [实例 #2 小鸭子 · 放大 1.2×]
══════════════════════════════════════════════════════════
                        │
                        ▼
      对象「小鸭子」 id=1  ← 切片软件对象列表中的一项
        ├─ part 0「身体」 subtype=normal_part  ← 零件：对象的组成件
        └─ part 1「嘴」   subtype=normal_part
```

### 3.2 基数关系

```text
盘 plate ──含 0..N──▶ 实例 instance ──摆放自──▶ 对象 object ──由 1..N 组成──▶ 零件 part
（一块物理板）        （对象的一次摆放）        （可整体操作的模型）      （对象内的网格件）
```

- **对象 → 零件**：一对多（组合）。零件不能脱离对象独立存在。
- **对象 → 实例**：一对多（摆放）。摆放 3 次即产生 3 个实例，几何仅存一份。
- **实例 → 盘**：每个实例归属且仅归属一块打印板；同一对象的实例可分属不同打印板。
- **盘 ↔ 对象**：无直接关联，均通过实例建立联系。打印板包含哪些对象，取决于盘节下登记的 `<model_instance>`。

## 4 两侧对照：几何侧与属性侧

这四个概念均为双面结构：空间信息（几何形状、摆放位置）记录于 `3D/3dmodel.model`，业务信息（名称、切片参数、打印板归属）记录于本文件。同一对象在两侧的表示如下（精简示意，`←` 注释为讲解所加）：

### 4.1 几何侧

几何侧 `3D/3dmodel.model`：

```xml
<resources>
  <object id="1" type="model">                 ← 对象「小鸭子」：多零件 → 用组件引用表达
    <components>
      <component objectid="2" transform="…"/>   ← 身体在对象内的摆放（3×4）
      <component objectid="3" transform="…"/>   ← 嘴在对象内的摆放（3×4）
    </components>
  </object>
  <object id="2" type="model"><mesh>…身体的顶点与三角形…</mesh></object>  ← 零件网格本体
  <object id="3" type="model"><mesh>…嘴的顶点与三角形…</mesh></object>    ←（外拆形态存放于 3D/Objects/）
</resources>
<build>
  <item objectid="1" transform="…"/>           ← 实例 #0 在板上的位置（每个实例一条）
  <item objectid="1" transform="…"/>           ← 实例 #1
</build>
```

### 4.2 属性侧

属性侧 `Metadata/model_settings.config`：

```xml
<config>
  <!-- ══ 对象节：每个对象一条，id 与几何侧同号对应 ══ -->
  <object id="1">
    <metadata key="name" value="小鸭子"/>        ← 对象名（对象列表中显示）
    <metadata key="extruder" value="2"/>         ← 该对象默认使用 2 号耗材槽
    <metadata key="wall_loops" value="3"/>       ← 对象级参数覆盖（全局值为 2，此处改为 3）

    <!-- ── 零件节：隶属于所属对象 ── -->
    <part id="0" subtype="normal_part">
      <metadata key="name" value="身体"/>
      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>  ← 零件在对象内的摆放（4×4）
      <metadata key="source_file" value="duck.stl"/>    ← 来源追溯 6 键（原文件/原 volume 编号/偏移）
      <metadata key="source_object_id" value="1"/>
      <metadata key="source_volume_id" value="0"/>
      <metadata key="source_offset_x" value="0"/>       ← x/y/z 三键各一条，此处省略 y/z
      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0"
                 facets_reversed="0" backwards_edges="0"/> ← 网格修复统计
    </part>
    <part id="1" subtype="normal_part">
      <metadata key="name" value="嘴"/>
      <metadata key="extruder" value="1"/>       ← 零件级覆盖：嘴单独使用 1 号耗材槽（多色打印依赖此机制）
    </part>
  </object>

  <!-- ══ 盘节：每块打印板一条 ══ -->
  <plate>
    <metadata key="plater_id" value="1"/>        ← 盘号，与 plate_1.png 的 1 对应
    <metadata key="plater_name" value="第一板"/>
    <metadata key="filament_maps" value="1;1"/>  ← 现状恒写全 1，不应作为真实映射使用
    <metadata key="thumbnail_file" value="Metadata/plate_1.png"/>

    <!-- ── 实例节：登记该板包含的对象实例 ── -->
    <model_instance>
      <metadata key="object_id" value="1"/>      ← 指 <object id="1"> 小鸭子
      <metadata key="instance_id" value="0"/>    ← 对象内第 0 次摆放
      <metadata key="identify_id" value="31"/>   ← 不透明标识，不应按数组下标解释
    </model_instance>
    <model_instance>
      <metadata key="object_id" value="1"/>
      <metadata key="instance_id" value="1"/>
      <metadata key="identify_id" value="32"/>
    </model_instance>
  </plate>
</config>
```

### 4.3 编号对应关系

| 概念 | 几何侧 | 属性侧 | 对应方式 |
|---|---|---|---|
| 对象 | `<object id=N>`（多零件时为 components 组合） | `<object id=N>` | 同 id 一一对应，两侧编号不应各自重排 |
| 零件 | component 引用的网格 `<object>` | 父对象节下的 `<part>` | 零件在对象内的摆放两侧各写一份：component 的 3×4 `transform`、part 的 4×4 `matrix`，矩阵形态不同，解析不应混用 |
| 实例 | `<build><item>` 的 objectid + 对象内顺序 | `<model_instance>` 的 object_id + instance_id | 空间变换在几何侧，归属哪块盘在属性侧 |
| 盘 | 没有（3MF Core 只有 build，无盘概念） | `<plate>` 节 | 盘号只存在于 `plater_id` 与 `plate_N` 资源命名 |

## 5 键清单：按写入行为分类

各层的键按写入行为分为三类（以序列化代码 `src/libslic3r/Format/bbs_3mf.cpp` 为准，逐键表见规范 [§6.1](../3mf_standard.md#611-对象层与零件层键按写入行为分类)）：

| 类 | 含义 | 各层包含的键 |
|---|---|---|
| **恒写键** | 每次保存必落盘 | part：`id` / `subtype` / `matrix` / `mesh_stat`；plate：`plater_id` / `plater_name` / `locked` / `filament_map_mode` / `filament_maps`；instance：`object_id` / `instance_id` / `identify_id` |
| **条件键** | 满足条件才写 | 各层 `name`（非空才写）；part 来源 6 键（有来源文件才整组写）、`merged_group_id`（存在合并组时才写）；plate 的缩略图等资源键（文件存在才写） |
| **差异键** | 修改后才保存 | object / part 的参数覆盖键——机制见第 6 章 |

两点常见误解：

- **对象层没有任何恒写的 metadata 键**。实测对象层必现的 `extruder` 属差异键——料槽分配机制总会将其写入对象配置，并非代码硬编码。
- `subtype` 的取值为 `normal_part` / `negative_part` / `modifier_part` / `support_enforcer` / `support_blocker`，不存在 `model_part` 取值。

## 6 参数覆盖优先级

对象可覆盖 [project_settings.config](3mf_project_settings.md) 中的参数，零件可进一步覆盖对象。实测同一参数（如 `wall_loops`）可同时出现在对象层与零件层，**优先级为 零件 > 对象 > 全局**——该规则仅存在于读取代码的逻辑中，文件本身没有任何声明。编写解析工具时必须按此隐含规则处理。

覆盖是**稀疏**的，仅写差异键：参数仅在该层被修改后才写入 model_settings.config 的对应节点；某层未出现该 key ≠ 值为空，而是"未修改，沿用上一级"。参数生效值的取值过程：

1. 零件层存在该 key → 取零件的值（例：嘴的 `extruder=1`）；
2. 零件层不存在 → 查对象层，对象层存在 → 取对象的值（例：身体未写 `extruder`，沿用对象的 `2`）；
3. 两层均未写 → 取 [project_settings.config](3mf_project_settings.md) 的全局值（例：均未修改 `layer_height`，取全局值）。

```text
project_settings.config     全局默认（约 580 键，全量）
        ▲ 覆盖①（只写差异键）
<object> 节的 metadata     "该参数在该对象上被修改"
        ▲ 覆盖②（只写差异键，更内层）
<part> 节的 metadata    "该参数仅在该零件上被修改"（例：嘴单独更换耗材槽）

生效值 = part > object > project（零件 > 对象 > 全局）
```

## 7 易混淆要点速查

1. **几何侧 `<object>` 个数 ≠ 属性侧 `<object>` 个数**——每个零件网格在 3dmodel.model 中也是一个 object（如上例 id=2/3），但属性侧仅为"可整体操作的对象"开设 object 节，零件信息均记录于 part 节。
2. `<plate>` 元素本身没有 id 属性，盘号记录于 `plater_id` 元数据。
3. `identify_id` 是不透明标识，不应按数组下标解释；`filament_maps` 现状恒写全 `1`。
4. 同一对象跨盘 = 实例分属不同 plate 节，并非几何复制。
5. `<assemble>` 节（装配视图）条件写入，实测 9 个样本 0 次出现，常规文件中不会出现。
6. **代码的 volume = 文件的 part**：读源码按 `ModelVolume` 查找、读文件按 `<part>` 查找，二者为同一实体；`source_volume_id` 等键名沿用代码侧命名。

## 附录（资料性）深入阅读

- 规范级定义：[3mf 工程文件规范](../3mf_standard.md) [§5.2 对象、组件与实例](../3mf_standard.md#52-对象组件与实例)、[§6.1 对象与盘索引](../3mf_standard.md#61-对象与盘索引metadatamodel_settingsconfig)
