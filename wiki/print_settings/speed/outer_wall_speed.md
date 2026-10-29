# outer_wall_speed

> 所在界面：工艺设置 → Speed → Other layers speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_other_layers_speed.md` 的「Outer wall」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Outer wall

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `outer_wall_speed`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--outer-wall-speed=1`.  
Speed of the outer wall, which is the outermost, visible wall. It is usually printed slower than the [inner wall](#inner-wall) to get better quality and good layer adhesion.
This setting is also limited by [Machine / Motion ability / Resonance avoidance speed settings](vfa_calib).  
It can be excluded from the [layer cooling slowdown](material_cooling#slow-printing-down-for-better-layer-cooling) with [Don't slow down outer walls](material_cooling#dont-slow-down-outer-walls).
