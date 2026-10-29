# small_perimeter_speed

> 所在界面：工艺设置 → Speed → Other layers speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_other_layers_speed.md` 的「Small perimeters」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Small perimeters

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `small_perimeter_speed`.  
[Type](option_type#list-types): `Float or Percentage list`.  
[CLI Example](cli_mode#setting-overrides): `--small-perimeter-speed=20%`.  
Speed of walls with a theoretical radius <= [small perimeters threshold](#small-perimeters-threshold).
Any shape (not only circles) will be considered as a small perimeter.

If expressed as a percentage (for example: 80%), it will be calculated on the [outer wall speed](#outer-wall).

> [!NOTE]
> The default is 50% of the [outer wall speed](#outer-wall).
