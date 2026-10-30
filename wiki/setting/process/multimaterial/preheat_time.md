# preheat_time

> Location: Process → Multimaterial → Ooze prevention

---

## Preheat time

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `preheat_time`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--preheat-time=1`.  
To reduce the waiting time after tool change, Orca can preheat the next tool while the current tool is still in use. This setting specifies the time in seconds to preheat the next tool. Orca will insert an M104 command to preheat the tool in advance.
