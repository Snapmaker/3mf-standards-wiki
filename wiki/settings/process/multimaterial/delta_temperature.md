# delta_temperature

> Location: Process → Multimaterial → Ooze prevention
> Also in this section: `standby_temperature_delta` (each documented on its own page).

---

## Temperature variation

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `delta_temperature`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--delta-temperature=1`.  
Temperature difference to be applied when an extruder is not active. The value is not used when [Idle temperature](../../filament/filament/idle_temperature.md) in the filament settings is set to a non-zero value.
