# close_fan_the_first_x_layers

> 所在界面：耗材设置 → Cooling → Cooling for specific layer
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「No cooling for the first」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### No cooling for the first

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `close_fan_the_first_x_layers`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--close-fan-the-first-x-layers=1`.  
Number of initial layers during which part-cooling fans are disabled.
Disabling the fan for the first few layers improves build-plate adhesion and reduces early-layer warping.
