# wall_sequence

> 所在界面：工艺设置 → Quality → Walls and surfaces
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_wall_and_surfaces.md` 的「Walls printing order」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Walls printing order

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wall_sequence`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `inner wall/outer wall, outer wall/inner wall, inner-outer-inner wall`.  
[CLI Example](cli_mode#setting-overrides): `--wall-sequence="inner wall/outer wall"`.  
Print sequence of the internal (inner) and external (outer) walls.  
The order applies to each side of a wall on its own: the walls around a hole follow it just like the walls around the contour.

> [!NOTE]
> Under an [Outer](others_settings_brim#outer), [Outer and Inner](others_settings_brim#outer-and-inner) or [Leading edge only](others_settings_brim#leading-edge-only) brim, the first layer prints its outer walls first whatever this setting, so the brim runs straight on into the outer wall.  
> [Auto](others_settings_brim#auto), [Mouse Ears](others_settings_brim#mouse-ears) and [Painted](others_settings_brim#painted) brims may leave the outer walls bare, so they keep this order.
