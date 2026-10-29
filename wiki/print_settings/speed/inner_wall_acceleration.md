# inner_wall_acceleration

> 所在界面：工艺设置 → Speed → Acceleration
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_acceleration.md` 的「Inner wall」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Inner wall

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `inner_wall_acceleration`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--inner-wall-acceleration=1`.  
Acceleration for [inner wall](speed_settings_other_layers_speed#inner-wall) printing. This is usually set to a higher value than outer wall printing to improve speed.
