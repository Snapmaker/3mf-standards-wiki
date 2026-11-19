# cooling_perimeter_transition_distance

> Location: Filament → Cooling → Part cooling fan
> 状态：占位——fork 新增参数，待补充。
> 显隐条件：[`cooling_slowdown_logic`](cooling_slowdown_logic.md) 选为 Consistent surface 时显示。

## 基本信息（来自 fork `PrintConfig.cpp`）

- 标签：Perimeter transition distance
- 类型：coFloats，单位 mm，范围 0–50
- 默认值：10.0
- 可见模式：Developer

> 工具提示原文：Distance in millimeters before the end of slowed perimeters where the original print speed is gradually restored. This prevents visible speed transitions at the end of perimeters.
> Only applies when 'Consistent surface' cooling logic is selected.

## 说明

降速墙结束前提前多少毫米逐渐恢复原速，避免墙末尾出现可见的速度突变痕迹。仅在 [`cooling_slowdown_logic`](cooling_slowdown_logic.md) = Consistent surface 时生效。

（待补：与外墙表面质量的关系、取值经验）
