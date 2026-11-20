# wipe_tower_filament

> Location: Process → Multimaterial → Filament for Features → Wipe Tower
> Visibility (preliminary, pending review): Shown only in multi-material (not single-extruder multi-material) configurations

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `wipe_tower_filament`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--wipe-tower-filament=1`.  

Filament to print the perimeter of the wipe tower. Set to `Default` to use any available filament, preferring a non-soluble one.
