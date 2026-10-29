# top_surface_acceleration

> 所在界面：工艺设置 → Speed → Acceleration
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_acceleration.md` 的「Top surface」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Top surface

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `top_surface_acceleration`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--top-surface-acceleration=1`.  
Acceleration of [top surface infill](speed_settings_other_layers_speed#top-surface). Using a lower value may improve top surface quality.  
A value similar to the [outer wall acceleration](#outer-wall) is recommended.
