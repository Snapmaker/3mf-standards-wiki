# infill_wall_overlap

> Location: Process → Strength → Infill

---

## Infill Wall Overlap

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `infill_wall_overlap`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Percentage`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--infill-wall-overlap=20%`.  
Infill area is enlarged slightly to overlap with wall for better bonding. The percentage value is approximately relative to the inner wall line width. More precisely, it is relative to half the inner wall line spacing plus half the internal solid infill line spacing with the [Classic](../../process/quality/quality_settings_wall_generator.md#classic) wall generator, and to the inner wall line spacing with [Arachne](../../process/quality/quality_settings_wall_generator.md#arachne) (the outer wall line spacing in both cases where only one wall is printed). Set this value to ~10-15% to minimize potential over-extrusion and accumulation of material resulting in rough surfaces.

- **Infill Wall Overlap Off**

![InfillWallOverlapOff](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/InfillWallOverlapOff.svg?raw=true)

- **Infill Wall Overlap On**

![InfillWallOverlapOn](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/InfillWallOverlapOn.svg?raw=true)
