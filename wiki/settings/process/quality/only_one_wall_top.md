# only_one_wall_top

> Location: Process → Quality → Walls and surfaces
> Also in this section: `only_one_wall_first_layer` (each documented on its own page).

---

## Only one wall

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `only_one_wall_top`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `false`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--only-one-wall-top=1`.  
Use only one wall on flat surfaces, to give more space to the [top infill pattern](../../process/strength/bottom_surface_pattern.md).
Especially useful in small features, like letters, where the top surface is very small and [concentric pattern](../../process/strength/sparse_infill_pattern.md) from walls would not cover it properly.

![only-one-wall](../../../images/wall-order/only-one-wall.gif)

Each option needs the shell it acts on, so they are only available when the matching [Shell Layers](../../process/strength/bottom_shell_layers.md) is greater than 0: without a top shell there is no top surface for the top option to act on, and the same applies to the first layer and the bottom shell.

> [!TIP]
> See [Surface Expansion and Only One Wall](../../process/quality/only_one_wall_first_layer.md) for how the inner walls are handled over an expanded top surface when using more than one wall.
