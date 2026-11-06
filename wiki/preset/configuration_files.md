# 打印配置文件里的命名与继承

> 面向新人的入门文档：一个打印配置文件叫什么、里面有哪些重要信息，以及不同配置之间如何复用参数。字段级约束以实际配置数据为准。

## 1. 先看一份配置文件

每个耗材、机器或工艺配置都是一个 JSON 文件。文件名告诉人“这是什么配置”，文件内容则保存它的元信息和参数值。

```text
Snapmaker/
└─ filament/
   └─ Generic ABS @U1 0.2 nozzle.json
```

打开后，开头通常能看到这样的内容（节选，完整文件约 114 个键）：

```json
{
  "type": "filament",
  "name": "Generic ABS @U1 0.2 nozzle",
  "from": "system",
  "instantiation": "true",
  "inherits": "Generic ABS @U1 base",
  "setting_id": "GFSB99",
  "compatible_printers": ["Snapmaker U1 (0.2 nozzle)"],
  "nozzle_temperature_range_low": ["240"],
  "nozzle_temperature_range_high": ["270"]
}
```

这份文件表达了三件事：

1. 它是一份耗材配置；
2. 它适用于 U1 机器的 0.2 mm 喷嘴——`compatible_printers` 会精确到“机型 (喷嘴)”；
3. 它在一个名为 `Generic ABS @U1 base` 的基础配置上继续修改。

## 2. 文件放在哪里

配置按用途分成三棵树：

| 目录 | 内容 | 例子 |
|---|---|---|
| `filament/` | 耗材和支撑材料 | `Generic ABS @U1 0.2 nozzle.json` |
| `machine/` | 打印机和机型变体 | `Snapmaker U1 (0.4 nozzle).json` |
| `process/` | 层高、质量和速度等工艺 | `0.20 Standard @Snapmaker U1 (0.4 nozzle).json` |

目录名和文件中的 `type` 必须对应：`filament`、`machine`、`process` 三者不能混用。

`machine/` 目录和厂商根目录里还有两类特殊文件：

| 文件 | 作用 |
|---|---|
| `<机型>.json`（`type: machine_model`） | 机型注册表：模型 ID、床面 STL、纹理图、可选喷嘴直径列表——**不含打印设置**，设置在喷嘴实例文件里 |
| 厂商根的 `Snapmaker.json` | 装载清单：登记全部机型、基座和实例文件（每条带 `sub_path` 指向具体 JSON） |

## 3. 文件名是配置的“人类可读索引”

文件名不只是一个随机标识，它把配置最重要的适用条件写在名称里。阅读名称时，可以按下面的顺序理解：

### 3.1 耗材名称

耗材名称通常由以下信息组成：

```text
厂商 + 材料大类 +（材料子型号）+ 适用机型 + 喷嘴尺寸
```

常见写法有三种：

| 用途 | 名称示例 | 读法 |
|---|---|---|
| 普通耗材 | `Snapmaker PETG-CF @U1 0.4 nozzle` | Snapmaker 的 PETG-CF，适用于 U1 和 0.4 mm 喷嘴 |
| 带子型号的耗材 | `Generic PETG-CF @U1 0.6 nozzle` | Generic 的 PETG-CF，适用于 U1 和 0.6 mm 喷嘴 |
| 支撑材料 | `Snapmaker Support For PLA @U1 0.2 nozzle` | 用于 PLA 的支撑材料，适用于 U1 和 0.2 mm 喷嘴 |

有些耗材名称没有机型或喷嘴部分，例如 `PolyLite PLA`。这表示它是更通用的一层配置，具体适配关系由继承链和内容字段补充。

### 3.2 机器名称

机器名称通常是：

```text
厂商 + 机型 +（可选的喷嘴尺寸）
```

例如：

- `Snapmaker U1 (0.4 nozzle)`：U1 的 0.4 mm 喷嘴配置；
- `Snapmaker J1`：J1 的通用机器配置。

### 3.3 工艺名称

工艺名称先写层高和质量档位，再写厂商、机型和喷嘴：

```text
层高 + 质量档位 + 厂商 +（可选机型）+ 喷嘴尺寸
```

例如：

- `0.20 Standard @Snapmaker U1 (0.4 nozzle)`：0.20 mm 层高、Standard 档位、适用于 Snapmaker U1 和 0.4 mm 喷嘴；
- `0.24 Draft @Snapmaker (0.6 nozzle)`：0.24 mm 层高、Draft 档位、厂商为 Snapmaker，未限定具体机型。

### 3.4 名称中的大小写和写法

名称中的值有统一写法。例如喷嘴使用 `0.4`，而不是 `0.40`；机型使用 `U1`，而不是 `u1`；厂商使用 `Snapmaker`，而不是 `snapmaker`。

输入时可以识别一些常见别名，但保存和展示时应使用统一写法。这样做可以避免同一个配置因为大小写或数字格式不同而出现多个名称。

### 3.5 文件名的通用限制

名称必须能作为文件名使用：

- 不能为空，长度不超过 200 字节；
- 不能包含控制字符或 `< > : " / \ | ? * %`；
- 不能以空格或句点结尾；
- 不能使用 Windows 保留名称，例如 `CON`、`PRN`、`AUX`、`NUL`、`COM1` 和 `LPT1`。

## 4. JSON 里的重要元信息

参数字段可能很多，但真正决定文件身份和关系的字段并不多：

| 字段 | 它回答的问题 | 说明 |
|---|---|---|
| `type` | 这是什么类型？ | 必须与所在目录一致 |
| `name` | 这份文件叫什么？ | 必须与文件名去掉 `.json` 后的名称一致 |
| `inherits` | 它基于哪份配置？ | 写父配置名称；最顶层配置省略 |
| `from` | 配置从哪里来？ | 常见值为 `system`，表示内置来源 |
| `instantiation` | 能不能直接使用？ | `true` 表示可实例化，`false` 表示基础配置 |
| `version` | 这份配置处于哪个版本？ | 按配置数据的版本约定保存 |
| `renamed_from` | 它以前叫什么？ | 可选的改名历史，多个旧名称用分号保留 |

其中 `name` 和 `inherits` 是结构字段，不应当像普通参数一样随意覆盖：

- 改名时，文件名、`name`、子配置的 `inherits` 需要一起更新；
- 删除父配置前，必须先处理它的子配置；
- 根配置没有 `inherits`，不能指向一个不存在的父配置；
- 继承关系不能绕回自己形成环。

## 5. 标识字段与实际参数

除了元信息，配置还包含两类业务字段。

### 5.1 标识字段

标识字段用于把配置与具体对象或预设对应起来：

| 字段 | 常见位置 | 用途 |
|---|---|---|
| `filament_id` | filament | 标识一款耗材实体 |
| `setting_id` | 三类配置 | 标识一个具体设置 |
| `filament_settings_id` | filament | 标识耗材设置族 |
| `printer_settings_id` | machine | 标识机器设置 |
| `process_id` | process | 标识工艺设置 |

同一实体的多个派生配置通常共享相应的标识字段。标识字段不参与文件名组成，也不能替代 `name`。

### 5.2 参数字段

参数字段是实际的打印设置，例如：

```json
{
  "nozzle_temperature_range_low": "190",
  "nozzle_temperature_range_high": "220",
  "filament_diameter": "1.75",
  "filament_colour": ["#FFFFFF"]
}
```

参数值沿继承链逐层合并：子文件写了自己的值，就覆盖父文件的同名值；子文件没有写，就继续使用父文件的值；整条链都没有写的键，使用切片引擎的内置默认值。

## 6. 继承树：公共内容在上，差异在下

继承的目的，是把公共内容放在上层、把差异留在下层。合并按“键”进行：子文件有这个键就用子文件的值，没有就找父文件，整条链都没有就用引擎内置默认值。`instantiation: false` 的基础配置不会出现在 UI 的选择列表里。

三棵树真实的层级和每层的内容量（括号内为实测键数）：

### 6.1 filament 的层级

```text
fdm_filament_common          4 键（纯锚点，不带参数）
└─ fdm_filament_abs_category  63 键（ABS 家族共性：温度、腔温……）
   └─ Generic ABS @U1 base     5 键（只放身份键，纯中转层）
      ├─ Generic ABS                 114 键（0.4 默认实例）
      └─ Generic ABS @U1 0.2 nozzle  114 键（0.2 喷嘴实例）
```

> [!IMPORTANT] 实测现状
> 耗材的最后一层**并不是“只保存喷嘴差异”**：上面两个实例 114 键里只有 `name` 和 `compatible_printers` 两键不同，其余内容重复携带。材料共性确实上移到了 category 层，但喷嘴兄弟之间是“各自带全量”的写法，取舍原因见 §6.4。

### 6.2 machine 的层级

```text
fdm_klipper(53) → fdm_toolchanger(58) → fdm_U1(43) → Snapmaker U1 (0.4 nozzle)(64 键)
fdm_common(32)  → fdm_idex(42)        → Snapmaker J1 (0.4 nozzle)(12 键)
```

机器侧有两条独立的根树。越靠下越接近实际机器：机型特有的 G-code、尺寸、硬件能力放在机型基座层，喷嘴实例只放绑定信息和喷嘴缩放值（`nozzle_diameter`、`max/min_layer_height` 等）。`Snapmaker J1.json` 这类机型注册表文件不属于设置树，它只登记机型元数据。

### 6.3 process 的层级

```text
fdm_process_common(182) → fdm_process_U1 → fdm_process_U1_common(75) → fdm_process_U1_0.08(26)
                          → 0.08mm Standard @Snapmaker U1 (0.4 nozzle)(37 键)
fdm_process_common(182) → fdm_process_idex(64) → 0.16 Optimal @Snapmaker J1 (0.4 nozzle)(18 键)
```

工艺是三棵树里“上移”做得最彻底的：公共键大头全在 `fdm_process_common`，U1 线还有“机型×层高”基座，实例只有 18–37 个键。层高、质量档位、机器和喷嘴相关的差异留在下层。

### 6.4 三种组织风格与取舍

| 风格 | 用在哪 | 特征 | 代价 |
|---|---|---|---|
| 彻底上移 | process | 公共键全在基座，实例很薄 | 改公共值动一个文件，但实例不自包含 |
| 半上移 + 实例自包含 | filament 新式（U1/J1） | 材料共性上移 category，喷嘴实例各带全量 | 实例可独立分发（云端按 `setting_id` 逐实例管理）；改公共值要动一批文件 |
| 单文件广兼容 | filament 老式（A250/A350） | 不分机型子预设，`compatible_printers` 一次列出全部兼容的“机型 (喷嘴)” | 文件最少，但无法按机型微调 |

新增预设时，先看同目录既有文件用的是哪种风格，跟着走，不要混用。

### 6.5 哪些内容必须放在子配置

机制上没有“必须放父”的参数——上移只是去重选择。但下面这些键每个实例必须自己带：

| 类别 | 键 |
|---|---|
| 身份键 | `type`、`name`、`from`、`instantiation`、`setting_id`、`inherits` |
| 绑定键 | 耗材/工艺的 `compatible_printers`（精确到“机型 (喷嘴)”）；机器实例的 `printer_model` + `printer_variant` + `default_print_profile` |
| 缩放值 | `nozzle_diameter`、`max/min_layer_height`、层高系参数 |

## 7. 名称和内容要互相说得通

文件名是给人看的摘要，JSON 内容是给读取程序使用的详细数据。两者表达同一件事时，应保持一致：

```text
文件名：Snapmaker PLA
```

对应的内容应能体现：

```json
{
  "filament_vendor": "Snapmaker",
  "filament_type": "PLA"
}
```

如果文件名写的是 `PLA`，内容却写成 `PETG`，这份配置就失去了可读性，也会导致名称和参数含义不一致。命名字段与内容字段的关系通常包括：

| 名称信息 | 常见内容字段 |
|---|---|
| 厂商 | `filament_vendor` |
| 材料大类 | `filament_type` |
| 机器 | 机器兼容性或机器标识字段 |
| 层高、质量档位、喷嘴 | 工艺参数或适用条件字段 |

基础配置中的人工标识，例如 `filament_id`，应使用稳定的非空字符串；它不应随着喷嘴或质量档位的变化而随意改变。

## 8. 新增或修改文件时的检查清单

- 文件放在正确的 `filament/`、`machine/` 或 `process/` 目录；
- 文件名使用统一的大小写、数字格式和空格；
- 文件名与 JSON 的 `name` 完全一致；
- `type` 与目录类型一致（机型注册表用 `machine_model`，且不写打印设置）；
- `inherits` 指向真实存在的父配置，且不会形成循环；
- 继承链上不重复定义不变的值，同时遵循所在目录的组织风格（见 §6.4——耗材实例按现状要自包含）；
- 实例自带身份键与绑定键（见 §6.5）；
- 名称表达的厂商、材料、机器、层高和喷嘴与内容字段一致；
- `filament_id`、`setting_id` 等标识字段保持稳定；
- `from`、`instantiation`、`version` 等元字段保持统一格式；
- 文件名不包含非法字符，也不使用保留设备名。

> [!TIP] 一个简单判断
> 先只看文件名，应该能说出“这是什么配置、适用于什么条件”；再打开 JSON，应该能找到与这句话对应的元字段、标识字段和参数覆盖。两边对不上时，优先检查名称、`inherits` 和绑定字段。
