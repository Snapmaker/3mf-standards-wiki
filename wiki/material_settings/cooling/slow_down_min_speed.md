# slow_down_min_speed

> 所在界面：耗材设置 → Cooling → Part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Min print speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Min print speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `slow_down_min_speed`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--slow-down-min-speed=1`.  
The minimum print speed to which the printer slows down to maintain the minimum layer time defined above when the slowdown for better layer cooling is enabled.  
See [How the slowdown is calculated](#how-the-slowdown-is-calculated).
