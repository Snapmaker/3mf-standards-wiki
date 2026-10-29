# full_fan_speed_layer

> 所在界面：耗材设置 → Cooling → Cooling for specific layer
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Full fan speed at layer」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Full fan speed at layer

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `full_fan_speed_layer`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--full-fan-speed-layer=1`.  
Fan speed is increased linearly from 0% starting at the layer specified by [close_fan_the_first_x_layers](#no-cooling-for-the-first) up to the maximum part-cooling speed at this specified layer.  
If this layer is less than or equal to [close_fan_the_first_x_layers](#no-cooling-for-the-first), it is ignored and the fan will reach the maximum allowed speed on the layer immediately after [close_fan_the_first_x_layers](#no-cooling-for-the-first) (i.e. at layer [close_fan_the_first_x_layers](#no-cooling-for-the-first) + 1).  
Set this option to `0` to disable the automatic ramp.
