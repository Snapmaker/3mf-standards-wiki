# initial_layer_speed

> Location: Process → Speed → Initial layer speed

---

## Initial layer

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `initial_layer_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--initial-layer-speed=1`.  
This setting determines the printing speed of the [outer/inner walls](../../process/strength/strength_settings_walls.md) and the brim on the first layer.  
All other first layer extrusions, such as [solid infill](../../process/strength/strength_settings_top_bottom_shells.md) and the [sparse infill](../../process/strength/strength_settings_infill.md) printed when [bottom layers](../../process/strength/strength_settings_top_bottom_shells.md#shell-layers) is set to 0, use the [First layer infill](#initial-layer-infill) speed.  
Adjusting this speed helps ensure proper adhesion and print quality for the initial layer.
