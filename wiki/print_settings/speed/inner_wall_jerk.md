# inner_wall_jerk

> 所在界面：工艺设置 → Speed → Jerk(XY)
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_jerk_xy.md` 的「Inner wall」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Inner wall

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `inner_wall_jerk`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--inner-wall-jerk=1`.  
Jerk for inner wall printing. This is usually set to a moderately higher value than outer wall jerk to improve speed.
