# tool_change_temprature_wait

> Location: Printer → Multimaterial → Advanced → Wait for the temperature when changing tools
> Status: placeholder — to be completed.

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `tool_change_temprature_wait`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `true`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--tool-change-temprature-wait=1`.  

It will use the M109 instead of M104 T[target] after changing tools if this is set to true
