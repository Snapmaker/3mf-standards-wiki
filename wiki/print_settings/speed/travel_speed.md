# travel_speed

> 所在界面：工艺设置 → Speed → Travel speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_travel.md` 的「Travel」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

# Travel

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `travel_speed`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--travel-speed=1`.  
![travel-lines](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/speed/travel-lines.png?raw=true)

Travel speed is the speed at which the print head moves when not extruding filament.  
This speed is typically faster than the printing speed, as there is no need to carefully place material. However, setting the travel speed too high can lead to issues such as missed steps or ringing artifacts.
