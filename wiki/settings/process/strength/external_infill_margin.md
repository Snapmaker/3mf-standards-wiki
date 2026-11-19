# external_infill_margin

> Location: Process → Strength → Infill
> 状态：占位——待补充。

## 基本信息（来自 fork `PrintConfig.cpp`）

- 标签：Anchor solid infill by X mm
- 类型：coFloatOrPercent，单位 mm or %（% 相对 [`line_width`](../quality/line_width.md)），min 0（max_literal 50）
- 默认值：（空，即不外扩）
- 可见模式：Advanced

> 工具提示原文：This parameter grows the top/bottom/solid layers by the specified mm to anchor them into the sparse infill and support the perimeters above. Can be a %% of the width of the perimeters.

## 说明

把顶/底/实心填充层向外扩指定的毫米数（或线宽百分比），让实心填充锚进稀疏填充、更好支撑上方外墙。留空表示不外扩。

与 [`infill_anchor`](infill_anchor.md) 的区别：后者控制稀疏填充线端头往内墙上的锚接长度，本键控制实心填充的外扩量。

（待补：推荐取值、对顶面质量的影响）
