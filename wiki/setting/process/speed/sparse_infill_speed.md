# sparse_infill_speed

> Location: Process → Speed → Other layers speed

---

## Sparse infill

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `sparse_infill_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `100`.  
[Range](../../../general_settings/option_type.md#range): `≥ 1` mm/s.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--sparse-infill-speed=1`.  
Speed of [sparse infill](../../process/strength/sparse_infill_density.md) which is printed faster than solid infill to reduce print time.  
If you are using your [Infill Pattern](../../process/strength/sparse_infill_density.md) as an aesthetic feature, you may want to set it closer to the [outer wall speed](#outer-wall) to get better quality.
