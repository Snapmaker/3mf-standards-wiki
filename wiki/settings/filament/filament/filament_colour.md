# filament_colour

> Location: Filament → Filament → Basic information
> 状态：占位——待补充。
> 注意：本键不渲染在耗材页签内，编辑入口在准备视图左侧面板的耗材列表色块（见下文）。

## 基本信息（来自 fork `PrintConfig.cpp`）

- 标签：Color
- 类型：coStrings（GUIType=color，每槽位一个 `#RRGGBB` 颜色串）
- 默认值：#F2754E
- 可见模式：Advanced

> 工具提示原文：Only used as a visual help on UI.

## 在哪里编辑

耗材设置页签（`Tab.cpp`）不构建此键。实际入口：

- **准备视图左侧面板的耗材列表**，每个耗材槽位一行，行首色块即本键。点击弹出颜色选择对话框（fork 的 `FilamentColorDialog`，支持颜色库、双拼/渐变多色；无匹配颜色库条目时回退系统 `wxColourDialog`"Please choose the filament color"）。
- 改动写入 `project_config` 的 `filament_colour[槽位]`，即**项目级、按槽位**生效，而非耗材预设参数。

## 作用与关联

- 仅作 UI 视觉辅助：3D 预览按它渲染各槽位模型颜色，不影响切片结果。
- 随工程保存进 3mf，并逐槽位写入 gcode 注释：`; filament_colour = #F4E2C1;#00C1AE;...`（飞书《gcode 字段交互协议》表 1 收录）。
- 与 [`default_filament_colour`](default_filament_colour.md) 的区别：后者是耗材预设的默认色（页签 Basic information），本键是当前工程各槽位实际生效色，载入预设时取后者作初值。
- 混色体系：`filament_colour` 是槽位"物理色"，`filament_multi_colors`/`filament_colour_mode`（Snapmaker V2.3.5 扩展）描述双拼/渐变展示色。

（待补：与 AMS 槽位同步、颜色库匹配规则）
