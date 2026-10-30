# Wiki 首页

本 wiki 讲清楚两件事：**我们的切片软件（OrcaSlicer fork）导出的 3mf 文件里有什么、为什么是这样**；后续将扩展为 fork 的完整使用文档。组织方式沿用上游 [OrcaSlicer Wiki](https://github.com/OrcaSlicer/OrcaSlicer/wiki) 的目录分类法。

## 3MF 专题

入门建议从第一篇开始按序读：

| 页面 | 内容 |
|---|---|
| [3mf 内部文件组成与作用](3mf/3mf_file_structure.md) | 入门：一个 3mf 是什么、有哪些文件、各自干什么 |
| [project_settings.config](3mf/3mf_project_settings.md) | 全局打印设置：500 多项参数怎么来的、三个值得知道的事实 |
| [model_settings.config](3mf/3mf_model_settings.md) | 对象/零件/打印板三层信息与参数覆盖优先级 |

## 研发内部资料（证据链）

[docs/](../docs/) 目录是阶段一盘点与对齐的原始工作文档，wiki 页面的结论都能在这里找到证据：

| 文档 | 内容 |
|---|---|
| [01-现状盘点-切片软件3mf配置文件](../docs/01-现状盘点-切片软件3mf配置文件.md) | 7 个导出样本实测 + Metadata 条目全景 |
| [02-字段字典对账-project_settings](../docs/02-字段字典对账-project_settings.md) | 源码定义 × 样本落盘逐项对账 |
| [03-现状盘点-model_settings与嵌入预设](../docs/03-现状盘点-model_settings与嵌入预设.md) | 三层字段实测 + 嵌入预设文件 |
| [04-问题清单-切片软件团队对齐](../docs/04-问题清单-切片软件团队对齐.md) | 进入阶段二（规范设计）前待裁决的 Q1–Q22 |

## 设置参数文档

按 fork 实际 UI 每「键」一文档，内容优先拷贝上游 OrcaSlicer wiki 对应小节，上游未收录的建占位页（附 `PrintConfig.cpp` 元数据）：

| 总览页 | 覆盖范围 |
|---|---|
| [打印机设置参数总览](printer/printer_overview.md) | 6 页面 104 键 |
| [耗材设置参数总览](filament/filament_overview.md) | 7 页面 107 键（含 18 个回抽覆盖交叉引用） |
| [工艺设置参数总览](process/process_overview.md) | 6 页面 311 键 + Plate Settings 板级键 |

## 规划中

- 3MF 规范设计（阶段二）：问题清单 P0 项闭环后开写
- fork 完整使用文档：在上述三个设置目录基础上继续扩展（见 [AGENTS.md](../AGENTS.md) 目录表）

## 参与贡献

写新页面前先读 [AGENTS.md](../AGENTS.md)：命名、链接、图片、目录归属等约定。
