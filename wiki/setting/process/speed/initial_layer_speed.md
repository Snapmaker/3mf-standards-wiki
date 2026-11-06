# initial_layer_speed

> Location: Process → Speed → Initial layer speed

---

## Initial layer

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `initial_layer_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `30`.  
[Range](../../../general_settings/option_type.md#range): `≥ 1` mm/s.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--initial-layer-speed=1`.  
This setting determines the printing speed of the [outer/inner walls](../../process/strength/wall_loops.md) and the brim on the first layer.  
All other first layer extrusions, such as [solid infill](../../process/strength/top_shell_thickness.md) and the [sparse infill](../../process/strength/sparse_infill_density.md) printed when [bottom layers](../../process/strength/bottom_shell_layers.md) is set to 0, use the [First layer infill](#initial-layer-infill) speed.  
Adjusting this speed helps ensure proper adhesion and print quality for the initial layer.
