# single_extruder_multi_material

> Location: Printer → Multimaterial → Single extruder multi-material setup

---

## Single Extruder Multi Material

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `single_extruder_multi_material`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--single-extruder-multi-material=1`.  
Allow using a single extruder to print with multiple filaments.  
If your printer has an MultiMaterialUnit, this will run the [Change filament G-code](../../printer/machine_gcode/printer_machine_gcode.md#change-filament-g-code) when changing filament is needed.
If your printer does not have an MultiMaterialUnit, you will need to enable [Manual Filament Change](#manual-filament-change).
