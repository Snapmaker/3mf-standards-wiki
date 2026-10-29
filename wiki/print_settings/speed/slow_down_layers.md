# slow_down_layers

> 所在界面：工艺设置 → Speed → Initial layer speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_initial_layer_speed.md` 的「Number of slow layers」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Number of slow layers

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `slow_down_layers`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--slow-down-layers=1`.  
Specifies how many of the first layers should be printed at a reduced speed. Instead of jumping straight to full speed after the first layer, the speed gradually increases in a linear fashion over this number of layers. This gradual ramp-up helps maintain adhesion and gives the print more stability in its early stages, especially on prints with a small contact area or materials prone to warping.

![number-of-slow-layers](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/speed/number-of-slow-layers.png?raw=true)
