# is_infill_first

> Location: Process → Quality → Walls and surfaces

---

### Print infill first

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `is_infill_first`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--is-infill-first=1`.  
When this option is enabled, the [infill](../../process/strength/sparse_infill_density.md) and [top/bottom shells](../../process/strength/top_shell_thickness.md) are printed first, followed by the walls. The first layer always prints the walls first, for better bed adhesion. This can be useful for some overhangs where the infill can support the walls.

![infill-first](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/infill-first.gif?raw=true)

**However**, the infill will slightly push out the printed walls where it is attached to them, resulting in a worse external surface finish. It can also cause the infill to shine through the external surfaces of the part.

![infill-ghosting](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/infill-ghosting.png?raw=true)

When using this option, it is recommended to use the [Precise Wall](../../process/quality/precise_outer_wall.md), [Inner/Outer/Inner](#innerouterinner) wall printing order or reduce [Infill/Wall Overlap](../../process/strength/infill_wall_overlap.md) to avoid the infill pushing out the external wall.
