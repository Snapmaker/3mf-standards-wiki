# sparse_infill_filament

> Location: Process → Multimaterial → Filament for Features
> 显隐条件（初步梳理，待校对）：仅多耗材（非单喷头多耗材）配置下显示

---

## Sparse Infill

> [!WARNING] fork 未实现
> `sparse_infill_filament_id` 为上游 OrcaSlicer 参数，fork 源码未收录，以下内容保留供参考。

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `sparse_infill_filament_id`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[Default](../../../general_settings/option_type.md#default-value): —.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--sparse-infill-filament-id=1`.  
Filament to print internal sparse infill.  
When using a [mixed nozzle size setup](../../../guides/mixed_nozzle_sizes.md), you can use a larger nozzle for infill to speed up printing while maintaining good layer adhesion.
