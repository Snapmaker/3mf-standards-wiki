# filament_z_hop_types

> Location: Filament → Setting Overrides → Retraction → Z-hop type
> Also in this section: `filament_retraction_length`, `filament_z_hop`, `filament_retract_lift_above`, `filament_retract_lift_below`, `filament_retract_lift_enforce`, `filament_retraction_speed`, `filament_deretraction_speed`, `filament_retract_restart_extra`, `filament_retraction_minimum_travel`, `filament_retract_when_changing_layer`, `filament_wipe`, `filament_wipe_distance`, `filament_retract_before_wipe`, `filament_long_retractions_when_cut`, `filament_retraction_distances_when_cut`, `filament_retract_length_toolchange`, `filament_retract_restart_extra_toolchange` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_z_hop_types`.  
[Type](../../../general_settings/option_type.md#list-types): `Choice list`.  
[Default](../../../general_settings/option_type.md#default-value): `ZHopType::zhtSlope`.  
[Options](../../../general_settings/option_type.md#choice): `Auto Lift, Normal Lift, Slope Lift, Spiral Lift`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-z-hop-types=value`.  

The motion used to lift the nozzle for the Z-hop: `Auto Lift` picks between the other types based on the travel move, `Normal Lift` raises the nozzle straight up, `Slope Lift` moves diagonally, and `Spiral Lift` spirals upward, which can help with stringing.

This is the filament-level counterpart of the printer parameter [Z-hop Type](../../printer/extruder/z_hop_types.md), so one material can lift differently from another. The checkbox in front of the field decides which value applies to this filament:

- **Unchecked** — no value is stored for this filament (`nil` in the preset file). The field is greyed out, shows the printer's value, and that value is used.
- **Checked** — the value entered here is used for this filament instead of the printer's value.

The value is a list with one entry per extruder. A filament that supports more than one flow type (for example standard and High Flow) keeps a separate value for each flow type; the value of the flow type selected for the extruder applies.
