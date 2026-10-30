# prime_volume

> Location: Process → Multimaterial → Prime tower

---

## Prime volume

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `prime_volume`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--prime-volume=1`.  
Volume of material, in mm³, printed on the prime tower after each tool change to prime the new extruder. Default is 45 mm³.

Unless the printer is a single extruder multi-material printer with [Purge in prime tower](../../printer/multimaterial/printer_multimaterial_wipe_tower.md#purge-in-prime-tower) enabled, the Type 2 tower purges this fixed volume at each tool change instead of the flushing volumes. On such printers the tower purges the flushing volumes and this option is hidden. The Type 1 tower takes the prime volume from each filament profile and uses this value only as a fallback.
