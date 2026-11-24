# filament_deretraction_speed

> Location: Filament → Setting Overrides → Retraction → De-retraction Speed
> Also in this section: `filament_retraction_length`, `filament_z_hop`, `filament_z_hop_types`, `filament_retract_lift_above`, `filament_retract_lift_below`, `filament_retract_lift_enforce`, `filament_retraction_speed`, `filament_retract_restart_extra`, `filament_retraction_minimum_travel`, `filament_retract_when_changing_layer`, `filament_wipe`, `filament_wipe_distance`, `filament_retract_before_wipe`, `filament_long_retractions_when_cut`, `filament_retraction_distances_when_cut`, `filament_retract_length_toolchange`, `filament_retract_restart_extra_toolchange` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_deretraction_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[Unit](../../../general_settings/option_type.md#unit): `mm/s`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-deretraction-speed=1`.  

How fast the filament is pushed back into the nozzle after a retraction. Zero means the same speed as retraction.

This is the filament-level counterpart of the printer parameter [De-retraction Speed](../../printer/extruder/deretraction_speed.md), so one material can reload at a different speed than another. The checkbox in front of the field decides which value applies to this filament:

- **Unchecked** — no value is stored for this filament (`nil` in the preset file). The field is greyed out, shows the printer's value, and that value is used.
- **Checked** — the value entered here is used for this filament instead of the printer's value.

The value is a list with one entry per extruder. A filament that supports more than one flow type (for example standard and High Flow) keeps a separate value for each flow type; the value of the flow type selected for the extruder applies.
