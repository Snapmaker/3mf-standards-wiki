# precise_z_height

> Location: Process → Quality → Precision

---

## Precise Z Height

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `precise_z_height`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--precise-z-height=1`.  
This feature ensures the accurate Z height of the model after slicing, even if the model height is not a multiple of the [layer height](../../process/quality/quality_settings_layer_height.md).

For example, slicing a 20mm x 20mm x 20.1mm cube with a layer height of 0.2mm would typically result in a final height of 20.2mm due to the layer height increments.

By enabling this parameter, the layer height of the last five layers is adjusted so that the final sliced height matches the actual object height, resulting in an accurate 20.1mm (as shown in the picture).

- **Precise Z Height Off**

  ![PreciseZOff](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/PreciseZOff.png?raw=true)

- **Precise Z Height On**

  ![PreciseZOn](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/PreciseZOn.png?raw=true)
