# filament_toolchange_delay

> 所在界面：耗材设置 → Multimaterial → Tool change parameters with single extruder MM printers
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/multimaterial/material_multimaterial.md` 的「Delay after unloading」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Delay after unloading

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filament_toolchange_delay`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-toolchange-delay=1`.  
Time to wait after the filament is unloaded. May help to get reliable tool changes with flexible materials that may need more time to shrink to original dimensions.
