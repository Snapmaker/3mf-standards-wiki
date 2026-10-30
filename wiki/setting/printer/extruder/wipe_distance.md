# wipe_distance

> Location: Printer → Extruder N → Retraction

---

## Wipe distance

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `wipe_distance[extruder_idx]`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--wipe-distance=1`.  
Describe how long the nozzle will move along the last path when retracting.  
Depending on how long the wipe operation lasts, how fast and long the extruder/filament retraction settings are, a retraction move may be needed to retract the remaining filament.
Setting a value in the retract amount before wipe setting below will perform any excess retraction before the wipe, else it will be performed after.
