# initial_layer_travel_speed

> 所在界面：工艺设置 → Speed → Initial layer speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_initial_layer_speed.md` 的「Initial layer travel speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Initial layer travel speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `initial_layer_travel_speed`.  
[Type](option_type#list-types): `Float or Percentage list`.  
[CLI Example](cli_mode#setting-overrides): `--initial-layer-travel-speed=20%`.  
Sets the travel (non-printing movement) speed for the first layer. This doesn't affect print quality and can be set as a percentage of the [travel speed](speed_settings_travel).  
Usually, this is set to 100% of the [travel speed](speed_settings_travel), but it can be reduced if you want to minimize vibrations or if your printer has issues with high-speed travel movements.
