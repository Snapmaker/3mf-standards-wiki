# single_extruder_multi_material

> 所在界面：打印机设置 → Multimaterial → Single extruder multi-material setup
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/multimaterial/printer_multimaterial_setup.md` 的「Single Extruder Multi Material」小节（2026-10-28），英文原文，待本地化校对。

---

## Single Extruder Multi Material

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `single_extruder_multi_material`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--single-extruder-multi-material=1`.  
Allow using a single extruder to print with multiple filaments.  
If your printer has an MultiMaterialUnit, this will run the [Change filament G-code](printer_machine_gcode#change-filament-g-code) when changing filament is needed.
If your printer does not have an MultiMaterialUnit, you will need to enable [Manual Filament Change](#manual-filament-change).
