# initial_layer_infill_speed

> Location: Process → Speed → Initial layer speed

---

## Initial layer infill

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `initial_layer_infill_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `60`.  
[Range](../../../general_settings/option_type.md#range): `≥ 1` mm/s.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--initial-layer-infill-speed=1`.  
Defines the speed used for everything on the first layer except walls and brim, mainly the [solid infill](../../process/strength/bottom_shell_layers.md) regions. These areas require more precise and consistent extrusion to create a flat and stable surface for subsequent layers. Printing this section too fast may result in high internal stresses (increased risk of warping), poor layer uniformity, or adhesion failures.
