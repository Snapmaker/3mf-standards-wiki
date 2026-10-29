# filament_cooling_initial_speed

> 所在界面：耗材设置 → Multimaterial → Tool change parameters with single extruder MM printers
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/multimaterial/material_multimaterial.md` 的「Speed of the first cooling move」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Speed of the first cooling move

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filament_cooling_initial_speed`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-cooling-initial-speed=1`.  
Cooling moves are gradually accelerating beginning at this speed.
