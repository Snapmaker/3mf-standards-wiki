# top_surface_speed

> 所在界面：工艺设置 → Speed → Other layers speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_other_layers_speed.md` 的「Top surface」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Top surface

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `top_surface_speed`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--top-surface-speed=1`.  
Speed of the [topmost solid layers](strength_settings_top_bottom_shells) of the print. This is usually set similar to the [outer wall speed](#outer-wall) to achieve a smoother and higher-quality finish on visible surfaces. Lower speeds help minimize surface defects and improve the appearance of the final printed object.
