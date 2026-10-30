# single_extruder_multi_material_priming

> Location: Process → Multimaterial → Prime tower

---

## Prime all printing extruders

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `single_extruder_multi_material_priming`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--single-extruder-multi-material-priming=1`.  
If enabled, all extruders used in the print are primed at the start of the print, before the first layer, by printing a short purge area for each of them side by side along the front edge of the bed. Only shown for printers using the Type 2 tower, and hidden when [Single Extruder Multi Material](../../printer/multimaterial/printer_multimaterial_setup.md#single-extruder-multi-material) is enabled.

With Marlin firmware, the printer beeps and pauses after priming: if the print overlaps the priming area, it waits for you to remove the priming extrusions, otherwise it continues after 10 seconds. With other firmware, Orca warns when the print is too close to the priming area.
