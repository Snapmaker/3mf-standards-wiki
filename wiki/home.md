# Wiki 首页

本 wiki 讲清楚两件事：**我们的切片软件（OrcaSlicer fork）导出的 3mf 文件里有什么、为什么是这样**；后续将扩展为 fork 的完整使用文档。组织方式沿用上游 OrcaSlicer Wiki 的目录分类法。

## 3MF 专题

入门建议从第一篇开始按序读：

| 页面 | 内容 |
|---|---|
| [3mf 内部文件组成与作用](specification/3mf/3mf%20documents/3mf_file_structure.md) | 入门：一个 3mf 是什么、有哪些文件、各自干什么 |
| [project_settings.config](specification/3mf/3mf%20documents/3mf_project_settings.md) | 全局打印设置：文件作用与读取流程、键类型总览、系统级固定键与三层覆盖基准 |
| [model_settings.config](specification/3mf/3mf%20documents/3mf_model_settings.md) | 对象/零件/盘/实例图解、与 3dmodel.model 两侧对照、参数覆盖优先级 |
| [3MF 版本管理细则](specification/3mf/3mf%20documents/3mf_version_management.md) | 进阶：五层版本标识、兼容性矩阵、变更检查清单 |
| [3mf 工程文件规范 v1.0（草案）](specification/3mf/3mf_standard.md) | 标准正文：包结构 → 模型部件 → 配置与三层覆盖 → 版本兼容，GB/T 体例；未闭环项按现状描述并标注待裁决（Qxx） |

## gcode.3mf 专题

切片成品包（`.gcode.3mf`，内嵌 G-code）的格式文档：

| 页面 | 内容 |
|---|---|
| [gcode.3mf 规范 v1.0（草案）](specification/gcode.3mf/gcode_3mf_standard.md) | 标准正文：总体结构 → 盘与打印数据 → 一致性要求，GB/T 体例（技术内容 = v0.9.9） |
| [G-code 文件规范 v1.0（草案）](specification/gcode.3mf/gcode_standard.md) | 标准正文：文件布局 → 行语法与指令 → 注释标记 → 自描述块与统计，GB/T 体例（基准机型 U1 / Klipper，基于 2.4.x 源码实测） |
| [两端交互字段对照](specification/gcode.3mf/gcode_3mf_interaction_fields.md) | 切片端写出、固件解析的字段清单（快照自飞书交互协议表）：设置键索引 + 协议字段详解 + 变更记录 |

## 预设专题

打印配置文件（filament / machine / process）的命名、格式与一致性要求：

| 页面 | 内容 |
|---|---|
| [打印配置文件：命名与继承](preset/configuration_files.md) | 入门：配置文件叫什么、元信息、参数如何复用 |
| [耗材预设文件格式要求 v1.0（草案）](preset/preset_filament_format.md) | 标准正文：文件结构 → 元数据 → 参数字典（耗材/冷却/参数覆盖/高级/材料/依赖）→ 一致性要求 |
| [工艺预设文件格式要求 v1.0（草案）](preset/preset_process_format.md) | 标准正文：文件结构 → 元数据 → 参数字典（质量/强度/速度/支撑/材料/其他）→ 一致性要求 |
| [打印机预设文件格式要求 v1.0（草案）](preset/preset_machine_format.md) | 标准正文：文件结构 → 元数据 → 参数字典（基础信息/打印机G-code/移动能力/挤出机/材料/注释）→ 一致性要求 |

## 研发内部资料（证据链）

[docs/](../docs/) 目录是阶段一盘点与对齐的原始工作文档，wiki 页面的结论都能在这里找到证据：

| 文档 | 内容 |
|---|---|
| [01-现状盘点-切片软件3mf配置文件](../docs/01-现状盘点-切片软件3mf配置文件.md) | 7 个导出样本实测 + Metadata 条目全景 |
| [02-字段字典对账-project_settings](../docs/02-字段字典对账-project_settings.md) | 源码定义 × 样本落盘逐项对账 |
| [03-现状盘点-model_settings与嵌入预设](../docs/03-现状盘点-model_settings与嵌入预设.md) | 三层字段实测 + 嵌入预设文件 |
| [04-问题清单-切片软件团队对齐](../docs/04-问题清单-切片软件团队对齐.md) | 进入阶段二（规范设计）前待裁决的 Q1–Q22 |
| [06-对账-gcode.3mf与3MF-Toolpath扩展](../docs/06-对账-gcode.3mf与3MF-Toolpath扩展.md) | gcode.3mf 与 3MF 联盟 Toolpath RC 逐机制对账（2026-11-04） |
| [07-对账-设置键UI覆盖度](../docs/07-对账-设置键UI覆盖度.md) | UI 设置键 × wiki 键页面对账：FDM 挂行键 100% 覆盖，缺口 0（2026-11-06） |
| [08-盘点-预设文件组织与继承实测](../docs/08-盘点-预设文件组织与继承实测.md) | Snapmaker 预设 547 个 JSON 实测：三树层级、键数、三种组织风格与勘误（2026-11-06） |
| [09-对账-PrintConfig元数据提取与键页注入](../docs/09-对账-PrintConfig元数据提取与键页注入.md) | 键页默认值/范围/单位/别名元数据的脚本化提取与注入，含缺键清单与复跑方法（2026-11-06） |
| [10-对账-预设格式文档与参数页面](../docs/10-对账-预设格式文档与参数页面.md) | 三份预设格式文档 × 参数页面 × 系统预设字段三方对账；补入 18 个在用键并标注页面待修项（2026-11-23） |

## 设置参数文档

按软件实际 UI 每「键」一文档，内容优先参照上游 OrcaSlicer wiki 对应小节，上游未收录的建占位页（附软件内置元数据）：

| 总览页 | 覆盖范围 |
|---|---|
| [打印机设置参数总览](settings/printer/printer_overview.md) | 6 页面 104 键 |
| [耗材设置参数总览](settings/filament/filament_overview.md) | 7 页面 107 键（含 18 个回抽覆盖交叉引用） |
| [工艺设置参数总览](settings/process/process_overview.md) | 6 页面 311 键 + Plate Settings 板级键 |

键页元数据行（Mode / Variables / Type / Defaults / Ranges / Aliases / CLI Example）的含义见支撑页：[Mode 显示模式](general_settings/option_mode.md) · [Type 取值类型](general_settings/option_type.md) · [内置占位符变量](developer_reference/built_in_placeholders_variables.md) · [CLI 命令行](cli/cli_mode.md)

## 规划中

- 3mf 工程文件规范定稿：P0 项闭环后替换正文中的「待裁决」标注（见 [docs/04](../docs/04-问题清单-切片软件团队对齐.md)）
- fork 完整使用文档：在上述三个设置目录基础上继续扩展（见 [AGENTS.md](../AGENTS.md) 目录表）

## 参与贡献

写新页面前先读 [AGENTS.md](../AGENTS.md)：命名、链接、图片、目录归属等约定。
