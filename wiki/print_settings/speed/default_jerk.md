# default_jerk

> 所在界面：工艺设置 → Speed → Jerk(XY)
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_jerk_xy.md` 的「Default」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Default

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `default_jerk`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--default-jerk=1`.  
Default Jerk value.

> [!NOTE]
> If this value is set to 0, the jerk will be set to the printer's default jerk.
