# 字段字典对账：project_settings.config（v0）

> 数据：`docs/data/field-dictionary-project-settings-v0.csv`（817 行）
> 来源：源码 `PrintConfig.cpp` 静态定义（786 项）× 7 样本实测落盘字段（584 项）
> 日期：2026-09-10

## 对账结论

| 分类 | 数量 | 说明 |
|---|---|---|
| 源码定义且样本落盘 | 553 | 字段字典主体 |
| 源码定义但样本未落盘 | 233 | 多为 SLA 参数、机器限制类、当前流程不写的可选项（待逐项分类） |
| 样本落盘但源码无静态定义 | 31 | 见下表 |

## 31 个"落盘但无静态定义"字段

- **序列化名 ≠ 定义名（遗留前缀机制）**，18 个：`filament_retract_*` 系列（源码定义为 `retract_*`）、`machine_max_acceleration_*` / `machine_max_jerk_*` / `machine_max_speed_*`（机器限制项，另行定义）
- **Schema 版本字段**，1 个：`project_schema_version`
- 其余为 2.4.0 新增字段（`*_flow_support`、`filament_grouping_mode`、`*_volume_type` 等，源码版本可能已更新，待确认）

## 重要发现：ProjectSchemaVersion 机制已存在

源码 `src/libslic3r/ProjectSchemaVersion.cpp` 显示 Snapmaker 分支已建立格式版本注册表：

- 字段名：`project_schema_version`，**current_version = 1，legacy_version = 1**
- 提供 `version_from(config)`（缺失时视为 legacy）与 `is_newer(config)` 判断
- **但**：仅 2.4.0 样本落盘该字段，2.3.6 文件缺失 → 依赖"缺失=legacy"的隐式约定

这直接是规范"版本元数据"章节的代码锚点：规范应把它升级为**强制 header 字段**并定义递增规则（对应语义化版本的 Minor/Major），而不是可选键。

## 236 个未落盘定义项归类（已完成，见 CSV `category` 列）

| 类别 | 数量 | 说明 / 规范处置建议 |
|---|---|---|
| SLA 树脂流程专用 | 77 | `pad_*`、`hollowing_*`、SLA 柱状支撑、`material_*`、`display_*`、曝光/校正类。FDM 项目永不落盘 → **排除出 project_settings 规范范围** |
| CLI 动作参数 | 52 | `load_*`、`export_*`、`cut_*`、`rotate/scale/split` 等 Slic3r 命令行遗留 → **排除** |
| 运行时派生状态 | 52 | `print_time`、`total_*`、`extruded_*`、时间戳占位符等，切片器算出的结果而非设置 → **排除**；切片结果摘要归 `slice_info.config`/`plate_N.json` 管辖 |
| GUI 内部/废弃候选 | 25 | `zhop`、`brim_ears`、`adaptive_layer_height`、`initial_layer_height`（均已被新键或独立文件取代）、`makerlab_*`、`mtcpp/mstpp` 等 → **逐项与切片软件团队确认后标记废弃** |
| 预设系统内部 | 19 | `compatible_*`、`inherits`、`uptodate_*` → 属预设文件（filament/machine/process_settings_N）语义，**不应进项目文件**；但实测 `inherits_group`、`different_settings_to_system` 已泄漏进 project_settings（W2） |
| 打印主机连接 | 7 | `printhost_*`、`print_host*` → 涉及凭据，**建议明确禁止写入 3mf**（安全项） |

**对规范的直接推论**：FullPrintConfig 的 786 个静态定义中，仅约 553+31≈584 项属于"项目设置"语义。规范应把这 584 项定义为**允许写入白名单的初始集合**，其余六类字段一律禁入——这正是"规定新增配置的写入范围"的可执行形态。

字段字典 v1 = 553 个"定义且落盘" + 31 个"落盘无静态定义"（其中 18 个需在规范中正式承认序列化名并登记别名）。
