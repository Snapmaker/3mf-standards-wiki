# 打印配置文件里的命名与继承

> 面向新人的入门文档：一个打印配置文件叫什么、里面有哪些重要信息，以及不同配置之间如何复用参数。字段级约束以实际配置数据为准。

## 1. 先看一份配置文件

每个耗材、机器或工艺配置都是一个 JSON 文件。文件名告诉人“这是什么配置”，文件内容则保存它的元信息和参数值。

```text
Snapmaker/
└─ filament/
   └─ Snapmaker PLA @U1 0.4 nozzle.json
```

打开后，开头通常能看到这样的内容：

```json
{
  "type": "filament",
  "name": "Snapmaker PLA @U1 0.4 nozzle",
  "from": "system",
  "instantiation": "true",
  "inherits": "Snapmaker PLA @U1 base",
  "setting_id": "…",
  "filament_vendor": "Snapmaker",
  "filament_type": "PLA",
  "nozzle_temperature_range_low": "190",
  "nozzle_temperature_range_high": "220"
}
```

这份文件表达了三件事：

1. 它是一份耗材配置；
2. 它适用于 Snapmaker PLA、U1 机器和 0.4 mm 喷嘴；
3. 它在一个名为 `Snapmaker PLA @U1 base` 的基础配置上继续修改。

## 2. 文件放在哪里

配置按用途分成三棵树：

| 目录 | 内容 | 例子 |
|---|---|---|
| `filament/` | 耗材和支撑材料 | `Snapmaker PLA @U1 0.4 nozzle.json` |
| `machine/` | 打印机和机型变体 | `Snapmaker U1 (0.4 nozzle).json` |
| `process/` | 层高、质量和速度等工艺 | `0.20 Standard @Snapmaker U1 (0.4 nozzle).json` |

目录名和文件中的 `type` 必须对应：`filament`、`machine`、`process` 三者不能混用。

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
| 普通耗材 | `Snapmaker PLA @U1 0.4 nozzle` | Snapmaker 的 PLA，适用于 U1 和 0.4 mm 喷嘴 |
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

参数值沿继承链逐层合并：子文件写了自己的值，就覆盖父文件的同名值；子文件没有写，就继续使用父文件的值。

## 6. 继承树：从公共配置到具体配置

继承的目的，是把公共内容放在上层，把差异留在下层。典型的结构是：

```text
公共基础
└─ 分类基础
   └─ 某厂商/材料/机型的基础配置
      └─ 可直接使用的具体配置
```

### 6.1 filament 的层级

```text
fdm_filament_common
└─ fdm_filament_pla_category
   └─ Snapmaker PLA @U1 base
      └─ Snapmaker PLA @U1 0.4 nozzle
```

- `fdm_filament_common` 保存所有耗材共有的基础内容；
- `fdm_filament_pla_category` 保存 PLA 类别共有的内容；
- `Snapmaker PLA @U1 base` 保存该材料与机型组合的基础内容；
- 最后一层只保存 0.4 mm 喷嘴相关的差异。

基础耗材配置通常不可直接实例化，具体耗材配置则可以设置为可实例化。材料名、厂商和耗材标识等信息一般在基础层确定，温度、风扇和挤出参数可以在更具体的层级覆盖。

### 6.2 machine 的层级

```text
fdm_klipper
└─ fdm_toolchanger
   └─ fdm_U1
      └─ Snapmaker U1 (0.4 nozzle)
```

越靠上的文件越通用，越靠下的文件越接近实际机器。机器特有的 G-code、尺寸、喷嘴数量和硬件能力应放在具体机器层，而不是复制到所有基础配置中。

### 6.3 process 的层级

```text
fdm_process_U1
└─ fdm_process_U1_common
   └─ fdm_process_U1_0.20_nozzle_0.4
      └─ 0.20 Standard @Snapmaker U1 (0.4 nozzle)
```

工艺文件通常把公共工艺设置放在上层，把层高、质量档位、机器和喷嘴相关的差异留给下层。

## 7. 名称和内容要互相说得通

文件名是给人看的摘要，JSON 内容是给读取程序使用的详细数据。两者表达同一件事时，应保持一致：

```text
文件名：Snapmaker PLA @U1 0.4 nozzle
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
- `type` 与目录类型一致；
- `inherits` 指向真实存在的父配置，且不会形成循环；
- 子配置只保存必要的差异，公共参数放在父配置；
- 名称表达的厂商、材料、机器、层高和喷嘴与内容字段一致；
- `filament_id`、`setting_id` 等标识字段保持稳定；
- `from`、`instantiation`、`version` 等元字段保持统一格式；
- 文件名不包含非法字符，也不使用保留设备名。

> [!TIP] 一个简单判断
> 先只看文件名，应该能说出“这是什么配置、适用于什么条件”；再打开 JSON，应该能找到与这句话对应的元字段、标识字段和参数覆盖。两边对不上时，优先检查名称、`inherits` 和绑定字段。
