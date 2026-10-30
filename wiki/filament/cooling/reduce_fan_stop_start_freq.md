# reduce_fan_stop_start_freq

> Location: Filament → Cooling → Part cooling fan

---

### Keep fan always on

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `reduce_fan_stop_start_freq`.  
[Type](../../general_settings/option_type.md#list-types): `Boolean list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--reduce-fan-stop-start-freq=1`.  
Enabling this setting means that part cooling fan will never stop entirely and will instead run at least at minimum speed to reduce the frequency of starting and stopping.
