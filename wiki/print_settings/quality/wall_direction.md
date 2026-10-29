# wall_direction

> 所在界面：工艺设置 → Quality → Walls and surfaces
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_wall_and_surfaces.md` 的「Wall loop direction」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Wall loop direction

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wall_direction`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `ccw, cw`.  
[CLI Example](cli_mode#setting-overrides): `--wall-direction=ccw`.  
The direction in which the **contour** wall loops are extruded when looking down from the top.  
Holes are printed in the opposite direction to the contour to maintain alignment with layers whose contour polygons are incomplete and change direction, also partially forming the contour of a hole.
A hole whose outer wall touches the contour's with nothing between them, like a [narrow wall](#narrow-walls) 2 lines wide, runs with the contour instead, so both walls are laid side by side in the same direction.
Check [PR 12669](https://github.com/OrcaSlicer/OrcaSlicer/pull/12669) for more details about reversing hole direction.

The usage of [Reverse on even](quality_settings_overhangs#reverse-on-even) will reverse wall direction based on this setting.

> [!NOTE]
> This option will be disabled if spiral vase mode is enabled.
