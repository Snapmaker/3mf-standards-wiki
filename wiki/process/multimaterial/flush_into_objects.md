# flush_into_objects

> Location: Process → Multimaterial → Flush options

---

## Flush into this object

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `flush_into_objects`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--flush-into-objects=1`.  
Purging after a filament change will be done by printing this object's walls and infill with the new filament. This may lower the amount of waste and decrease the print time, but the colors of the object will be mixed as a result. Objects with this option are used for purging before the infill of other objects, and whatever they can't take is still purged on the prime tower. It will not take effect unless the prime tower is enabled. With a Type 2 [wipe tower](../../printer/multimaterial/printer_multimaterial_wipe_tower.md), purging into objects is only used on single extruder multi-material printers with [Purge in prime tower](../../printer/multimaterial/printer_multimaterial_wipe_tower.md#purge-in-prime-tower) enabled.

This is a per-object setting, so it isn't shown in the global process settings. Right-click the object in the object list or in the 3D view and check **Flush Options** > **Flush into this object**, or switch the process settings from **Global** to **Objects**, select the object and change it there. The **Flush Options** menu only appears when the plate uses more than one filament.
