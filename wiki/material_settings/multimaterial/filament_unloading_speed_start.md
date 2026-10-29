# filament_unloading_speed_start

> 所在界面：耗材设置 → Multimaterial → Tool change parameters with single extruder MM printers
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/multimaterial/material_multimaterial.md` 的「Unloading speed at the start」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Unloading speed at the start

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filament_unloading_speed_start`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-unloading-speed-start=1`.  
Speed used for unloading the tip of the filament immediately after ramming.
