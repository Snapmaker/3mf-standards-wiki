# overhang_threshold_participating_cooling

> Location: Filament → Cooling → Part cooling fan
> 状态：占位——上游 OrcaSlicer wiki 未收录，fork 新增参数，待补充。

## 基本信息（来自 fork `PrintConfig.cpp`）

- 标签：Overhang threshold for participating cooling
- 类型：coEnums（六档：none / 1_4 / 2_4 / 3_4 / 4_4 / bridge，UI 显示 0% / 10% / 25% / 50% / 75% / 100%）
- 默认值：95%（bridge 档）
- 可见模式：Advanced

> 工具提示原文：Decide which overhang part join the cooling function to slow down the speed. Expressed as percentage which indicates how much width of the line is without support from the lower layer. 100% means forcing cooling for all outer wall no matter how much overhang degree.

## 说明

决定悬垂程度达到多少的**外墙**参与"降速散热"：百分比表示线条宽度上无下层支撑的比例。100% 表示无论悬垂角度多大，全部外墙都参与降速。

与 [`overhang_fan_threshold`](overhang_fan_threshold.md)（触发风扇提速的阈值）相邻但管的是**降速**这一侧。

> [!NOTE]
> 枚举档位 bridge 在序列化配置中写作 95%，UI 下拉显示为 100% 档。

（待补：与 slow_down_for_layer_cooling 的联动细节）
