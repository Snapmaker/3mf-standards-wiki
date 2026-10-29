# adaptive_pressure_advance_overhangs

> 所在界面：耗材设置 → Filament → Flow ratio and Pressure Advance
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_flow_ratio_and_pressure_advance.md` 的「Enable adaptive pressure advance for overhangs (beta)」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

#### Enable adaptive pressure advance for overhangs (beta)

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `adaptive_pressure_advance_overhangs`.  
[Type](option_type#list-types): `Boolean list`.  
[CLI Example](cli_mode#setting-overrides): `--adaptive-pressure-advance-overhangs=1`.  
Enable adaptive PA for overhangs as well as when flow changes within the same feature. This is an experimental option, as if the PA profile is not set accurately, it will cause uniformity issues on the external surfaces before and after overhangs.
