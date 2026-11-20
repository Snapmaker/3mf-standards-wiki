# enable_tower_interface_cooldown_during_tower

> Location: Process → Multimaterial → Prime tower → Cool down from interface boost during prime tower
> Visibility(preliminary, pending review): Shown only on Snapmaker U1 machines

---

[Mode](../../../general_settings/option_mode.md): `Developer`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `enable_tower_interface_cooldown_during_tower`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `false`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--enable-tower-interface-cooldown-during-tower=1`.  

Only shown when [Enable tower interface features](#enable-tower-interface-features) is enabled, and only used by the Type 2 tower. After heating to the interface temperature, the nozzle is set back to its print temperature at the start of the purge, so it cools down while the tower is printed. When disabled, the print temperature is restored only after the purge is finished.
