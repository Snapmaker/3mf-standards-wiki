# reduce_crossing_wall

> 所在界面：工艺设置 → Quality → Walls and surfaces
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_wall_and_surfaces.md` 的「Avoid crossing walls」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Avoid crossing walls

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `reduce_crossing_wall`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--reduce-crossing-wall=1`.  
This option instructs the slicer to avoid crossing perimeters (walls) during travel moves.  
Instead of traveling directly through a wall, the print head will detour around it, which can significantly reduce surface defects and stringing.

While this increases print time slightly, the improvement in print quality, especially with materials prone to stringing like **PETG** or **TPU**, often justifies the trade-off.  
Highly recommended for detailed or aesthetic prints.

![avoid-crossing-walls](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/avoid-crossing-walls.png?raw=true)
