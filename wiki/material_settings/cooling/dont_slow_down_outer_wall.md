# dont_slow_down_outer_wall

> 所在界面：耗材设置 → Cooling → Part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Don't slow down outer walls」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：需先启用 slow_down_for_layer_cooling 后显示

---

### Don't slow down outer walls

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `dont_slow_down_outer_wall`.  
[Type](option_type#list-types): `Boolean list`.  
[CLI Example](cli_mode#setting-overrides): `--dont-slow-down-outer-wall=1`.  
If enabled, this setting will ensure external perimeters are not slowed down to meet the minimum layer time. This is particularly helpful in the below scenarios:

1. To avoid changes in shine when printing glossy filaments
2. To avoid changes in external wall speed which may create slight wall artifacts that appear like Z banding
3. To avoid printing at speeds which cause VFAs (fine artifacts) on the external walls

When enabled, the outer walls are left out of the slowdown: they always print at their [outer wall speed](speed_settings_other_layers_speed#outer-wall) and their time counts as fixed time, like travels.

The whole missing time is then taken from the rest of the extrusions, so:

- Inner walls, infill and other features are slowed down more than they would be otherwise, and can end up slower than the outer wall.
- [Min print speed](#min-print-speed) is reached sooner, so small layers are more likely to finish faster than the Layer time.
- Overhang walls are still slowed down, as they are a different feature from the outer wall.

Using the [previous example](#how-the-slowdown-is-calculated) with a Layer time of 22 s (12 s missing):

| Feature | Without the option | With the option |
| --- | --- | --- |
| Outer wall | 95.2 mm/s | 100 mm/s |
| Inner wall | 95.2 mm/s | 94.7 mm/s |
| Sparse infill | 95.2 mm/s | 94.7 mm/s |

Without the option, the cap reaches the outer wall and all three print at $\frac{2000}{9 + 12} \approx 95.2$ mm/s.  
With it, the outer wall keeps its 100 mm/s and the inner wall and infill drop to $\frac{1800}{7 + 12} \approx 94.7$ mm/s.

This keeps the outer surface consistent between layers at the cost of less cooling time on small layers.
