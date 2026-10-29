# fan_max_speed

> 所在界面：耗材设置 → Cooling → Part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Material Part Cooling Fan」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`fan_min_speed`、`fan_cooling_layer_time`、`slow_down_layer_time`（各另有独立文档）。

---

## Material Part Cooling Fan

[Mode](option_mode): `Simple`.  
[Variables](built_in_placeholders_variables): `fan_min_speed`, `fan_cooling_layer_time`, `fan_max_speed`, `slow_down_layer_time`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--fan-min-speed=1` (same pattern for the other variables above).  
These settings control the behavior of the part cooling fan during printing. Proper configuration of these parameters can significantly enhance print quality by optimizing cooling for different features and layer times.
