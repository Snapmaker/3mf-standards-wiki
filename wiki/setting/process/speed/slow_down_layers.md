# slow_down_layers

> Location: Process → Speed → Initial layer speed

---

## Number of slow layers

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `slow_down_layers`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--slow-down-layers=1`.  
Specifies how many of the first layers should be printed at a reduced speed. Instead of jumping straight to full speed after the first layer, the speed gradually increases in a linear fashion over this number of layers. This gradual ramp-up helps maintain adhesion and gives the print more stability in its early stages, especially on prints with a small contact area or materials prone to warping.

![number-of-slow-layers](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/speed/number-of-slow-layers.png?raw=true)
