# filament_minimal_purge_on_wipe_tower

> Location: Filament → Multimaterial → Wipe tower parameters
> Also in this section: `filament_tower_interface_pre_extrusion_dist`, `filament_tower_interface_pre_extrusion_length`, `filament_tower_interface_print_temp`, `filament_tower_ironing_area` (each documented on its own page).

---

## Multimaterial Wipe Tower Parameters

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_minimal_purge_on_wipe_tower`.  
[Type](../../../general_settings/option_type.md): Float list.  
[Default](../../../general_settings/option_type.md#default-value): `15`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` mm³.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-minimal-purge-on-wipe-tower=1`.  
Wipe towers are sacrificial structures printed alongside the main object to purge excess material from the nozzle after a tool change in multimaterial printing. This ensures that the next extrusion uses the correct filament color or type without contamination from the previous material.
