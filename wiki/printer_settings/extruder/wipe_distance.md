# wipe_distance

> 所在界面：打印机设置 → Extruder N → Retraction
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_retraction.md` 的「Wipe distance」小节（2026-10-28），英文原文，待本地化校对。

---

## Wipe distance

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wipe_distance[extruder_idx]`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--wipe-distance=1`.  
Describe how long the nozzle will move along the last path when retracting.  
Depending on how long the wipe operation lasts, how fast and long the extruder/filament retraction settings are, a retraction move may be needed to retract the remaining filament.
Setting a value in the retract amount before wipe setting below will perform any excess retraction before the wipe, else it will be performed after.
