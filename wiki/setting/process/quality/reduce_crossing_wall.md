# reduce_crossing_wall

> Location: Process → Quality → Walls and surfaces

---

## Avoid crossing walls

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `reduce_crossing_wall`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--reduce-crossing-wall=1`.  
This option instructs the slicer to avoid crossing perimeters (walls) during travel moves.  
Instead of traveling directly through a wall, the print head will detour around it, which can significantly reduce surface defects and stringing.

While this increases print time slightly, the improvement in print quality, especially with materials prone to stringing like **PETG** or **TPU**, often justifies the trade-off.  
Highly recommended for detailed or aesthetic prints.

![avoid-crossing-walls](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/avoid-crossing-walls.png?raw=true)
