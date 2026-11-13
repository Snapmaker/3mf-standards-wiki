# align_infill_direction_to_model

> Location: Process → Strength → Advanced

---

## Align directions to model

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `align_infill_direction_to_model`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `false`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--align-infill-direction-to-model=1`.  
Aligns [infill](../../process/strength/infill_direction.md), [bridge](#bridge-infill-direction), [ironing](../../process/quality/ironing_angle.md) and [top/bottom surface fill](../../process/strength/bottom_surface_pattern.md) directions to follow the model's orientation on the build plate.  
When enabled, these directions rotate together with the model so the printed features keep their intended orientation relative to the part, preserving optimal strength and surface characteristics regardless of how the model is placed.

![fill-direction-to-model](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/fill-direction-to-model.png?raw=true)
