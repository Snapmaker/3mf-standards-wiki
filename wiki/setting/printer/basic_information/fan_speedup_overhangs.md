# fan_speedup_overhangs

> Location: Printer → Basic information → Cooling Fan

---

## Fan speed-up time

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `fan_speedup_time`, `fan_speedup_overhangs`.  
[Type](../../../general_settings/option_type.md): `fan_speedup_time` (Float), `fan_speedup_overhangs` (Boolean).  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--fan-speedup-time=1` (`fan_speedup_time` shown; other variables above follow their own type).  
Start the fan this number of seconds earlier than its target start time (you can use fractional seconds). It assumes infinite acceleration for this time estimation, and will only take into account G1 and G0 moves (arc fitting is unsupported).
It won't move fan commands from custom G-code (they act as a sort of 'barrier').
It won't move fan commands into the start G-code if the 'only custom start G-code' is activated.
Use 0 to deactivate.

### Only overhangs

Will only take into account the delay for the cooling of overhangs.
