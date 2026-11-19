# overhang_totally_speed

> Location: Process → Speed → Overhang speed
> 状态：占位——待补充。
> 本键与 `overhang_1_4_speed` / `overhang_2_4_speed` / `overhang_3_4_speed` / `overhang_4_4_speed` 同属"Slow down for overhang"同一行（第 5 列，标签 100%）。

## 基本信息（来自 fork `PrintConfig.cpp`）

- 标签：100%（full_label 同）
- 类型：coFloatsOrPercents，单位 mm/s or %（% 相对 [`outer_wall_speed`](outer_wall_speed.md)），min 0
- 默认值：10
- 可见模式：Advanced

> 工具提示原文：Speed of 100% overhang wall which has 0 overlap with the lower layer.

## 说明

完全悬空（与下层 0 重叠，100% 悬垂）外墙的打印速度——即最悬的一档。上游把这种墙按桥接处理（套用 75% 档并封顶桥速），fork 单独拆出了这一档。

（待补：与 bridge_speed 的关系）
