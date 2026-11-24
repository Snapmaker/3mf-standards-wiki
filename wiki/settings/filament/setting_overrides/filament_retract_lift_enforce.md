# filament_retract_lift_enforce

> Location: Filament → Setting Overrides → Retraction → On surfaces
> Also in this section: `filament_retraction_length`, `filament_z_hop`, `filament_z_hop_types`, `filament_retract_lift_above`, `filament_retract_lift_below`, `filament_retraction_speed`, `filament_deretraction_speed`, `filament_retract_restart_extra`, `filament_retraction_minimum_travel`, `filament_retract_when_changing_layer`, `filament_wipe`, `filament_wipe_distance`, `filament_retract_before_wipe`, `filament_long_retractions_when_cut`, `filament_retraction_distances_when_cut`, `filament_retract_length_toolchange`, `filament_retract_restart_extra_toolchange` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_retract_lift_enforce`.  
[Type](../../../general_settings/option_type.md#list-types): `Choice list`.  
[Default](../../../general_settings/option_type.md#default-value): `RetractLiftEnforceType ::rletAllSurfaces`.  
[Options](../../../general_settings/option_type.md#choice): `All Surfaces, Top Only, Bottom Only, Top and Bottom`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-retract-lift-enforce=value`.  

Which surfaces the Z-hop applies to: `All Surfaces`, `Top Only`, `Bottom Only` or `Top and Bottom`. It works together with the [Only Lift Z Above](filament_retract_lift_above.md) and [Only Lift Z Below](filament_retract_lift_below.md) limits.

This is the filament-level counterpart of the printer parameter [On Surfaces](../../printer/extruder/retract_lift_enforce.md), so one material can choose different surfaces than another. The checkbox in front of the field decides which value applies to this filament:

- **Unchecked** — no value is stored for this filament (`nil` in the preset file). The field is greyed out, shows the printer's value, and that value is used.
- **Checked** — the value entered here is used for this filament instead of the printer's value.

The value is a list with one entry per extruder, like the printer setting.
