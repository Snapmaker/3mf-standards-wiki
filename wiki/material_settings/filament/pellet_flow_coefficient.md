# pellet_flow_coefficient

> 所在界面：耗材设置 → Filament → Flow ratio and Pressure Advance
> 状态：占位——上游 OrcaSlicer wiki 未收录，待补充。
> 显隐条件（初步梳理，待校对）：仅 pellet（粒料）机型显示

## 基本信息（来自 fork `PrintConfig.cpp`）

- 标签：Pellet flow coefficient
- 类型：coFloats
- 默认值：0.4157
- 可见模式：-

> 工具提示原文：Pellet flow coefficient is empirically derived and allows for volume calculation for pellet printers.\n\nInternally it is converted to filament_diameter. All other volume calculations remain the same.\n\nfilament_diameter = sqrt( (4 * pellet_flow_coefficient) / PI )

（待补：参数作用、取值范围、与同类参数的关系、适用场景）
