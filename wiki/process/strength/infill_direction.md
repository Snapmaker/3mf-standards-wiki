# infill_direction

> Location: Process → Strength → Infill
> 本小节同时涵盖：`solid_infill_direction`（各另有独立文档）。

---

### Direction

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `infill_direction`, `solid_infill_direction`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--infill-direction=1` (same pattern for the other variables above).  
Controls the direction of the infill lines to optimize or strengthen the print.

[Adaptive Cubic](../../process/strength/strength_settings_patterns.md#adaptive-cubic) and [Support Cubic](../../process/strength/strength_settings_patterns.md#support-cubic) do not support rotation, so the sparse infill direction and the sparse infill [rotation template](#rotation) are disabled for them. The solid infill direction and rotation template are not affected.

![fill-direction](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/fill-direction.png?raw=true)

> [!TIP]
> Enable [Align directions to model](../../process/strength/strength_settings_advanced.md#align-directions-to-model) to make this direction follow the model's orientation on the build plate.
