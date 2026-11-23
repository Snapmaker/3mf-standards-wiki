# 打印配置文件命名与继承规范 v1.0（草案）

← [Wiki 首页](../home.md)

相关：[耗材预设文件格式](preset_filament_format.md) · [工艺预设文件格式](preset_process_format.md) · [打印机预设文件格式](preset_machine_format.md)

> 规范性用语：**应 / 不应**表示要求，**宜 / 不宜**表示推荐，**可**表示允许。

## 目录

- [前言](#前言)
- [引言](#引言)
- [1 范围](#1-范围)
- [2 术语和定义](#2-术语和定义)
- [3 总体结构](#3-总体结构)
- [4 命名规则](#4-命名规则)
  - [4.1 耗材预设](#41-耗材预设)
  - [4.2 打印机预设](#42-打印机预设)
  - [4.3 工艺预设](#43-工艺预设)
  - [4.4 大小写与写法](#44-大小写与写法)
  - [4.5 文件名限制](#45-文件名限制)
- [5 元数据与标识字段](#5-元数据与标识字段)
  - [5.1 元数据](#51-元数据)
  - [5.2 标识字段](#52-标识字段)
- [6 继承与覆盖](#6-继承与覆盖)
  - [6.1 覆盖规则](#61-覆盖规则)
  - [6.2 继承层级](#62-继承层级)
  - [6.3 组织风格](#63-组织风格)
  - [6.4 子配置必备键](#64-子配置必备键)
- [7 一致性要求](#7-一致性要求)
- [深入阅读](#深入阅读)

## 前言

本规范规定 Snapmaker Orca 打印配置文件的目录组织、命名、元数据和继承规则及一致性要求，适用于预设的使用、开发和维护。

## 引言

打印配置文件以 JSON 对象保存元信息和配置参数，按用途分为耗材、打印机、工艺三类，通过继承复用公共设置。本文依次说明目录组织、命名规则、元数据与标识字段、继承与覆盖规则和一致性检查。三类文件的字段级格式和参数写法分别见 [耗材预设文件格式](preset_filament_format.md)、[工艺预设文件格式](preset_process_format.md)、[打印机预设文件格式](preset_machine_format.md)。

## 1 范围

本页面规定 Snapmaker Orca **打印配置文件**（预设）的目录组织、命名、元数据、标识字段与继承规则，供使用、开发和维护预设的人员查阅。三类预设分别位于 `Snapmaker/filament/`、`Snapmaker/machine/`、`Snapmaker/process/`，JSON 中的 `type` 分别为 `"filament"`、`"machine"`、`"process"`。

本页面是三类预设格式规范的共同部分；参数字典、参数序列化与各类特有字段见三份预设格式规范，本文不重复列出。

## 2 术语和定义

| 术语 | 含义 |
|---|---|
| 基础预设 | `instantiation` 为字符串 `"false"`，用于提供共享配置 |
| 实例 | `instantiation` 为字符串 `"true"`，用于选择或绑定具体配置 |
| 继承 | `inherits` 按名称引用父预设；子项覆盖父项的同名键，未指定的参数继续回退到父项或内置默认值 |

## 3 总体结构

配置按用途分为三棵树：

| 目录 | 内容 | 示例 |
|---|---|---|
| `filament/` | 耗材与支撑材料 | `Generic ABS @U1 0.2 nozzle.json` |
| `machine/` | 打印机与机型变体 | `Snapmaker U1 (0.4 nozzle).json` |
| `process/` | 层高、质量与速度等工艺 | `0.20 Standard @Snapmaker U1 (0.4 nozzle).json` |

目录名应与 JSON 中的 `type` 对应，三类不应混用。

`machine/` 目录和厂商根目录还存在两类特殊文件：

| 文件 | 作用 |
|---|---|
| `<机型>.json`（`type: machine_model`） | 机型注册表：模型 ID、床面 STL、纹理图、可选喷嘴直径列表；不应包含打印设置，设置放在打印机实例中 |
| `Snapmaker.json` | 厂商清单：通过 `machine_model_list`、`machine_list`、`process_list`、`filament_list` 登记全部文件，条目带 `sub_path` 指向具体 JSON；新增或改名时应同步核对清单及引用 |

## 4 命名规则

文件名去除 `.json` 后应与 `name` 一致。名称宜由各小节所列部分按顺序组成，各段以空格分隔，适用机型段以 `@` 引出。

### 4.1 耗材预设

耗材名称通常由以下部分按顺序组成：

```text
厂商 + 材料大类 +（材料子型号）+ 适用机型 + 喷嘴尺寸
```

| 形式 | 名称示例 |
|---|---|
| 普通耗材 | `Snapmaker PETG-CF @U1 0.4 nozzle` |
| 带子型号的耗材 | `Generic PETG-CF @U1 0.6 nozzle` |
| 支撑材料 | `Snapmaker Support For PLA @U1 0.2 nozzle` |

名称可省略机型或喷嘴部分（如 `PolyLite PLA`），表示更通用的一层预设；具体适配关系由继承链和 `compatible_printers` 补充。

### 4.2 打印机预设

打印机名称通常由以下部分按顺序组成：

```text
厂商 + 机型 +（可选的喷嘴尺寸）
```

例如：

- `Snapmaker U1 (0.4 nozzle)`：U1 的 0.4 mm 喷嘴配置；
- `Snapmaker J1`：J1 的通用打印机配置。

### 4.3 工艺预设

工艺名称先写层高和质量档位，再写厂商、机型和喷嘴：

```text
层高 + 质量档位 + 厂商 +（可选机型）+ 喷嘴尺寸
```

例如：

- `0.20 Standard @Snapmaker U1 (0.4 nozzle)`：0.20 mm 层高、Standard 档位、适用于 Snapmaker U1 和 0.4 mm 喷嘴；
- `0.24 Draft @Snapmaker (0.6 nozzle)`：0.24 mm 层高、Draft 档位、厂商为 Snapmaker，未限定具体机型。

### 4.4 大小写与写法

名称中的值应使用统一写法。例如喷嘴尺寸写 `0.4`，不写 `0.40`；机型写 `U1`，不写 `u1`；厂商写 `Snapmaker`，不写 `snapmaker`。

输入时可识别常见别名，但保存和展示应使用统一写法，避免同一配置因大小写或数字格式不同而出现多个名称。

### 4.5 文件名限制

文件名应满足目标操作系统的文件规则：

- 不为空，长度不超过 200 字节；
- 不包含控制字符或 `< > : " / \ | ? * %`；
- 不以空格或句点结尾；
- 不使用 Windows 保留名称，例如 `CON`、`PRN`、`AUX`、`NUL`、`COM1` 和 `LPT1`。

## 5 元数据与标识字段

### 5.1 元数据

决定文件身份和关系的元数据字段：

| 字段 | 写法与用途 |
|---|---|
| `type` | 字符串 `"filament"`、`"machine"` 或 `"process"`，应与所在目录及预设类别对应 |
| `name` | 非空字符串，标识预设；与文件名及厂商清单名称对应 |
| `inherits` | 父预设的 `name`；根预设可省略；父项应可解析且不得形成循环 |
| `from` | 系统预设使用字符串 `"system"` |
| `instantiation` | 系统预设使用字符串 `"true"` 或 `"false"`，不是 JSON 布尔值 |
| `version` | 可选版本元数据；应遵循所在预设集现有约定 |
| `renamed_from` | 可选历史名称；多个旧名称用分号分隔 |

`name` 与 `inherits` 是结构字段，不应像普通参数一样随意覆盖：

- 改名时，应同步更新文件名、`name`、子预设的 `inherits` 和厂商清单；
- 删除父预设前，应先处理其子预设；
- 根预设不应携带无法解析的 `inherits`；
- 继承关系不应形成循环。

### 5.2 标识字段

标识字段把预设与具体实体或设置对应起来：

| 字段 | 常见位置 | 用途 |
|---|---|---|
| `filament_id` | filament | 耗材实体标识 |
| `setting_id` | 三类预设 | 设置标识 |
| `filament_settings_id` | filament | 耗材设置族标识 |
| `printer_settings_id` | machine | 打印机设置标识 |
| `process_id` | process | 工艺设置标识 |

同一实体的多个派生预设宜共享相应标识字段。标识字段不参与文件名组成，也不应替代 `name`。

## 6 继承与覆盖

### 6.1 覆盖规则

参数值沿继承链逐层合并：子预设写出的键覆盖父项的同名键；子预设未写出的键继续向父项回退；整条链都未定义的键使用引擎内置默认值。`instantiation` 为 `"false"` 的基础预设不出现在 UI 的选择列表里。

### 6.2 继承层级

三类预设均以 `fdm_*` 基座开头，逐层落到可直接使用的实例。本节给出各树的分层思路。

#### 耗材预设

```text
fdm_filament_common
└─ fdm_filament_abs_category       材料家族共性：温度、腔温……
   └─ Generic ABS @U1 base          只承载身份键的中转层
      ├─ Generic ABS                0.4 默认实例
      └─ Generic ABS @U1 0.2 nozzle 0.2 喷嘴实例
```

材料共性宜放在 category 层；`@U1 base` 这类中转层只承载身份键和 `inherits`。耗材喷嘴实例目前各自携带接近全量的参数，只有 `name` 和 `compatible_printers` 等个别键不同；新增或修改实例时，宜按同目录既有文件复制后调整，不宜只写与父项的差异。

#### 打印机预设

```text
fdm_klipper → fdm_toolchanger → fdm_U1 → Snapmaker U1 (0.4 nozzle)
fdm_common  → fdm_idex        → Snapmaker J1 (0.4 nozzle)
```

打印机侧有两条独立的根树，越靠下越接近实际机器。机型特有的 G-code、尺寸和硬件能力宜放在机型基座层；喷嘴实例只应携带绑定信息与喷嘴缩放值（`nozzle_diameter`、`max/min_layer_height` 等）。`Snapmaker J1.json` 这类机型注册表不属于设置树，不参与继承。

#### 工艺预设

```text
fdm_process_common → fdm_process_U1 → fdm_process_U1_common → fdm_process_U1_0.08
                                   → 0.08mm Standard @Snapmaker U1 (0.4 nozzle)
fdm_process_common → fdm_process_idex → 0.16 Optimal @Snapmaker J1 (0.4 nozzle)
```

工艺的公共键宜集中在 `fdm_process_common`；U1 线在公共基座与实例之间还有“机型 × 层高”基座。层高、质量档位、机器和喷嘴相关的差异应留在下层。

### 6.3 组织风格

| 风格 | 使用范围 | 写法 |
|---|---|---|
| 公共键彻底上移 | process | 公共键集中在基座，实例只写差异 |
| 材料共性上移、实例自包含 | filament 新式（U1/J1） | 材料共性放 category，喷嘴实例各带全量 |
| 单文件广兼容 | filament 老式（A250/A350） | 不分机型子预设，`compatible_printers` 一次列出全部兼容的“机型 (喷嘴)” |

新增预设时，宜先确认同目录既有文件采用的组织风格并保持一致，不宜混用。

### 6.4 子配置必备键

机制上不存在“必须放在父级”的参数，上移仅是去重选择。以下键每个实例应自行携带：

| 类别 | 键 |
|---|---|
| 身份键 | `type`、`name`、`from`、`instantiation`、`setting_id`、`inherits` |
| 绑定键 | 耗材与工艺的 `compatible_printers`（精确到“机型 (喷嘴)”）；打印机实例的 `printer_model` + `printer_variant` + `default_print_profile` |
| 缩放值 | `nozzle_diameter`、`max/min_layer_height`、层高系参数 |

## 7 一致性要求

生产或修改打印配置文件时应检查：

1. 文件位于正确的目录，`type` 与目录、预设类别及厂商清单相互对应；机型注册表使用 `machine_model`，且不携带打印设置。
2. 文件名与 `name` 一致，名称的构成、大小写和文件名限制符合 §4。
3. `inherits` 能找到同类父项，继承链无环；改名时同步更新文件名、`name`、子项和厂商清单。
4. 继承链上不重复定义不变的值，同时遵循所在目录的组织风格（§6.3）；耗材实例按现状宜自包含（§6.2）。
5. 实例携带 §6.4 列出的身份键与绑定键。
6. 名称表达的厂商、材料、机器、层高和喷嘴与内容字段一致；`filament_id`、`setting_id` 等标识字段保持稳定。
7. `from`、`instantiation`、`version` 等元字段使用统一格式；`instantiation` 使用字符串而非 JSON 布尔值。
8. 文件名不包含非法字符，不使用保留设备名。

## 深入阅读

- 字段级格式、参数序列化与参数字典见 [耗材预设文件格式](preset_filament_format.md) · [工艺预设文件格式](preset_process_format.md) · [打印机预设文件格式](preset_machine_format.md)。
