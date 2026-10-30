# wall_filament

> Location: Process → Multimaterial → Filament for Features
> 显隐条件（初步梳理，待校对）：仅多耗材（非单喷头多耗材）配置下显示

---

## Outer Walls

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `outer_wall_filament_id`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--outer-wall-filament-id=1`.  
Filament to print outer walls.  
You can also print the outer walls with a translucent filament to achieve a frosted glass effect.  
When using a [mixed nozzle size setup](../../../guides/mixed_nozzle_sizes.md), it's recommended to use the smaller nozzle for outer walls to achieve better surface quality and detail.
