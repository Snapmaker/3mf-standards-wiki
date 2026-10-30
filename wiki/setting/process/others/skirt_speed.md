# skirt_speed

> Location: Process → Others → Skirt

---

## Speed

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `skirt_speed`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--skirt-speed=1`.  
Printing speed for the skirt in mm/s. Set to 0 to use the [First layer infill](../../process/speed/speed_settings_initial_layer_speed.md#initial-layer-infill) speed on the first layer and the [Support](../../process/speed/speed_settings_other_layers_speed.md#support) speed on higher layers.  
Slower speeds give a more reliable prime; very fast skirt speeds may not adhere properly and come off, causing problems with the part.
