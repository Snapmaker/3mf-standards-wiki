# top_bottom_infill_wall_overlap

> Location: Process → Strength → Top/bottom shells

---

## Infill/Wall Overlap

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `top_bottom_infill_wall_overlap`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Percentage`.  
[Default](../../../general_settings/option_type.md#default-value): `25`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--top-bottom-infill-wall-overlap=20%`.  
The top solid infill area is slightly enlarged to overlap with walls for better bonding and to minimize pinholes where the infill meets the walls.  
A value of 25-30% is a good starting point. The percentage value is approximately relative to the inner wall line width. More precisely, it is relative to half the inner wall line spacing plus half the internal solid infill line spacing with the [Classic](../../process/quality/wall_generator.md) wall generator, and to the inner wall line spacing with [Arachne](../../process/quality/initial_layer_min_bead_width.md) (the outer wall line spacing in both cases where only one wall is printed).

> [!TIP]
> Check [Monotonic line](../../process/strength/sparse_infill_pattern.md) to learn about its overlap differences with [Monotonic](../../process/strength/sparse_infill_pattern.md) and [Rectilinear](../../process/strength/sparse_infill_pattern.md).
