# single_extruder_multi_material_priming

> 所在界面：工艺设置 → Multimaterial → Prime tower
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_prime_tower.md` 的「Prime all printing extruders」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Prime all printing extruders

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `single_extruder_multi_material_priming`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--single-extruder-multi-material-priming=1`.  
If enabled, all extruders used in the print are primed at the start of the print, before the first layer, by printing a short purge area for each of them side by side along the front edge of the bed. Only shown for printers using the Type 2 tower, and hidden when [Single Extruder Multi Material](printer_multimaterial_setup#single-extruder-multi-material) is enabled.

With Marlin firmware, the printer beeps and pauses after priming: if the print overlaps the priming area, it waits for you to remove the priming extrusions, otherwise it continues after 10 seconds. With other firmware, Orca warns when the print is too close to the priming area.
