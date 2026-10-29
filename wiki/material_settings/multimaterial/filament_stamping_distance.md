# filament_stamping_distance

> 所在界面：耗材设置 → Multimaterial → Tool change parameters with single extruder MM printers
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/multimaterial/material_multimaterial.md` 的「Stamping distance」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Stamping distance

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filament_stamping_distance`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-stamping-distance=1`.  
Stamping distance measured from the center of the cooling tube.
If set to non-zero value, filament is moved toward the nozzle between the individual cooling moves ("stamping"). This option configures how long this movement should be before the filament is retracted again.
