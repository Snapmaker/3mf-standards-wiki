# activate_air_filtration

> 所在界面：耗材设置 → Cooling → Exhaust fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Activate air filtration」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

#### Activate air filtration

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `activate_air_filtration`.  
[Type](option_type#list-types): `Boolean list`.  
[CLI Example](cli_mode#setting-overrides): `--activate-air-filtration=1`.  
Activate for better air filtration.

G-code command: `M106 P3 S(0-255)`
