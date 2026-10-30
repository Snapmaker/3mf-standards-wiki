# first_layer_travel_acceleration

> Location: Process → Speed → Acceleration

---

## Initial layer travel

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `initial_layer_travel_acceleration`.  
[Type](../../general_settings/option_type.md#list-types): `Float or Percentage list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--initial-layer-travel-acceleration=20%`.  
Acceleration of [initial layer travel](../../process/speed/speed_settings_initial_layer_speed.md#initial-layer-travel-speed).
Using a lower value can improve build plate adhesion. If the value is expressed as a percentage (e.g. 50%), it will be calculated based on the [Travel Acceleration](#travel).
