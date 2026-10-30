# solid_infill_filament

> Location: Process → Multimaterial → Filament for Features
> 显隐条件（初步梳理，待校对）：仅多耗材（非单喷头多耗材）配置下显示

---

## Internal Solid Infill

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `internal_solid_filament_id`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--internal-solid-filament-id=1`.  
Filament to print internal solid infill.  
When using a [mixed nozzle size setup](../../guides/mixed_nozzle_sizes.md), you can use a larger nozzle for internal solid infill to speed up printing while maintaining good layer adhesion.
