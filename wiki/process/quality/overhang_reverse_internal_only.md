# overhang_reverse_internal_only

> Location: Process → Quality → Overhangs

---

### Reverse internal only

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `overhang_reverse_internal_only`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--overhang-reverse-internal-only=1`.  
A simple way to reduce the texture on the outer wall is to only reverse the internal walls.
This will still provide almost all of the benefits of alternating extrusion direction on even layers (if using [inner/outer](../../process/quality/quality_settings_wall_and_surfaces.md#innerouter)), but the outer wall will be printed in the same direction, resulting in a smoother surface finish.
