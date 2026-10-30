# Snapmaker Orca 3mf 规范 0\.9\.9

版本：0\.9\.9　｜　适用软件：Snapmaker Orca 2\.4\.1　｜　更新日期：2026\-10\-27

本文定义 Snapmaker Orca 工程 3MF 的文件结构、几何对象、打印配置及工程附加数据，供工程文件的导入、编辑和保存使用。

配套文档：[Snapmaker Orca gcode\.3mf规范0\.9\.9](https://snapmaker.feishu.cn/docx/GsfJd2gz2ofcl0xxdMEcgHiRnib) · [Snapmaker Orca gcode规范 0\.9\.9](https://snapmaker.feishu.cn/docx/OQ3td0sp8owdI1xXXGzcNcLhnUA)

# 概述

工程 3MF 保存的是“模型如何摆放、使用什么参数切片”。它可以包含多个模型、多个实例和多个打印盘。文件采用 ZIP 打包并启用 ZIP64，条目采用 Store（不压缩）或 Deflate（压缩）：几何使用 3MF 的 XML 结构，切片参数和编辑信息保存在 Metadata 目录。

|文件|保存内容|主要用途|
|---|---|---|
|\*\.3mf|几何、摆放、配置和编辑信息|打开工程、修改参数、重新切片|
|\*\.gcode\.3mf|已切片 G\-code、盘信息和预览资源|交给设备选择打印盘并打印|
|\*\.gcode|已经展开的指令文本|由对应机型固件逐行执行|

本规范中的“必选”指普通工程保存文件中的必要内容；“可选”指仅在工程包含相应数据时出现。配置\-only 包和备份包可能省略部分内容。

# 文件组织

```text
工程.3mf
├── [Content_Types].xml
├── _rels/.rels
├── 3D/
│   ├── 3dmodel.model
│   ├── _rels/3dmodel.model.rels       （拆分模型时）
│   └── Objects/*.model              （拆分模型时）
├── Metadata/
│   ├── model_settings.config
│   ├── project_settings.config
│   ├── process_settings_K.config    （可选）
│   ├── filament_settings_K.config   （可选）
│   ├── machine_settings_K.config    （可选）
│   ├── layer_heights_profile.txt    （可选）
│   ├── layer_config_ranges.xml      （可选）
│   ├── custom_gcode_per_layer.xml   （可选）
│   └── 其他工程资源
└── Auxiliaries/                     （可选）
```

|文件|内容格式|是否必选|作用|
|---|---|---|---|
|\[Content\_Types\]\.xml|XML|是|记录部件的媒体类型|
|\_rels/\.rels|XML|是|指向主模型和封面图|
|3D/3dmodel\.model|3MF XML|是|几何对象、组件关系和实例|
|3D/Objects/\*\.model|3MF XML|条件必选|拆分保存的几何，由主模型引用|
|Metadata/model\_settings\.config|XML|是|对象、部件、盘、实例和装配信息|
|Metadata/project\_settings\.config|JSON|保存完整配置时|工程使用的配置快照|
|三类 \*\_settings\_K\.config|JSON|否|工程内嵌的工艺、耗材、机器预设|
|Auxiliaries/\*\*|按资源类型|否|封面、图片及其他附加资料|

K 是同类内嵌预设文件的编号，不是盘号或料槽号。文件名中没有 config\_setting 或 config\_settings\.config；讨论中的“配置文件”通常指 project\_settings\.config 或上述三类预设文件。

## 路径与关系

表中的 object@id 表示 object 节点的 id 属性；斜杠表示子节点路径。

ZIP 条目名不带开头的斜杠，例如 3D/3dmodel\.model；XML 关系中的 /3D/3dmodel\.model 表示包内绝对路径。相对路径从关系所属部件的目录计算。

```xml
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rel-1"
    Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"
    Target="/3D/3dmodel.model"/>
</Relationships>
```

读取时通过关系定位目标文件，关系的 Type 是标识字符串，不是需要访问的网址。仅识别文件名不能替代关系解析。

# 模型、部件与实例

一个模型对象可以由多个部件组成，也可以在打印盘上放置多个实例。部件保存几何；实例保存摆放位置。多个实例可以共用同一份几何。

|概念|对应结构|例子|
|---|---|---|
|几何部件|object/mesh|模型的主体或一个修改器网格|
|组合对象|object/components|由主体和若干部件组成的模型|
|摆放实例|build/item|同一个模型在盘上复制出的两个位置|

|字段|类型 / 单位|出现条件|说明与示例|
|---|---|---|---|
|model@unit|枚举|模型根节点|基线写 millimeter，几何单位为 mm|
|model@requiredextensions|空格分隔文本|使用扩展时|p 表示使用 Production 扩展，支持跨文件组件等结构|
|object@id|正整数|每个资源对象|在所属 \.model 文件中唯一|
|object@type|枚举|可省略|当前几何通常写 model|
|vertex@x / y / z|浮点数 / 模型单位|每个顶点|顶点坐标；可采用小数或科学计数法|
|triangle@v1 / v2 / v3|整数|每个三角面|本 mesh 的顶点下标，从 0 开始|
|component@objectid|正整数|组件引用|被引用对象的 id|
|component@p:path|包内路径|跨文件组件|被引用对象所在的 \.model 文件|
|component@transform|12 个浮点数|存在部件变换时|部件的旋转、缩放和平移|
|item@objectid|正整数|每个实例|本实例引用的对象|
|item@transform|12 个浮点数|存在实例变换时|实例在模型坐标系中的摆放|
|item@printable|布尔文本|当前导出写入|厂商历史属性，记录实例是否参与打印|
|p:UUID|UUID 字符串|使用 Production 扩展时|身份追踪标识；2\.4\.1 部分值固定，不宜作为跨任务唯一 ID|

```xml
<object id="2" type="model">
  <components>
    <component objectid="1"
      p:path="/3D/Objects/object_1.model"
      transform="1 0 0 0 1 0 0 0 1 0 0 0"/>
  </components>
</object>
<build>
  <item objectid="2"
    transform="1 0 0 0 1 0 0 0 1 20 30 0"/>
</build>
```

## 坐标与变换

3MF 使用右手坐标系。单位由 model@unit 指定；当前导出的单位是毫米。12 个数的最后三个是平移量，不要与 model\_settings 中的 16 数矩阵混用。

```text
变换文本：a b c d e f g h i j k l
x' = a*x + d*y + g*z + j
y' = b*x + e*y + h*z + k
z' = c*x + f*y + i*z + l

单位变换：1 0 0 0 1 0 0 0 1 0 0 0
```

组合模型先应用部件变换，再应用外层组件和实例变换。对象 id 只在所属模型文件中唯一，跨文件引用应同时记录“文件路径 \+ 对象 id”。

## 模型基本信息

|字段|类型 / 单位|出现条件|说明与示例|
|---|---|---|---|
|Application|文本|主模型 metadata|创建软件，如 Snapmaker\_Orca\-2\.4\.1|
|Title / Designer / Description|文本|有相应资料时|模型标题、设计者和说明|
|Copyright / License|文本|有相应资料时|版权及厂商保存的许可说明|
|CreationDate / ModificationDate|文本|当前可为空|创建、修改日期；当前导出可能为空|
|Snapmaker\_Orca:3mfVersion|整数字符串|模型 metadata|当前写 1；这是模型格式标识，不是软件版本|

# 工程配置

project\_settings\.config 的扩展名虽然是 \.config，内容实际是 JSON。model\_settings\.config 和 slice\_info\.config 则是 XML，不能仅凭扩展名选择解析器。

```json
{
  "version": "2.4.1",
  "name": "project_settings",
  "from": "project",
  "project_schema_version": "1",
  "layer_height": "0.2",
  "enable_support": "1",
  "nozzle_temperature": [
    "200",
    "220"
  ],
  "printable_area": [
    "0x0",
    "270x0",
    "270x270",
    "0x270"
  ]
}
```

|参数类型|JSON 中的写法|读取方式|
|---|---|---|
|整数、浮点数|"3"、"0\.2"|先读字符串，再按参数含义转换成数字|
|布尔值|"0"、"1"|0 表示关闭，1 表示开启；不是 JSON true/false|
|百分比|"15%"、"120%"|保留 %；不能与绝对数值混同|
|枚举|"klipper"、"by layer"|按完整枚举文本识别，不使用 C\+\+ 内部编号|
|数值或枚举数组|\["200","220"\]|数组元素仍是字符串；下标含义由具体字段决定|
|文本、多行 G\-code|JSON 字符串|按 JSON 解码一次，保留解码后的换行和原文|
|单点 / 点列表|"10,20" / \["0x0","270x0"\]|单点通常用逗号；点列表的每个元素用 x 分隔|
|允许空值的数值数组|数组中可能出现 "nil"|nil 表示没有覆盖值，不等于 0；只有定义为可空的字段允许|

|字段|类型 / 单位|出现条件|说明与示例|
|---|---|---|---|
|version|字符串|有配置时|写出配置的软件版本，如 2\.4\.1|
|name|字符串|有配置时|工程快照为 project\_settings；内嵌预设为预设名称|
|from|字符串|有配置时|本导出路径写 project|
|project\_schema\_version|整数字符串|按配置保存|当前为 "1"，表示工程配置结构版本|

## 工程快照与内嵌预设

project\_settings\.config 保存工程当时使用的参数。三类内嵌预设用于恢复预设名称、来源和继承关系，可能只包含相对父预设的差异，不一定是完整参数集。恢复工程时按各自用途读取，不能把 ZIP 中最后一个配置文件当作最终配置。

对象、部件和高度范围还可以保存局部参数。局部参数只作用于对应对象、部件或高度区间；机器配置、工程配置和局部覆盖不应混成一个无作用域的键值表。

## 机器参数

|字段|配置类型|含义|
|---|---|---|
|printer\_model|string|机型标识；用于识别切片时选择的打印机|
|printer\_variant|string|机器预设的变体标识|
|printer\_settings\_id|string|机器预设名称或标识|
|gcode\_flavor|enum|G\-code 方言，如 klipper、marlin2|
|nozzle\_diameter|float\[\]|喷嘴直径，mm；数组与挤出机配置对应|
|printable\_area|point\[\]|打印区域外轮廓，点列表，mm|
|printable\_height|float|最大打印高度，mm|
|extruder\_offset|point\[\]|各挤出机的 XY 偏移，mm|
|use\_relative\_e\_distances|bool|是否使用相对挤出距离|
|machine\_start\_gcode|string|打印开始模板；切片时展开|
|machine\_end\_gcode|string|打印结束模板；切片时展开|
|change\_filament\_gcode|string|换工具或换料模板；切片时展开|

## 耗材参数

|字段|配置类型|含义|
|---|---|---|
|filament\_type|string\[\]|材料类型，如 PLA、PETG|
|filament\_colour|string\[\]|材料颜色列表|
|filament\_diameter|float\[\]|丝径，mm|
|filament\_density|float\[\]|密度，g/cm³；用于估算重量|
|filament\_flow\_ratio|float\[\]|流量比例|
|filament\_max\_volumetric\_speed|float\[\]|最大体积流量，mm³/s|
|nozzle\_temperature|int\[\]|非首层喷嘴温度，°C|
|nozzle\_temperature\_initial\_layer|int\[\]|首层喷嘴温度，°C|
|hot\_plate\_temp|int\[\]|对应热床类型的非首层温度，°C|
|hot\_plate\_temp\_initial\_layer|int\[\]|对应热床类型的首层温度，°C|
|fan\_min\_speed|float\[\]|最低冷却风扇速度，%|
|fan\_max\_speed|float\[\]|最高冷却风扇速度，%|
|filament\_ids|string\[\]|耗材配置 ID；用于摘要中的 tray\_info\_idx|
|filament\_settings\_id|string\[\]|耗材预设名称或标识列表|
|filament\_retraction\_length|float\[\]|材料覆盖的回抽长度，mm；nil 表示不覆盖|

## 工艺参数

|字段|配置类型|含义|
|---|---|---|
|layer\_height|float|常规层高，mm|
|initial\_layer\_print\_height|float|首层层高，mm；此版本是绝对数值|
|wall\_loops|int|墙圈数|
|top\_shell\_layers|int|顶壳层数|
|bottom\_shell\_layers|int|底壳层数|
|sparse\_infill\_density|percent|稀疏填充密度，%|
|sparse\_infill\_pattern|enum|填充图案枚举|
|outer\_wall\_line\_width|float\_or\_percent|外墙线宽，可为 mm 或百分比|
|outer\_wall\_speed|float\[\]|外墙速度，mm/s|
|inner\_wall\_speed|float\[\]|内墙速度，mm/s|
|travel\_speed|float\[\]|空移速度，mm/s|
|default\_acceleration|float\[\]|默认加速度，mm/s²|
|enable\_support|bool|是否生成支撑|
|print\_sequence|enum|逐层或逐对象打印|
|curr\_bed\_type|enum|当前热床板类型；影响所选温度参数|

表中的类型是参数的逻辑类型。例如 int\[\] 在 JSON 中写成字符串数组，而不是数字数组。温度、速度等数组中可能包含流量变体，读取方法见下一节。

## 数组与流量变体

有些参数会为同一种材料保存 standard（标准流量）和 high\_flow（高流量）两套值。因此，“第几个耗材”和“参数数组的第几个元素”不总是相同。

|字段|含义|
|---|---|
|filament\_volume\_type|各耗材当前选择的流量类型|
|filament\_flow\_step\_size|各耗材占用的参数段长度|
|filament\_flow\_support|把各耗材支持的流量类型依次拼接起来|
|process\_flow\_support|工艺参数数组中各套值的流量类型顺序|
|nozzle\_volume\_type|各挤出机安装喷嘴的流量类型|
|printer\_flow\_support|机器参数的流量类型说明；此版本没有注册机器流量变体参数|

```text
filament_volume_type    = ["high_flow", "standard"]
filament_flow_step_size = ["2", "1"]
filament_flow_support   = ["standard", "high_flow", "standard"]
nozzle_temperature      = ["200", "220", "205"]

process_flow_support    = ["standard", "high_flow"]
outer_wall_speed        = ["60", "90"]
```

耗材 0 占前两个位置，选择 high\_flow，所以使用温度 220；耗材 1 占第三个位置，选择 standard，所以使用温度 205。工艺速度按 process\_flow\_support 选择，分别为 90 和 60。读取时先找到所属耗材段，再在段内选择流量类型。

其他数组按各自含义读取，例如 printable\_area 是轮廓点列表，nozzle\_diameter 是喷嘴列表，不能套用上述分段规则。

# 对象、打印盘与编辑信息

Metadata/model\_settings\.config 的根节点是 config。它把 3MF 中的几何对象与工程编辑状态关联起来。下面的 object id 对应 \.model 中的对象编号。

```xml
<config>
  <object id="2">
    <metadata key="name" value="支架"/>
    <part id="1" subtype="normal_part">
      <metadata key="name" value="主体"/>
    </part>
  </object>
  <plate>
    <metadata key="plater_id" value="1"/>
    <metadata key="plater_name" value="打印盘 1"/>
    <metadata key="locked" value="false"/>
    <model_instance>
      <metadata key="object_id" value="2"/>
      <metadata key="instance_id" value="0"/>
      <metadata key="identify_id" value="101"/>
    </model_instance>
  </plate>
</config>
```

|字段|类型 / 单位|出现条件|说明与示例|
|---|---|---|---|
|object@id|正整数|对象节点|对应 3MF 中的组合对象 id|
|object 下 metadata 的 name、module 键|文本|有相应值时|对象名称、模块名称；其他 key 可为对象级参数|
|part@id|正整数|部件节点|对应部件的几何资源 id|
|part@subtype|枚举|部件节点|normal\_part、negative\_part、modifier\_part、support\_enforcer、support\_blocker|
|part 下 metadata 的 matrix 键|16 个浮点数|有来源矩阵时|按行排列的 4×4 来源矩阵，与 3MF 的 12 数变换不同|
|source\_file|文本|有来源文件时|源文件名或路径，仅记录来源|
|source\_object\_id / source\_volume\_id|整数文本|有来源文件时|源文件中的对象和部件索引|
|source\_offset\_x / y / z|浮点文本|有来源文件时|源网格偏移|
|source\_in\_inches / source\_in\_meters|1|发生单位转换时|记录导入前的单位；不再次缩放已转换的几何|
|merged\_group\_id|标识文本|有合并组时|部件的装配合并关系|
|mesh\_stat|整数属性组|部件统计|修复边、退化面、删除面、反向面等历史统计|

|字段|类型 / 单位|出现条件|说明与示例|
|---|---|---|---|
|plater\_id|正整数|每个盘|原盘号，从 1 开始|
|plater\_name|文本|每个盘|盘名称，可为空|
|locked|true / false|每个盘|编辑器中的盘锁定状态|
|bed\_type|枚举文本|有盘级设置时|本盘的热床板类型|
|print\_sequence|枚举文本|有盘级设置时|逐层或逐对象打印|
|first\_layer\_print\_sequence|空格分隔整数|有自定义顺序时|首层的顺序配置|
|other\_layers\_print\_sequence|空格分隔整数|有自定义顺序时|其他层的顺序配置|
|other\_layers\_print\_sequence\_nums|整数文本|有相应配置时|与其他层顺序配置配套的计数|
|spiral\_mode|布尔文本|有盘级设置时|螺旋模式；历史文件还可能用 0/1|
|model\_instance/object\_id|正整数|盘中存在模型实例时|对应 3MF 对象 id|
|model\_instance/instance\_id|非负整数|盘中存在模型实例时|同一对象的实例下标，从 0 开始|
|model\_instance/identify\_id|标识文本|盘中存在模型实例时|实例标识；不是数组下标|

assemble/assemble\_item 另外保存装配视图中的 object\_id、instance\_id、12 数 transform 和三数 offset。该装配位置与打印盘摆放是两种编辑状态。

# 附加工程数据

|文件|记录内容|格式要点|
|---|---|---|
|layer\_heights\_profile\.txt|自适应层高|v2 头为 layer\_heights\_profile\_format\_version=2；每行 object\_id=N\|z0;h0;z1;h1…，N 为真实 3MF 对象 id，z/h 单位 mm|
|layer\_config\_ranges\.xml|高度范围参数|objects/object@id 是对象顺序号，从 1 开始；range 的 min\_z/max\_z 为 mm；option@opt\_key 是参数名，文本为参数值|
|brim\_ear\_points\.txt|鼠耳位置与半径|头为 brim\_points\_format\_version=0；记录 object\_id=N\|x y z radius…；N 为对象顺序号，从 1 开始|
|custom\_gcode\_per\_layer\.xml|逐层插入的换色、暂停、自定义代码|按原盘号保存事件，切片时展开为 G\-code|
|cut\_information\.xml|切割对象和连接件|保存切割 ID、校验值、连接件数及体积索引，用于工程编辑|
|三角面 paint\_\* 属性|支撑、接缝、颜色和绒毛涂绘|保存的是编辑数据；不等于最终 G\-code 中的工具命令|
|Auxiliaries/\*\*|图片等附加文件|按资源类型保存；不属于几何顶点或切片参数|

这些附加文件的 object\_id 含义并不相同：层高 profile v2 使用真实 3MF 对象 id；范围、鼠耳和切割文件使用模型中的对象顺序号。读取时以各文件格式为准。

## 逐层事件字段

|字段|类型 / 单位|出现条件|说明与示例|
|---|---|---|---|
|plate\_info@id|正整数|每个事件盘|原盘号，从 1 开始|
|layer@top\_z|浮点 / mm|每个事件|插入事件的打印高度|
|layer@type|整数枚举|每个事件|0 换色、1 暂停、2 换工具、3 模板、4 自定义、5 未知|
|layer@extruder|整数|每个事件|事件使用的工具提示值，按事件类型解释|
|layer@color / extra|文本|每个事件|颜色提示、消息或附加代码|
|layer@gcode|文本|每个事件|事件对应代码；暂停取 machine\_pause\_gcode，模板取 template\_custom\_gcode|
|mode@value|枚举文本|盘事件模式|SingleExtruder、MultiAsSingle、MultiExtruder|

## 混色参数

mixed\_filament\_definitions 是一个字符串，用分号分隔定义、用逗号分隔字段；不是 JSON 对象。基础字段依次为 component\_a、component\_b、enabled、custom、mix\_b\_percent、pointillism\_all\_filaments。两个 component 是从 1 开始的材料组件标识，混合比例为 0–100。

|后续 token|保存内容|
|---|---|
|g… / w…|渐变组件 ID 与权重|
|m… / z…|分布模式与局部 Z 子层数|
|xa… / xb…|两个组件的表面偏移|
|d… / o…|删除标记与自动来源标记|
|u… / cm…|稳定标识与创建模式|
|r1 / start / end|启用渐变时的范围；start/end 按四位小数写出|
|末尾可选项|非空时追加手动 pattern|

混色组件、耗材流量类型和物理工具是不同概念。固件执行的是切片后产生的工具命令，不能直接把混色组件标识当喷头编号。

# 版本与兼容说明

|情况|读取约定|
|---|---|
|旧模型版本键|可读 BambuStudio:3mfVersion、bamboo\_slicer:Version3mf；当前保存写 Snapmaker\_Orca:3mfVersion|
|模型版本与工程配置版本|当前模型写出版本为 1；工程 project\_schema\_version 为 "1"，两者分开读取|
|旧层高文件没有版本头|按 legacy v1 的对象顺序解释，不套用 v2 对象 id|
|未知参数或可选资源|保留可识别部分；只做几何导入时应说明未恢复的工程编辑内容|
|早期厂商 XML 写法|部分 metadata 名、printable 和 paint\_\* 属性沿用历史格式；它们属于厂商兼容约定，不都属于 Core 字段|
|文件类型表不完整|2\.4\.1 的 Content Types 未覆盖全部配置和附加资源；已知文件按本规范的实际内容格式读取|

未知的必需扩展会影响模型解释，读取器应报告不支持。仅缺少可选封面图时，可以继续打开几何与配置。

# 完整字段字典

正文列出常用机器、耗材和工艺字段。完整字典包含 699 个注册字段，支持按字段名、中文说明和预设类别检索；同时提供 JSON 版本，供开发工具读取。该集合也包含光固化（SLA）与配置元数据，不表示每份 FFF 工程都必须写入 699 项。

\[配置字段字典\.html\]

\[配置字段字典\.json\]

# 参考资料

字段名和写出行为以 Snapmaker Orca 2\.4\.1 为准。对应源码提交：1bff8daec7dc9daaf3addec9b4c234e8b74f474c。

[Snapmaker Orca：3MF 容器与工程字段实现](https://github.com/Snapmaker/OrcaSlicer/blob/1bff8daec7dc9daaf3addec9b4c234e8b74f474c/src/libslic3r/Format/bbs_3mf.cpp)

[3MF Core Specification](https://github.com/3MFConsortium/spec_core/blob/master/3MF Core Specification.md)

[3MF Production Extension](https://github.com/3MFConsortium/spec_production/blob/master/3MF Production Extension.md)

