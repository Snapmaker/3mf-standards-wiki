# sparse_infill_acceleration

> Location: Process → Speed → Acceleration

---

## Sparse infill

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `sparse_infill_acceleration`.  
[Type](../../../general_settings/option_type.md#list-types): `Float or Percentage list`.  
[Default](../../../general_settings/option_type.md#default-value): `100%`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` mm/s² or %.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--sparse-infill-acceleration=20%`.  
Acceleration of [sparse infill](../../process/speed/sparse_infill_acceleration.md). If the value is expressed as a percentage (e.g. 100%), it will be calculated based on the default acceleration.
