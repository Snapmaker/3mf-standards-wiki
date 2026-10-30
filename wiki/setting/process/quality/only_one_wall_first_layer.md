# only_one_wall_first_layer

> Location: Process → Quality → Walls and surfaces
> 本小节同时涵盖：`only_one_wall_top`（各另有独立文档）。

---

## Only one wall

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `only_one_wall_first_layer`, `only_one_wall_top`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--only-one-wall-first-layer=1` (same pattern for the other variables above).  
Use only one wall on flat surfaces, to give more space to the [top infill pattern](../../process/strength/strength_settings_top_bottom_shells.md#surface-pattern).
Especially useful in small features, like letters, where the top surface is very small and [concentric pattern](../../process/strength/strength_settings_patterns.md#concentric) from walls would not cover it properly.

![only-one-wall](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/only-one-wall.gif?raw=true)

Each option needs the shell it acts on, so they are only available when the matching [Shell Layers](../../process/strength/strength_settings_top_bottom_shells.md#shell-layers) is greater than 0: without a top shell there is no top surface for the top option to act on, and the same applies to the first layer and the bottom shell.

> [!TIP]
> See [Surface Expansion and Only One Wall](../../process/strength/strength_settings_top_bottom_shells.md#surface-expansion-and-only-one-wall) for how the inner walls are handled over an expanded top surface when using more than one wall.
