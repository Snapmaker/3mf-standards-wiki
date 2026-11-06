# Wiki 首页

本 wiki 讲清楚两件事：**我们的切片软件（OrcaSlicer fork）导出的 3mf 文件里有什么、为什么是这样**；后续将扩展为 fork 的完整使用文档。组织方式沿用上游 [OrcaSlicer Wiki](https://github.com/OrcaSlicer/OrcaSlicer/wiki) 的目录分类法。

## 3MF 专题

入门建议从第一篇开始按序读：

| 页面 | 内容 |
|---|---|
| [3mf 内部文件组成与作用](specification/3mf/3mf%20documents/3mf_file_structure.md) | 入门：一个 3mf 是什么、有哪些文件、各自干什么 |
| [project_settings.config](specification/3mf/3mf%20documents/3mf_project_settings.md) | 全局打印设置：500 多项参数怎么来的、三个值得知道的事实 |
| [model_settings.config](specification/3mf/3mf%20documents/3mf_model_settings.md) | 对象/零件/打印板三层信息与参数覆盖优先级 |
| [3MF 版本管理细则](specification/3mf/3mf%20documents/3mf_version_management.md) | 进阶：五层版本标识、兼容性矩阵、变更检查清单 |
| [3mf 工程文件规范 v1.0（草案）](specification/3mf/3mf_standard.md) | 标准正文：包结构 → 模型部件 → 配置与三层覆盖 → 版本兼容，GB/T 体例；未闭环项按现状描述并标注待裁决（Qxx） |

## gcode.3mf 专题

切片成品包（`.gcode.3mf`，内嵌 G-code）的格式文档：

| 页面 | 内容 |
|---|---|
| [gcode.3mf 规范 v1.0（草案）](specification/gcode.3mf/gcode_3mf_standard.md) | 标准正文：总体结构 → 盘与打印数据 → 一致性要求，GB/T 体例（技术内容 = v0.9.9） |

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

## 设置参数文档

按 fork 实际 UI 每「键」一文档，内容优先拷贝上游 OrcaSlicer wiki 对应小节，上游未收录的建占位页（附 `PrintConfig.cpp` 元数据）：

| 总览页 | 覆盖范围 |
|---|---|
| [打印机设置参数总览](setting/printer/printer_overview.md) | 6 页面 104 键 |
| [耗材设置参数总览](setting/filament/filament_overview.md) | 7 页面 107 键（含 18 个回抽覆盖交叉引用） |
| [工艺设置参数总览](setting/process/process_overview.md) | 6 页面 311 键 + Plate Settings 板级键 |
| [打印配置文件：命名与继承](preset/configuration_files.md) | 入门：配置文件叫什么、元信息、参数如何复用 |

## 规划中

- 3mf 工程文件规范定稿：P0 项闭环后替换正文中的「待裁决」标注（见 [docs/04](../docs/04-问题清单-切片软件团队对齐.md)）
- fork 完整使用文档：在上述三个设置目录基础上继续扩展（见 [AGENTS.md](../AGENTS.md) 目录表）

## 参与贡献

写新页面前先读 [AGENTS.md](../AGENTS.md)：命名、链接、图片、目录归属等约定。
