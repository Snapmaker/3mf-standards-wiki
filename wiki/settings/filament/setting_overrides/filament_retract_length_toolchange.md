# filament_retract_length_toolchange

> Location: Filament → Setting Overrides → Retraction → Retraction Length (Toolchange)
> Also in this section: `filament_retraction_length`, `filament_z_hop`, `filament_z_hop_types`, `filament_retract_lift_above`, `filament_retract_lift_below`, `filament_retract_lift_enforce`, `filament_retraction_speed`, `filament_deretraction_speed`, `filament_retract_restart_extra`, `filament_retraction_minimum_travel`, `filament_retract_when_changing_layer`, `filament_wipe`, `filament_wipe_distance`, `filament_retract_before_wipe`, `filament_long_retractions_when_cut`, `filament_retraction_distances_when_cut`, `filament_retract_restart_extra_toolchange` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_retract_length_toolchange`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `10`.  
[Unit](../../../general_settings/option_type.md#unit): `mm`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-retract-length-toolchange=1`.  

How far this filament is pulled back for a tool change in a multi-material print. The length is measured on the raw filament before it enters the extruder, and it is used instead of the regular [Retraction Length](../../printer/extruder/retraction_length.md) for that retraction.

This is the filament-level counterpart of the printer parameter [Retraction Length (Toolchange)](../../printer/extruder/retract_length_toolchange.md), so one material can use a different tool-change retraction than another. The checkbox in front of the field decides which value applies to this filament:

- **Unchecked** — no value is stored for this filament (`nil` in the preset file). The field is greyed out, shows the printer's value, and that value is used.
- **Checked** — the value entered here is used for this filament instead of the printer's value.

The value is a list with one entry per extruder. A filament that supports more than one flow type (for example standard and High Flow) keeps a separate value for each flow type; the value of the flow type selected for the extruder applies.

The value is written to the G-code config block under the same key name, with one entry per extruder. It is one of the fields the printer reads from the G-code: field 21 in the [interaction fields reference](../../../specification/gcode.3mf/gcode_3mf_interaction_fields.md#1-字段总表).
