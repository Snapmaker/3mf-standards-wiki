# first_layer_travel_jerk

> 所在界面：工艺设置 → Speed → Jerk(XY)
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_jerk_xy.md` 的「Initial layer travel」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Initial layer travel

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `initial_layer_travel_jerk`.  
[Type](option_type#list-types): `Float or Percentage list`.  
[CLI Example](cli_mode#setting-overrides): `--initial-layer-travel-jerk=20%`.  
Jerk for initial layer travel.
Using a lower value can improve build plate adhesion. If the value is expressed as a percentage (e.g. 50%), it will be calculated based on the [Travel Jerk](#travel).
