# internal_solid_infill_speed

> 所在界面：工艺设置 → Speed → Other layers speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_other_layers_speed.md` 的「Internal solid infill」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Internal solid infill

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `internal_solid_infill_speed`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--internal-solid-infill-speed=1`.  
Speed of internal solid infill, which fills the interior of the model with solid layers.  
This is typically set faster than the [top surface speed](#top-surface) to optimize print time, while still ensuring adequate strength and layer adhesion. Adjusting this speed can help balance print quality and efficiency, especially for models requiring strong internal structures.  
Solid infill is also considered when [infill % is set to 100%](strength_settings_infill#internal-solid-infill).
