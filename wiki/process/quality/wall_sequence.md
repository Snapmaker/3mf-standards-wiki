# wall_sequence

> Location: Process → Quality → Walls and surfaces

---

## Walls printing order

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `wall_sequence`.  
[Type](../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../general_settings/option_type.md#choice): `inner wall/outer wall, outer wall/inner wall, inner-outer-inner wall`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--wall-sequence="inner wall/outer wall"`.  
Print sequence of the internal (inner) and external (outer) walls.  
The order applies to each side of a wall on its own: the walls around a hole follow it just like the walls around the contour.

> [!NOTE]
> Under an [Outer](../../process/others/others_settings_brim.md#outer), [Outer and Inner](../../process/others/others_settings_brim.md#outer-and-inner) or [Leading edge only](../../process/others/others_settings_brim.md#leading-edge-only) brim, the first layer prints its outer walls first whatever this setting, so the brim runs straight on into the outer wall.  
> [Auto](../../process/others/others_settings_brim.md#auto), [Mouse Ears](../../process/others/others_settings_brim.md#mouse-ears) and [Painted](../../process/others/others_settings_brim.md#painted) brims may leave the outer walls bare, so they keep this order.
