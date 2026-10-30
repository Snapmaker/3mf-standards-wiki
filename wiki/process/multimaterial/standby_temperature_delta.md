# standby_temperature_delta

> Location: Process → Multimaterial → Ooze prevention
> 本小节同时涵盖：`delta_temperature`（各另有独立文档）。

---

## Temperature variation

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `standby_temperature_delta`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--standby-temperature-delta=1`.  
Temperature difference to be applied when an extruder is not active. The value is not used when [Idle temperature](../../filament/filament/material_basic_information.md#idle-temperature) in the filament settings is set to a non-zero value.
