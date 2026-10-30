# outer_wall_speed

> Location: Process → Speed → Other layers speed

---

## Outer wall

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `outer_wall_speed`.  
[Type](../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--outer-wall-speed=1`.  
Speed of the outer wall, which is the outermost, visible wall. It is usually printed slower than the [inner wall](#inner-wall) to get better quality and good layer adhesion.
This setting is also limited by [Machine / Motion ability / Resonance avoidance speed settings](../../calibration/vfa_calib.md).  
It can be excluded from the [layer cooling slowdown](../../filament/cooling/material_cooling.md#slow-printing-down-for-better-layer-cooling) with [Don't slow down outer walls](../../filament/cooling/material_cooling.md#dont-slow-down-outer-walls).
