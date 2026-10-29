# only_one_wall_first_layer

> 所在界面：工艺设置 → Quality → Walls and surfaces
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_wall_and_surfaces.md` 的「Only one wall」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`only_one_wall_top`（各另有独立文档）。

---

## Only one wall

[Mode](option_mode): `Simple`.  
[Variables](built_in_placeholders_variables): `only_one_wall_first_layer`, `only_one_wall_top`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--only-one-wall-first-layer=1` (same pattern for the other variables above).  
Use only one wall on flat surfaces, to give more space to the [top infill pattern](strength_settings_top_bottom_shells#surface-pattern).
Especially useful in small features, like letters, where the top surface is very small and [concentric pattern](strength_settings_patterns#concentric) from walls would not cover it properly.

![only-one-wall](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/only-one-wall.gif?raw=true)

Each option needs the shell it acts on, so they are only available when the matching [Shell Layers](strength_settings_top_bottom_shells#shell-layers) is greater than 0: without a top shell there is no top surface for the top option to act on, and the same applies to the first layer and the bottom shell.

> [!TIP]
> See [Surface Expansion and Only One Wall](strength_settings_top_bottom_shells#surface-expansion-and-only-one-wall) for how the inner walls are handled over an expanded top surface when using more than one wall.
