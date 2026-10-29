# parking_pos_retraction

> 所在界面：打印机设置 → Multimaterial → Single extruder multi-material parameters
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/multimaterial/printer_multimaterial_semm_parameters.md` 的「Filament parking position」小节（2026-10-28），英文原文，待本地化校对。

---

## Filament parking position

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `parking_pos_retraction`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--parking-pos-retraction=1`.  
Distance of the extruder tip from the position where the filament is parked when unloaded. This should match the value in printer firmware.
