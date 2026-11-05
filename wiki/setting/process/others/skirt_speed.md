# skirt_speed

> Location: Process → Others → Skirt

---

## Speed

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `skirt_speed`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--skirt-speed=1`.  
Printing speed for the skirt in mm/s. Set to 0 to use the [First layer infill](../../process/speed/initial_layer_infill_speed.md) speed on the first layer and the [Support](../../process/speed/support_speed.md) speed on higher layers.  
Slower speeds give a more reliable prime; very fast skirt speeds may not adhere properly and come off, causing problems with the part.
