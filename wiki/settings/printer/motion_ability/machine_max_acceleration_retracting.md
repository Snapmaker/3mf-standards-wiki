# machine_max_acceleration_retracting

> Location: Printer → Motion ability → Acceleration limitation → Acceleration limitation

---

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `machine_max_acceleration_retracting`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `1500, 1250`.  
[Unit](../../../general_settings/option_type.md#unit): `mm/s²`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--machine-max-acceleration-retracting=1`.  

Safeguard maximum accelerations for all axes.
This will cap the acceleration set by the process if it exceeds these values.
