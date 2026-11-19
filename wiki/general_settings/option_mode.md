# Option Mode（参数显示模式）

← [Wiki 首页](../home.md)

设置键页面元数据行的 `[Mode]` 标记该参数属于哪个显示层级——层级越高，界面上可见的参数越多。

fork 共三档，对应 `src/libslic3r/Config.hpp` 中 `ConfigOptionMode` 枚举（`comSimple` / `comAdvanced` / `comDevelop`）：

| 档位 | 显示范围 | 适合谁 |
|---|---|---|
| `Simple` | 只显示切片出活必需的核心参数 | 新手、快速打印 |
| `Advanced` | 追加常用微调参数（本 wiki 多数键页在此档） | 熟悉切片概念的用户 |
| `Develop` | 全部参数，含开发调试用、未充分测试项 | 开发、排障 |

键页的 Mode 值取自 fork `src/libslic3r/PrintConfig.cpp` 中该键定义的 `def->mode` 字段（fork 仓库 iesteem/OrcaSlicer）。

> [!NOTE] 与上游 wiki 的差异
> 上游 OrcaSlicer wiki 记为四档（Simple / Advanced / Expert / Developer）；fork 枚举是三档，无 Expert。键页中上游 `Expert` 档已统一改标为 fork 的 `Develop`（2026-11-19，[docs/09 Q4](../../docs/09-对账-PrintConfig元数据提取与键页注入.md)）。

> [!TIP]
> 档位切换入口以 fork 实际 UI 为准；上游是在 Preferences → Developer → Settings 开启 Developer Mode 后才可选 Developer 档，Develop 档下的参数不保证稳定。
