# machine_max_acceleration_z

> Location: Printer → Motion ability → Acceleration limitation

---

## Acceleration limitation

[Modes](../../../general_settings/option_mode.md):  
`Simple` [Variables](../../../developer_reference/built_in_placeholders_variables.md): `machine_max_acceleration_x`, `machine_max_acceleration_y`, `machine_max_acceleration_z`, `machine_max_acceleration_e`, `machine_max_acceleration_extruding`, `machine_max_acceleration_retracting`.  
`Advanced` [Variable](../../../developer_reference/built_in_placeholders_variables.md): `machine_max_acceleration_travel`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--machine-max-acceleration-x=1` (same pattern for the other variables above).  
Safeguard maximum accelerations for all axes.
This will cap the acceleration set by the process if it exceeds these values.
