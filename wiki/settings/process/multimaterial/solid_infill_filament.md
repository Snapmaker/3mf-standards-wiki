# solid_infill_filament

> Location: Process → Multimaterial → Filament for Features → Internal Solid Infill
> Visibility (preliminary, pending review): Shown only in multi-material (not single-extruder multi-material) configurations

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `solid_infill_filament`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[Default](../../../general_settings/option_type.md#default-value): `1`.  
[Range](../../../general_settings/option_type.md#range): `≥ 1`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--solid-infill-filament=1`.  

Filament to print internal solid infill.  
When using a [mixed nozzle size setup](../../../guides/mixed_nozzle_sizes.md), you can use a larger nozzle for internal solid infill to speed up printing while maintaining good layer adhesion.
