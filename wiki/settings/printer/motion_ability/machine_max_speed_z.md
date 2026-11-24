# machine_max_speed_z

> Location: Printer → Motion ability → Speed limitation → Z

---

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `machine_max_speed_z`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `12, 12`.  
[Unit](../../../general_settings/option_type.md#unit): `mm/s`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--machine-max-speed-z=1`.  

Safeguard maximum speeds for all axes.
This will cap the speed set by the process if it exceeds these values.
