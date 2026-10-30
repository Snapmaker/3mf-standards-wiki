# initial_layer_travel_speed

> Location: Process → Speed → Initial layer speed

---

## Initial layer travel speed

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `initial_layer_travel_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float or Percentage list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--initial-layer-travel-speed=20%`.  
Sets the travel (non-printing movement) speed for the first layer. This doesn't affect print quality and can be set as a percentage of the [travel speed](../../process/speed/speed_settings_travel.md).  
Usually, this is set to 100% of the [travel speed](../../process/speed/speed_settings_travel.md), but it can be reduced if you want to minimize vibrations or if your printer has issues with high-speed travel movements.
