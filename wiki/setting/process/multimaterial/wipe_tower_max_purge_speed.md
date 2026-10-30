# wipe_tower_max_purge_speed

> Location: Process → Multimaterial → Prime tower
> 显隐条件（初步梳理，待校对）：仅非 BBL 机型显示

---

## Maximum wipe tower print speed

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `wipe_tower_max_purge_speed`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--wipe-tower-max-purge-speed=1`.  
The maximum print speed when purging in the wipe tower and printing the wipe tower sparse layers. When purging, if the sparse infill speed or calculated speed from the filament max volumetric speed is lower, the lowest will be used instead.  
When printing the sparse layers, if the sparse infill speed or calculated speed from the filament max volumetric speed is lower, the lowest will be used instead.  
Increasing this speed may affect the tower's stability as well as increase the force with which the nozzle collides with any blobs that may have formed on the wipe tower.  
Before increasing this parameter beyond the default of 90 mm/s, make sure your printer can reliably bridge at the increased speeds and that ooze when tool changing is well controlled.  
The wipe tower external perimeters use the inner wall speed, also limited by this setting.
