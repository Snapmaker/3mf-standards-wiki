# filament_retraction_distances_when_cut

> Location: Filament → Setting Overrides → Retraction → Retraction distance when cut
> Also in this section: `filament_retraction_length`, `filament_z_hop`, `filament_z_hop_types`, `filament_retract_lift_above`, `filament_retract_lift_below`, `filament_retract_lift_enforce`, `filament_retraction_speed`, `filament_deretraction_speed`, `filament_retract_restart_extra`, `filament_retraction_minimum_travel`, `filament_retract_when_changing_layer`, `filament_wipe`, `filament_wipe_distance`, `filament_retract_before_wipe`, `filament_long_retractions_when_cut`, `filament_retract_length_toolchange`, `filament_retract_restart_extra_toolchange` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_retraction_distances_when_cut`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `18`.  
[Range](../../../general_settings/option_type.md#range): `[10, 18]`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-retraction-distances-when-cut=1`.  

Experimental. The retraction length used before the filament is cut during a material change.

This is the filament-level counterpart of the printer parameter [Retraction Distance When Cut](../../printer/extruder/retraction_distances_when_cut.md), so one material can use a different cut distance. The checkbox in front of the field decides which value applies to this filament:

- **Unchecked** — no value is stored for this filament (`nil` in the preset file). The field is greyed out, shows the printer's value, and that value is used.
- **Checked** — the value entered here is used for this filament instead of the printer's value.

The value is a list with one entry per extruder, like the printer setting.

The override only takes effect when the printer's long-retraction-on-cut setting lets the filament decide and this filament's [Long Retraction When Cut](filament_long_retractions_when_cut.md) is on; otherwise the checkbox is greyed out.
