# top_surface_jerk

> 所在界面：工艺设置 → Speed → Jerk(XY)
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_jerk_xy.md` 的「Top surface」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Top surface

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `top_surface_jerk`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--top-surface-jerk=1`.  
Jerk for top surface printing. This is usually set to a lower value than infill to ensure better quality.
