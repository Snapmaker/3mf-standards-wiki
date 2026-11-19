# enable_overlap_area_carving

> Location: Process → Others → Special mode
> 状态：占位——上游 OrcaSlicer wiki 未收录，fork 新增参数，待补充。

## 基本信息（来自 fork `PrintConfig.cpp`）

- 标签：Carve overlaps by per-layer slice area
- 类型：coBool
- 默认值：false
- 可见模式：Developer

> 工具提示原文：When enabled, overlaps between multi-extruder parts are carved with the new algorithm: on each layer, the part with the smaller slice area owns the overlap, keeping small details intact inside larger bodies. Developer option.

## 说明

多挤出机零件重叠区域的挖除算法开关。开启后改用新算法：每一层上**截面面积更小的零件**拥有重叠区，使大零件内部的小零件细节得以保留。位于 Special mode 组 [`slicing_mode`](slicing_mode.md) 之后。

（待补：新旧算法差异示意、对装配公差的影响）
