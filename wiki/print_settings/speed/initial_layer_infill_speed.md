# initial_layer_infill_speed

> 所在界面：工艺设置 → Speed → Initial layer speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_initial_layer_speed.md` 的「Initial layer infill」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Initial layer infill

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `initial_layer_infill_speed`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--initial-layer-infill-speed=1`.  
Defines the speed used for everything on the first layer except walls and brim, mainly the [solid infill](strength_settings_top_bottom_shells#shell-layers) regions. These areas require more precise and consistent extrusion to create a flat and stable surface for subsequent layers. Printing this section too fast may result in high internal stresses (increased risk of warping), poor layer uniformity, or adhesion failures.
