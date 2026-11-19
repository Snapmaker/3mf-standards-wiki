# cooling_slowdown_logic

> Location: Filament → Cooling → Part cooling fan
> 状态：占位——上游 OrcaSlicer wiki 未收录，fork 新增参数，待补充。
> 显隐条件：勾选 [`slow_down_for_layer_cooling`](slow_down_for_layer_cooling.md) 后显示（Tab.cpp `toggle_option`）。

## 基本信息（来自 fork `PrintConfig.cpp`）

- 标签：Cooling slowdown logic
- 类型：coEnums（单选：Uniform cooling / Consistent surface）
- 默认值：uniform_cooling
- 可见模式：Developer

> 工具提示原文：Determines how the printer slows down when minimum layer time isn't reached.
> 'Uniform cooling' slows down all print features equally (current default behavior).
> 'Consistent surface' prioritizes slowing infill and internal perimeters first, preserving external perimeter speed for better surface finish on glossy filaments. This helps reduce VFA (Vertical Fine Artifacts) and maintains consistent surface shine.

## 说明

决定最短层时间不达标时的降速策略（移植自 PrusaSlicer 2.9.3，为减少 VFA）：

- **Uniform cooling**（默认）：所有特征等比例降速，即原有行为；
- **Consistent surface**：优先降填充和内墙，尽量保住外墙速度以获得一致表面光泽；选它时配套参数 [`cooling_perimeter_transition_distance`](cooling_perimeter_transition_distance.md) 生效。

（待补：两种模式的效果对比、适用耗材）
