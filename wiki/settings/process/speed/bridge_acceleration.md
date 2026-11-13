# bridge_acceleration

> Location: Process → Speed → Acceleration

---

## Bridge

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `bridge_acceleration`.  
[Type](../../../general_settings/option_type.md#list-types): `Float or Percentage list`.  
[Default](../../../general_settings/option_type.md#default-value): `50%`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` mm/s² or %.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--bridge-acceleration=20%`.  
Acceleration of [bridges](../../process/speed/bridge_speed.md). If the value is expressed as a percentage (e.g. 50%), it will be calculated based on the outer wall acceleration.
