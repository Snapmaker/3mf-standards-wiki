# ironing_angle

> Location: Process → Quality → Ironing

---

## Angle Offset

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `ironing_angle`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--ironing-angle=1`.  
The angle of ironing lines offset relative to the top surface solid infill direction.  
This option can only be edited when the ironing [Pattern](#pattern) is Rectilinear.

Commonly used ironing angle offsets are 0°, 45°, and 90°, each producing a [different surface finish](https://github.com/OrcaSlicer/OrcaSlicer/issues/10834#issuecomment-3322628589) which will depend on your printer nozzle.

> [!TIP]
> Enable [Align directions to model](../../process/strength/strength_settings_advanced.md#align-directions-to-model) to make the ironing direction follow the model's orientation on the build plate.
