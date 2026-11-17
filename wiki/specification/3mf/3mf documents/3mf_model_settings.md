# model_settings.config：对象与打印板信息

← [Wiki 首页](../../../home.md)

> 3mf 里必有的一份 XML：每个对象叫什么、怎么摆、在哪块打印板上。实测证据见 [研发内部资料](../../../../docs/)。

## 目录

- [它是什么](#它是什么)
- [四个概念怎么联系起来：两块盘、三只鸭子](#四个概念怎么联系起来两块盘三只鸭子)
- [两侧对照：几何侧与属性侧](#两侧对照几何侧与属性侧)
- [参数覆盖优先级](#参数覆盖优先级)
- [易混点速查](#易混点速查)

## 它是什么

`Metadata/model_settings.config`，一个 XML 文件，描述几何之外的"业务信息"。内容分四层：

| 层 | 源码对应 | 管什么 | 固定内容 |
|---|---|---|---|
| object（对象） | `ModelObject` | 一个可整体操作的模型 | 名称、耗材槽；可按需覆盖全局参数 |
| part（零件） | `ModelVolume` | 对象内部的组成件 | 位置矩阵、来源文件、网格统计；也可覆盖参数 |
| plate（打印板） | —（工程级概念，不属对象侧类） | 一块打印板的布局 | 板名、耗材映射、缩略图文件名 |
| model_instance（实例） | `ModelInstance` | 对象的每次摆放 | 对象编号、实例编号、identify_id（不透明标识） |

对象的编号与主模型 `3D/3dmodel.model` 里的编号一一对应——那边管几何，这边管属性。

**part 在代码里叫 volume**：这层最容易名字对不上——文件侧是对象节下的 `<part>`，源码侧是 `ModelVolume`（字面"体积"，同一东西的两副名字）。写入时对象内的 volume 按顺序逐个落成 `<part>`，读取时反向重建。part 层元数据的 `source_volume_id` 键名用的就是代码侧叫法；对象/零件两层的参数覆盖，序列化的正是源码里 `ModelObject::config` / `ModelVolume::config` 这两级配置。

## 四个概念怎么联系起来：两块盘、三只鸭子

设想一个最小的工程：一只"小鸭子"（身体 + 嘴两个零件），在盘 1 摆了两只、盘 2 摆了一只。

**打印现场**——三个实例都是同一个对象的"摆放副本"，几何只有一份：

```text
盘 1 ════════════════════════════════════════════════════
      [实例 #0 小鸭子 · 旋转 30°]      [实例 #1 小鸭子 · 原姿态]
盘 2 ════════════════════════════════════════════════════
      [实例 #2 小鸭子 · 放大 1.2×]
══════════════════════════════════════════════════════════
                        │
                        ▼
      对象「小鸭子」 id=1  ← 切片软件对象列表里的一项
        ├─ part 0「身体」 subtype=model_part   ← 零件：对象的组成件
        └─ part 1「嘴」   subtype=model_part
```

**基数关系**：

```text
盘 plate ──含 0..N──▶ 实例 instance ──摆放自──▶ 对象 object ──由 1..N 组成──▶ 零件 part
（一块物理板）        （对象的一次摆放）        （可整体操作的模型）      （对象内的网格件）
```

- **对象 → 零件**：一对多（组合）。零件不能脱离对象单独存在。
- **对象 → 实例**：一对多（摆放）。摆 3 次就有 3 个实例，几何只存一份。
- **实例 → 盘**：每个实例归属且仅归属一块盘；同一对象的实例可以分到不同盘上。
- **盘 ↔ 对象**：没有直接连线——全靠实例中转。盘里有什么，看盘节下挂了哪些 `<model_instance>`。

## 两侧对照：几何侧与属性侧

这四个概念都是"双面"的：空间信息（长什么样、摆在哪）在 `3D/3dmodel.model`，业务信息（叫什么、怎么切、在哪块板）在本文件。同一只小鸭子，两侧分别长这样（精简示意，`←` 注释为讲解所加）：

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
  <object id="3" type="model"><mesh>…嘴的顶点与三角形…</mesh></object>    ←（外拆形态放在 3D/Objects/）
</resources>
<build>
  <item objectid="1" transform="…"/>           ← 实例 #0 在板上的位置（每个实例一条）
  <item objectid="1" transform="…"/>           ← 实例 #1
</build>
```

属性侧 `Metadata/model_settings.config`：

```xml
<config>
  <!-- ══ 对象节：每个对象一条，id 与几何侧同号挂钩 ══ -->
  <object id="1">
    <metadata key="name" value="小鸭子"/>        ← 对象名（对象列表显示的）
    <metadata key="extruder" value="2"/>         ← 这个对象默认用 2 号耗材槽
    <metadata key="wall_loops" value="3"/>       ← 对象级参数覆盖（全局是 2，这里改 3）

    <!-- ── 零件节：挂在所属对象下面 ── -->
    <part id="0" subtype="model_part">
      <metadata key="name" value="身体"/>
      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>  ← 零件在对象内的摆放（4×4）
      <metadata key="source_file" value="duck.stl"/>    ← 来源追溯 6 键（原文件/原 volume 编号/偏移）
      <metadata key="source_object_id" value="1"/>
      <metadata key="source_volume_id" value="0"/>
      <metadata key="source_offset_x" value="0"/>       ← x/y/z 三键各一条，此处省略 y/z
      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0"
                 parts_removed="0" backwards_edges="0"/> ← 网格体检报告
    </part>
    <part id="1" subtype="model_part">
      <metadata key="name" value="嘴"/>
      <metadata key="extruder" value="1"/>       ← 零件级覆盖：嘴单独用 1 号槽（多色打印就靠这）
    </part>
  </object>

  <!-- ══ 盘节：每块打印板一条 ══ -->
  <plate>
    <metadata key="plater_id" value="1"/>        ← 盘号，与 plate_1.png 的 1 对应
    <metadata key="plater_name" value="第一板"/>
    <metadata key="filament_maps" value="1;1"/>  ← 现状恒写全 1，勿当真实映射（Q12）
    <metadata key="thumbnail_file" value="Metadata/plate_1.png"/>

    <!-- ── 实例节：这块板上摆了"哪个对象的哪一次摆放" ── -->
    <model_instance>
      <metadata key="object_id" value="1"/>      ← 指 <object id="1"> 小鸭子
      <metadata key="instance_id" value="0"/>    ← 对象内第 0 次摆放
      <metadata key="identify_id" value="31"/>   ← 不透明标识，勿按下标解释
    </model_instance>
    <model_instance>
      <metadata key="object_id" value="1"/>
      <metadata key="instance_id" value="1"/>
      <metadata key="identify_id" value="32"/>
    </model_instance>
  </plate>
</config>
```

### 编号挂钩关系

| 概念 | 几何侧 | 属性侧 | 挂钩方式 |
|---|---|---|---|
| 对象 | `<object id=N>`（多零件时为 components 组合） | `<object id=N>` | 同 id 一一对应，两侧编号不应各自重排 |
| 零件 | component 引用的网格 `<object>` | 父对象节下的 `<part>` | 零件在对象内的摆放两侧各写一份：component 的 3×4 `transform`、part 的 4×4 `matrix`，矩阵形态不同，解析不应混用 |
| 实例 | `<build><item>` 的 objectid + 对象内顺序 | `<model_instance>` 的 object_id + instance_id | 空间变换在几何侧，归属哪块盘在属性侧 |
| 盘 | 没有（3MF Core 只有 build，无盘概念） | `<plate>` 节 | 盘号只存在于 `plater_id` 与 `plate_N` 资源命名 |

## 参数覆盖优先级

对象可以覆盖 [project_settings.config](3mf_project_settings.md) 里的参数，零件还可以再覆盖对象。实测同一个参数（如 `wall_loops`）同时出现在对象层和零件层，**优先级是 零件 > 对象 > 全局**——但这条规则只存在于读取代码的逻辑里，文件本身没有任何声明。写解析工具时必须按这个隐含规则处理。

覆盖是**稀疏**的，只写差异键：某个参数只有在这一层改过，才会写进 model_settings.config 的对应节点；某层没出现这个 key ≠ 值为空，而是"没改，沿用上一级"。取一个参数生效值的完整过程：

1. 零件层有这个 key → 用零件的值（例：嘴的 `extruder=1`）；
2. 零件层没有 → 看对象层，对象层有 → 用对象的值（例：身体没写 `extruder`，沿用对象的 `2`）；
3. 两层都没写 → 用 [project_settings.config](3mf_project_settings.md) 的全局值（例：都没改 `layer_height`，用全局）。

```text
project_settings.config     全局默认（约 580 键，全量）
        ▲ 覆盖①（只写差异键）
<object> 节的 metadata      "这一参数对这个对象改"
        ▲ 覆盖②（只写差异键，更内层）
<part> 节的 metadata        "只对这个零件改"（例：嘴单独换耗材槽）

生效值 = part > object > project（零件 > 对象 > 全局）
```

## 易混点速查

1. **几何侧 `<object>` 个数 ≠ 属性侧 `<object>` 个数**——每个零件网格在 3dmodel.model 里也是一个 object（如上例 id=2/3），但属性侧只给"可整体操作的对象"开 object 节，零件信息全在 part 节里。
2. `<plate>` 元素本身没有 id 属性，盘号在 `plater_id` 元数据里。
3. `identify_id` 是不透明标识，不应按数组下标解释；`filament_maps` 现状恒写全 `1`（Q12）。
4. 同一对象跨盘 = 实例分到不同 plate 节，不是几何复制。
5. `<assemble>` 节（装配视图）条件写入，实测 9 个样本 0 次出现（Q4），普通文件见不到。
6. **代码的 volume = 文件的 part**：读源码按 `ModelVolume` 找、读文件按 `<part>` 找，是同一个东西；`source_volume_id` 等键名保留代码侧叫法。

## 深入阅读（研发内部资料）

- 三层字段实测盘点：[03-现状盘点-model_settings与嵌入预设](../../../../docs/03-现状盘点-model_settings与嵌入预设.md)
- 待团队裁决问题（含 `module` key、`assemble` 节、plate 条件 key）：[04-问题清单-切片软件团队对齐](../../../../docs/04-问题清单-切片软件团队对齐.md)
- 规范级定义：[3mf 工程文件规范](../3mf_standard.md) [§5.2 对象、组件与实例](../3mf_standard.md#52-对象组件与实例)、[§6.1 对象与盘索引](../3mf_standard.md#61-对象与盘索引metadatamodel_settingsconfig)
