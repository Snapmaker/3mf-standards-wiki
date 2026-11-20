# filament_tower_interface_pre_extrusion_dist

> Location: Filament → Filament → Basic information → Multimaterial Wipe Tower Parameters
> Visibility(preliminary, pending review): Shown only on Snapmaker U1 machines
> Also in this section: `filament_tower_interface_pre_extrusion_length`, `filament_tower_interface_print_temp`, `filament_tower_ironing_area`, `filament_minimal_purge_on_wipe_tower` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Developer`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_tower_interface_pre_extrusion_dist`.  
[Type](../../../general_settings/option_type.md): Float list.  
[Default](../../../general_settings/option_type.md#default-value): `10`.  
[Unit](../../../general_settings/option_type.md#unit): `mm`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-tower-interface-pre-extrusion-dist=1`.  

Wipe towers are sacrificial structures printed alongside the main object to purge excess material from the nozzle after a tool change in multimaterial printing. This ensures that the next extrusion uses the correct filament color or type without contamination from the previous material.
