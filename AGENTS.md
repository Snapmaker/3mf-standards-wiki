# AGENTS.md — 本仓库 wiki 约定

本仓库是团队 wiki（3MF 专题先行，后续扩展为软件完整文档）。人类贡献者和 AI 都遵守本文件。

## 目录结构

顶级目录即分类法。新页面放进匹配的目录；没有合适的目录时先在 AGENTS.md/home.md 登记再建。

| 目录 | 状态 | 放什么 |
|---|---|---|
| `wiki/specification/3mf/` | 现有 | 3MF 文件格式专题：`3mf_standard.md` 为工程文件规范正文，`3mf documents/` 子目录放现状盘点类文档（文件结构、配置文件解析、版本管理细则） |
| `wiki/specification/gcode.3mf/` | 现有 | gcode.3mf 嵌入式格式专题：`gcode_3mf_standard.md` 容器规范、`gcode_standard.md` G-code 文件规范、`gcode_3mf_interaction_fields.md` 两端交互字段对照 |
| `wiki/images/` | 按需建 | wiki 图片集中存放，按主题建子目录 |
| `wiki/settings/printer/` `wiki/settings/filament/` `wiki/settings/process/` | 现有 | 设置参数每键一文档。子目录名按软件 UI 三个设置标签页（Printer/Filament/Process）命名，对应上游 wiki 的 `printer_settings`/`material_settings`/`print_settings` |
| `wiki/preset/` | 现有 | 预设体系文档：命名与继承规范，耗材/工艺/打印机预设文件格式标准 |
| `wiki/general_settings/` `wiki/cli/` `wiki/developer_reference/` | 现有（支撑页） | 键页元数据支撑页（`option_mode` / `option_type` / `built_in_placeholders_variables` / `cli_mode`，2026-11-19 自上游移植并修订）；其余内容随软件完整文档阶段扩充，**目录名与上游 OrcaSlicer wiki 一致** |
| `wiki/print_prepare/` `wiki/calibration/` `wiki/guides/` `wiki/releases/` | 预留 | 软件完整文档阶段启用，**目录名与上游 OrcaSlicer wiki 一致**，便于对照迁移 |

## 命名

- 文件名全小写 `snake_case`：`[a-z0-9]` 单词以 `_` 连接（如 `3mf_project_settings.md`）
- 同一专题的页面带组前缀（3MF 专题统一 `3mf_` 前缀；校准类可用 `_calib` 后缀，参照上游）
- 文件名保持全局唯一（不只在同目录内唯一），为将来迁 GitHub Wiki / mkdocs 扁平 URL 留余地
- 文件名用英文，正文用中文

## 内链

- 用相对路径带 `.md` 扩展名：`[参数覆盖](3mf_model_settings.md)`
- 锚点用 kebab-case 指向真实标题（标题里的编号和空格都算）：`[x](3mf_file_structure.md#3-每个文件的作用)`
- 独立页面（专题、规范正文、总览页）标题下第二行放面包屑：`← [Wiki 首页](../home.md)`（层级更深时相应加 `../`）
- 设置键页面（`wiki/settings/`）用 `> Location: Tab → 分组 → UI 区块` 行替代面包屑
- **孤儿页规则**：新页面必须被 `wiki/home.md`（或其他页面）链接，否则不许合入——没有入口的页面等于不存在

## 图片

- wiki 图片放 `wiki/images/<主题>/`，不要散在页面旁边
- 用相对路径引用，alt 文本必填且描述内容：`![打印板预览示例](images/3mf/plate_preview.png)`
- **图片一律本地化：不得直链上游仓库**（OrcaSlicer_WIKI 等外链图床），先下载进 `wiki/images/` 再引用
- 纯文字能说清的（表格、公式、代码）不用图片

## 链接

- **正文不得链接到 OrcaSlicer 上游原始路径**（wiki 页 / PR / issue / release）：有本地对应页的改链本地页，没有的写纯文字（如"upstream PR 12669"）；上游资料作"深入阅读"引用时同样只留文字描述不放超链

## Callouts

用 GitHub alerts 语法，不要用加粗/引用块 improvisation。**标记 `[!NOTE]` 等必须独占一行**（后面接文字 GitHub 不渲染成 alert，标记会原样露出）；标题写第二行，可加粗：

```markdown
> [!NOTE]
> **标题（可选）**
> 内容
```

## 文风

- wiki 面向新人：简洁、说人话，一页讲清一件事；长页顶部放目录
- 证据链（样本清单、逐项对账、代码行号）不放 wiki 正文，留在内部工作记录
- **不暴露实现细节**：`wiki/settings/` 键页与总览页、`wiki/general_settings/` `wiki/cli/` `wiki/developer_reference/` 支撑页不写源文件名/类名/原始类型名（`coXxx`）/仓库路径，指称软件时用"软件 / 当前软件版本 / Snapmaker Orca"；规范正文（`specification/`）引用源码仍按下文"源码引用"规则执行
- 涉及未定论的结论，标注"待定"，不要写成已定论
- **例外**：`wiki/settings/` 目录页面正文**全英文**（含占位页模板与总览页），标注行用英文（`> Status:` / `> Visibility:` / `> G-code embedded name:` / `> Also in this section:`）

## 源码引用

引用源码时写相对路径 + 文件定位，不写绝对路径（各人 checkout 位置不同）：

```markdown
序列化代码位于 `src/libslic3r/Format/bbs_3mf.cpp`（Snapmaker Orca 源码）
```
