# top_bottom_infill_wall_overlap

> 所在界面：工艺设置 → Strength → Top/bottom shells
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_top_bottom_shells.md` 的「Infill/Wall Overlap」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Infill/Wall Overlap

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `top_bottom_infill_wall_overlap`.  
[Type](option_type#integer-float-percentage): `Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--top-bottom-infill-wall-overlap=20%`.  
The top solid infill area is slightly enlarged to overlap with walls for better bonding and to minimize pinholes where the infill meets the walls.  
A value of 25-30% is a good starting point. The percentage value is approximately relative to the inner wall line width. More precisely, it is relative to half the inner wall line spacing plus half the internal solid infill line spacing with the [Classic](quality_settings_wall_generator#classic) wall generator, and to the inner wall line spacing with [Arachne](quality_settings_wall_generator#arachne) (the outer wall line spacing in both cases where only one wall is printed).

> [!TIP]
> Check [Monotonic line](strength_settings_patterns#monotonic-line) to learn about its overlap differences with [Monotonic](strength_settings_patterns#monotonic) and [Rectilinear](strength_settings_patterns#rectilinear).
