# CLI 模式（命令行切片）

← [Wiki 首页](../home.md)

不开图形界面，直接在命令行加载模型/工程、施加变换、切片并导出，适合批处理与自动化流水线。命令行工具随软件发布包提供，可执行文件名以发布包为准。

## Invocation

```
orca-slicer [输入文件...] [选项...]
```

- 不以 `-` 开头的参数都按输入文件（模型或工程）处理，按出现顺序加载。
- 单独的 `--` 表示"之后的参数全部是文件"，文件名以 `-` 开头时用它保护。

## Flag Syntax

### Boolean flags

开关型选项只要出现即生效（`--info`），也接受 `=1`/`=0`。陷阱：`--flag 0`（空格分隔）**不会**把开关关掉，`0` 会被当成输入文件。

### Value flags

单值选项两种写法等价：`--slice 0` 或 `--slice=0`。

规则：设置键名用下划线（`layer_height`），命令行选项统一转连字符（`--layer-height`）。

### Vector (multi-value) flags

逐耗材/逐对象取值的选项传逗号分隔的序列，位置 = 0 起索引：

- **补齐**：缺的槽位用**首个值**重复填充，不是各槽默认值——`--retraction-length=0.9,0.8,1.2` 在 4 耗材下得 `[0.9, 0.8, 1.2, 0.9]`。
- **追加**：同一选项出现多次是追加不是覆盖——`--retraction-length=0.8 --retraction-length=1.2` 得 `[0.8, 1.2]`；要覆盖就一次传全表。

## Setting Overrides

除 CLI 专用选项外，几乎所有界面设置页参数都能用 `--键名=值` 覆盖（键名下划线转连字符）。每个键的键名见其键页的 `[Variable]`/`[Variables]` 行。

> [!NOTE]
> 上游 wiki 列出不开放命令行覆盖的键共三类：预设身份与继承（`preset_name`、`inherits` 等）、打印主机凭据（`print_host`、`printhost_apikey` 等）、内部索引（`filament_self_index` 等），并记为 43 个。实际开放范围以实测为准：覆盖被拒提示 "Invalid option" 时，先查该键是否属于这三类。

## Example

```bash
orca-slicer model.3mf --load-settings "process.json;printer.json" --load-filaments filament.json --arrange 1 --slice 0 --export-3mf output.3mf
```

加载工程 → 应用工艺/打印机/耗材设置 → 自动排版 → 全部盘切片 → 导出 3mf。（示例沿用上游文档，fork 未逐项实测，用前先验证。）
