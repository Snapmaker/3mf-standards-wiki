# deretraction_speed

> 所在界面：打印机设置 → Extruder N → Retraction
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_retraction.md` 的「Deretraction speed」小节（2026-10-28），英文原文，待本地化校对。

---

## Deretraction speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `deretraction_speed[extruder_idx]`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--deretraction-speed=1`.  
Speed for reloading filament into the nozzle. Zero means same speed of retraction.
