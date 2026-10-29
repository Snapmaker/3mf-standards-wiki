# filament_max_volumetric_speed

> 所在界面：耗材设置 → Filament → Volumetric speed limitation
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_volumetric_speed_limitation.md` 的「Max volumetric speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Max volumetric speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filament_max_volumetric_speed`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-max-volumetric-speed=1`.  
This setting is the volume of filament that can be melted and extruded per second. Printing speed is limited by max volumetric speed, in case of too high and unreasonable speed setting. This value cannot be zero.
