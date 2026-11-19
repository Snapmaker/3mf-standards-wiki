# travel_short_distance_acceleration

> Location: Process → Speed → Acceleration
> 状态：占位——上游 OrcaSlicer wiki 未收录，fork 新增参数，待补充。

## 基本信息（来自 fork `PrintConfig.cpp`）

- 标签：Short travel
- 类型：coFloats，单位 mm/s²，min 0
- 默认值：250
- 可见模式：Developer

> 工具提示原文：Acceleration used for short travel moves near external perimeters. Short travels are moves shorter than the 'Retraction minimum travel' distance.
> Lower values (e.g., 250-500 mm/s²) reduce ringing artifacts on sharp corners without significantly impacting print time.
> Set to 0 to disable (uses normal travel acceleration).

## 说明

外墙附近**短移动**的加速度。"短"的定义是小于耗材的 [Retraction minimum travel](../../filament/setting_overrides/filament_retraction_minimum_travel.md)（`filament_retraction_minimum_travel`）距离的空驶。

调低（如 250–500 mm/s²）可减少尖角处的振纹（ringing）且几乎不影响打印时间；设 0 表示关闭、退回普通 [`travel_acceleration`](travel_acceleration.md)。

（待补：与 input shaping 的配合）
