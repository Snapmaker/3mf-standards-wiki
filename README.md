# 3mf-standards-wiki

Snapmaker Orca 的文件格式规范与设置参数文档：讲清楚 3mf 文件里有什么、为什么是这样，并逐步扩展为软件的完整使用文档。

## 内容

| 专题 | 文档 |
|---|---|
| 3MF 工程文件 | [工程文件规范 v1.0（草案）](wiki/specification/3mf/3mf_standard.md) · [project_settings.config](wiki/specification/3mf/project_settings_config.md) · [model_settings.config](wiki/specification/3mf/model_settings_config.md) · [3MF 版本管理细则](wiki/specification/3mf/3mf_version_management.md) |
| gcode.3mf | [gcode.3mf 规范 v1.0（草案）](wiki/specification/gcode.3mf/gcode_3mf_standard.md) · [G-code 文件规范 v1.0（草案）](wiki/specification/gcode.3mf/gcode_standard.md) · [两端交互字段对照](wiki/specification/gcode.3mf/gcode_3mf_interaction_fields.md) |
| 预设 | [打印配置文件命名与继承规范 v1.0（草案）](wiki/preset/configuration_files.md) · [耗材预设文件格式](wiki/preset/preset_filament_format.md) · [工艺预设文件格式](wiki/preset/preset_process_format.md) · [打印机预设文件格式](wiki/preset/preset_machine_format.md) |
| 设置参数 | [打印机](wiki/settings/printer/printer_overview.md) · [耗材](wiki/settings/filament/filament_overview.md) · [工艺](wiki/settings/process/process_overview.md) 设置参数总览 |

各专题的阅读顺序和页面说明见 [Wiki 首页](wiki/home.md)。

各规范正文均为 v1.0 草案，未定论的内容按现状描述并标注「待定」。设置参数页为英文，其余页面为中文。

## 仓库结构

```
wiki/
├── home.md               ← Wiki 首页，所有页面的入口
├── specification/        ← 格式规范：3mf/、gcode.3mf/
├── preset/               ← 预设：命名与继承规范，耗材 / 工艺 / 打印机预设文件格式
├── settings/             ← 设置参数，每键一页：printer/、filament/、process/
├── general_settings/     ← 支撑页：显示模式与取值类型
├── cli/                  ← 支撑页：命令行切片
├── developer_reference/  ← 支撑页：内置占位符变量
└── images/               ← 图片
AGENTS.md                 ← 写作约定：目录、命名、链接、文风
```

## 参与贡献

新增或修改页面前，先读 [AGENTS.md](AGENTS.md)。
