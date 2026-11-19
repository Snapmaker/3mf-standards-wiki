# nozzle_temperature_initial_layer

> Location: Filament → Filament → Print temperature
> Also in this section: `nozzle_temperature` (each documented on its own page).
> G-code embedded name: `first_layer_temperature` (the gcode comment section writes the old name while the value comes from this key; both old and new names exist as custom g-code placeholders).

---

## Nozzle

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `nozzle_temperature_initial_layer`.  
[Type](../../../general_settings/option_type.md#list-types): `Integer list`.  
[Default](../../../general_settings/option_type.md#default-value): `200`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` ℃.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--nozzle-temperature-initial-layer=1`.  
One of the most critical settings for successful 3D printing is the nozzle temperature.  
The correct nozzle temperature ensures proper melting and extrusion of the filament, leading to good layer adhesion and overall print quality.  
You can set a higher temperature for the first layer to improve bed adhesion but be cautious with deformations as [elephant foot](../../process/quality/elefant_foot_compensation.md).
