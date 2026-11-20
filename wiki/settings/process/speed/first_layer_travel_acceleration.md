# first_layer_travel_acceleration

> Location: Process → Speed → Acceleration

---

## Initial layer travel

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `first_layer_travel_acceleration`.  
[Type](../../../general_settings/option_type.md#list-types): `Float or Percentage`.  
[Default](../../../general_settings/option_type.md#default-value): `100%`.  
[Unit](../../../general_settings/option_type.md#unit): `mm/s² or %`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--first-layer-travel-acceleration=1`.  

Acceleration of [initial layer travel](../../process/speed/initial_layer_travel_speed.md).
Using a lower value can improve build plate adhesion. If the value is expressed as a percentage (e.g. 50%), it will be calculated based on the [Travel Acceleration](#travel).
