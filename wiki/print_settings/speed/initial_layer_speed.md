# initial_layer_speed

> 所在界面：工艺设置 → Speed → Initial layer speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_initial_layer_speed.md` 的「Initial layer」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Initial layer

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `initial_layer_speed`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--initial-layer-speed=1`.  
This setting determines the printing speed of the [outer/inner walls](strength_settings_walls) and the brim on the first layer.  
All other first layer extrusions, such as [solid infill](strength_settings_top_bottom_shells) and the [sparse infill](strength_settings_infill) printed when [bottom layers](strength_settings_top_bottom_shells#shell-layers) is set to 0, use the [First layer infill](#initial-layer-infill) speed.  
Adjusting this speed helps ensure proper adhesion and print quality for the initial layer.
