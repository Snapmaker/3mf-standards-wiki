# filament_tower_ironing_area

> Location: Filament → Filament → Basic information
> 本小节同时涵盖：`filament_tower_interface_pre_extrusion_dist`、`filament_tower_interface_pre_extrusion_length`、`filament_tower_interface_print_temp`、`filament_minimal_purge_on_wipe_tower`（各另有独立文档）。

---

## Multimaterial Wipe Tower Parameters

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `filament_minimal_purge_on_wipe_tower`, `filament_tower_interface_pre_extrusion_dist`, `filament_tower_interface_pre_extrusion_length`, `filament_tower_ironing_area`, `filament_tower_interface_purge_volume`, `filament_tower_interface_print_temp`.  
[Type](../../../general_settings/option_type.md): `filament_minimal_purge_on_wipe_tower` (Float list), `filament_tower_interface_pre_extrusion_dist` (Float list), `filament_tower_interface_pre_extrusion_length` (Float list), `filament_tower_ironing_area` (Float list), `filament_tower_interface_purge_volume` (Float list), `filament_tower_interface_print_temp` (Integer list).  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-minimal-purge-on-wipe-tower=1` (`filament_minimal_purge_on_wipe_tower` shown; other variables above follow their own type).  
Wipe towers are sacrificial structures printed alongside the main object to purge excess material from the nozzle after a tool change in multimaterial printing. This ensures that the next extrusion uses the correct filament color or type without contamination from the previous material.
