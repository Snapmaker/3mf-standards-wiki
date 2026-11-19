# outer_wall_speed

> Location: Process → Speed → Other layers speed

---

## Outer wall

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `outer_wall_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `60`.  
[Range](../../../general_settings/option_type.md#range): `≥ 1` mm/s.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--outer-wall-speed=1`.  
Speed of the outer wall, which is the outermost, visible wall. It is usually printed slower than the [inner wall](../../process/speed/inner_wall_speed.md) to get better quality and good layer adhesion.
This setting is also limited by [Machine / Motion ability / Resonance avoidance speed settings](../../../calibration/vfa_calib.md) and by the filament's Max external volumetric speed. [Resonance avoidance](../../printer/motion_ability/resonance_avoidance.md) never raises it above that limit or the [Max volumetric speed](../../filament/filament/filament_max_volumetric_speed.md).  
It can be excluded from the [layer cooling slowdown](../../filament/cooling/slow_down_for_layer_cooling.md) with [Don't slow down outer walls](../../filament/cooling/dont_slow_down_outer_wall.md).  
With volumetric speeds enabled, it is set as a volumetric speed instead, 50% by default.

## Speed limitations

> [!IMPORTANT]
> Every speed setting is limited by several parameters like:
>
> - [Maximum Volumetric Speed](../../../calibration/volumetric_speed_calib.md)
> - Max external volumetric speed on outer walls, external bridges, overhang walls and top surfaces that are not ironed
> - Machine / Motion ability
> - Acceleration
> - Jerk settings
> - [Filament layer cooling time](../../filament/cooling/slow_down_for_layer_cooling.md)
