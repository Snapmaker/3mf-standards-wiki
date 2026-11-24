# wall_filament

> Location: Process → Multimaterial → Filament for Features → Outer Walls
> Visibility (preliminary, pending review): Shown only in multi-material (not single-extruder multi-material) configurations

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `wall_filament`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[Default](../../../general_settings/option_type.md#default-value): `1`.  
[Range](../../../general_settings/option_type.md#range): `≥ 1`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--wall-filament=1`.  

Filament to print outer walls.  
You can also print the outer walls with a translucent filament to achieve a frosted glass effect.  
When using a mixed nozzle size setup, it's recommended to use the smaller nozzle for outer walls to achieve better surface quality and detail.
