# wall_direction

> Location: Process → Quality → Walls and surfaces

---

## Wall loop direction

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `wall_direction`.  
[Type](../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../general_settings/option_type.md#choice): `ccw, cw`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--wall-direction=ccw`.  
The direction in which the **contour** wall loops are extruded when looking down from the top.  
Holes are printed in the opposite direction to the contour to maintain alignment with layers whose contour polygons are incomplete and change direction, also partially forming the contour of a hole.
A hole whose outer wall touches the contour's with nothing between them, like a [narrow wall](#narrow-walls) 2 lines wide, runs with the contour instead, so both walls are laid side by side in the same direction.
Check [PR 12669](https://github.com/OrcaSlicer/OrcaSlicer/pull/12669) for more details about reversing hole direction.

The usage of [Reverse on even](../../process/quality/quality_settings_overhangs.md#reverse-on-even) will reverse wall direction based on this setting.

> [!NOTE]
> This option will be disabled if spiral vase mode is enabled.
