# is_infill_first

> 所在界面：工艺设置 → Quality → Walls and surfaces
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_wall_and_surfaces.md` 的「Print infill first」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Print infill first

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `is_infill_first`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--is-infill-first=1`.  
When this option is enabled, the [infill](strength_settings_infill) and [top/bottom shells](strength_settings_top_bottom_shells) are printed first, followed by the walls. The first layer always prints the walls first, for better bed adhesion. This can be useful for some overhangs where the infill can support the walls.

![infill-first](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/infill-first.gif?raw=true)

**However**, the infill will slightly push out the printed walls where it is attached to them, resulting in a worse external surface finish. It can also cause the infill to shine through the external surfaces of the part.

![infill-ghosting](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/infill-ghosting.png?raw=true)

When using this option, it is recommended to use the [Precise Wall](quality_settings_precision#precise-wall), [Inner/Outer/Inner](#innerouterinner) wall printing order or reduce [Infill/Wall Overlap](strength_settings_infill#infill-wall-overlap) to avoid the infill pushing out the external wall.
