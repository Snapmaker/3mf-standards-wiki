# initial_layer_jerk

> Location: Process → Speed → Jerk(XY)
> Also in this section: `graphic_effect_plate_temp_initial_layer` (each documented on its own page).

---

### Initial layer

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `initial_layer_jerk`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `9`.  
[Unit](../../../general_settings/option_type.md#unit): `mm/s`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--initial-layer-jerk=1`.  

Jerk for initial layer printing. This is usually set to a lower value than top surface to improve adhesion.
