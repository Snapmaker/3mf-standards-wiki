# adaptive_pressure_advance_bridges

> 所在界面：耗材设置 → Filament → Flow ratio and Pressure Advance
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_flow_ratio_and_pressure_advance.md` 的「Pressure advance for bridges」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

#### Pressure advance for bridges

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `adaptive_pressure_advance_bridges`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--adaptive-pressure-advance-bridges=1`.  
Pressure advance value for bridges. Set to 0 to disable.  
A lower PA value when printing bridges helps reduce the appearance of slight under extrusion immediately after bridges.  
This is caused by the pressure drop in the nozzle when printing in the air and a lower PA helps counteract this.
