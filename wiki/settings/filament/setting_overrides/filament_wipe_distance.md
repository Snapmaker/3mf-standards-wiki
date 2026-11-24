# filament_wipe_distance

> Location: Filament → Setting Overrides → Retraction → Wipe Distance
> Also in this section: `filament_retraction_length`, `filament_z_hop`, `filament_z_hop_types`, `filament_retract_lift_above`, `filament_retract_lift_below`, `filament_retract_lift_enforce`, `filament_retraction_speed`, `filament_deretraction_speed`, `filament_retract_restart_extra`, `filament_retraction_minimum_travel`, `filament_retract_when_changing_layer`, `filament_wipe`, `filament_retract_before_wipe`, `filament_long_retractions_when_cut`, `filament_retraction_distances_when_cut`, `filament_retract_length_toolchange`, `filament_retract_restart_extra_toolchange` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_wipe_distance`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `1`.  
[Unit](../../../general_settings/option_type.md#unit): `mm`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-wipe-distance=1`.  

How far the nozzle travels along the last extrusion path while wiping.

This is the filament-level counterpart of the printer parameter [Wipe Distance](../../printer/extruder/wipe_distance.md), so one material can wipe over a different distance. The checkbox in front of the field decides which value applies to this filament:

- **Unchecked** — no value is stored for this filament (`nil` in the preset file). The field is greyed out, shows the printer's value, and that value is used.
- **Checked** — the value entered here is used for this filament instead of the printer's value.

The value is a list with one entry per extruder. A filament that supports more than one flow type (for example standard and High Flow) keeps a separate value for each flow type; the value of the flow type selected for the extruder applies.

This only matters when [Wipe While Retracting](filament_wipe.md) is on.
