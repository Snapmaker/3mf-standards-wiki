# filament_tower_interface_print_temp

> Location: Filament → Filament → Basic information
> 显隐条件（初步梳理，待校对）：仅 Snapmaker U1 机型显示
> 本小节同时涵盖：`filament_tower_interface_pre_extrusion_dist`、`filament_tower_interface_pre_extrusion_length`、`filament_tower_ironing_area`、`filament_minimal_purge_on_wipe_tower`（各另有独立文档）。

---

## Multimaterial Wipe Tower Parameters

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_tower_interface_print_temp`.  
[Type](../../../general_settings/option_type.md): Integer list.  
[Default](../../../general_settings/option_type.md#default-value): `-1`.  
[Range](../../../general_settings/option_type.md#range): `≥ -1` °C.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-tower-interface-print-temp=1`.  
Wipe towers are sacrificial structures printed alongside the main object to purge excess material from the nozzle after a tool change in multimaterial printing. This ensures that the next extrusion uses the correct filament color or type without contamination from the previous material.
