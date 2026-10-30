# AGENTS.md — 本仓库 wiki 约定

本仓库是团队 wiki（3MF 专题先行，后续扩展为 OrcaSlicer fork 完整文档）。目录组织沿用上游 [OrcaSlicer Wiki](https://github.com/OrcaSlicer/OrcaSlicer_WIKI) 的分类法，按本仓库形态（仓库内纯 markdown，无构建工具）做了适配。人类贡献者和 AI 都遵守本文件。

## 目录结构

顶级目录即分类法。新页面放进匹配的目录；没有合适的目录时先在 AGENTS.md/home.md 登记再建。

| 目录 | 状态 | 放什么 |
|---|---|---|
| `wiki/3mf/` | 现有 | 3MF 文件格式专题（文件结构、配置文件解析） |
| `wiki/images/` | 按需建 | wiki 图片集中存放，按主题建子目录 |
| `wiki/printer/` `wiki/filament/` `wiki/process/` | 现有 | 设置参数每键一文档。目录名按 fork UI 三个设置标签页（Printer/Filament/Process）命名，对应上游 wiki 的 `printer_settings`/`material_settings`/`print_settings` |
| `wiki/print_prepare/` `wiki/calibration/` `wiki/general_settings/` `wiki/guides/` `wiki/cli/` `wiki/developer_reference/` `wiki/releases/` | 预留 | fork 完整文档阶段启用，**目录名与上游 OrcaSlicer wiki 一致**，便于对照迁移 |
| `docs/` | 现有（内部） | 研发证据链：盘点、对账、问题清单。不是 wiki 正文的层级，不放新人向内容 |

## 命名

- 文件名全小写 `snake_case`：`[a-z0-9]` 单词以 `_` 连接（如 `3mf_project_settings.md`）
- 同一专题的页面带组前缀（3MF 专题统一 `3mf_` 前缀；校准类可用 `_calib` 后缀，参照上游）
- 文件名保持全局唯一（不只在同目录内唯一），为将来迁 GitHub Wiki / mkdocs 扁平 URL 留余地
- 文件名用英文，正文用中文

## 内链

- 用相对路径带 `.md` 扩展名：`[参数覆盖](3mf_model_settings.md)`、指向 docs/ 用 `../../docs/` 前缀
- 锚点用 kebab-case 指向真实标题（标题里的编号和空格都算）：`[x](3mf_file_structure.md#3-每个文件的作用)`
- 每个页面标题下第二行放面包屑：`← [Wiki 首页](../home.md)`
- **孤儿页规则**：新页面必须被 `wiki/home.md`（或其他页面）链接，否则不许合入——没有入口的页面等于不存在

## 图片

- wiki 图片放 `wiki/images/<主题>/`，不要散在页面旁边
- 用相对路径引用，alt 文本必填且描述内容：`![打印板预览示例](images/3mf/plate_preview.png)`
- 纯文字能说清的（表格、公式、代码）不用图片

## Callouts

用 GitHub alerts 语法，不要用加粗/引用块 improvisation：

```markdown
> [!NOTE] 信息
> [!TIP] 技巧
> [!IMPORTANT] 关键
> [!WARNING] 注意
```

## 文风

- wiki 面向新人：简洁、说人话，一页讲清一件事；长页顶部放目录
- 证据链（样本清单、逐项对账、代码行号）不放 wiki 正文，放 `docs/`，wiki 里用"深入阅读"链接过去
- 涉及"待团队裁决"的结论，注明来源问题编号（如 docs/04 的 Q6），不要写成已定论

## 源码引用

引用 fork 源码时写相对路径 + 文件定位，不写绝对路径（各人 checkout 位置不同）：

```markdown
序列化代码位于 `src/libslic3r/Format/bbs_3mf.cpp`（fork 仓库 iesteem/OrcaSlicer）
```
