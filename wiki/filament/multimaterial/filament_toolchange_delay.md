# filament_toolchange_delay

> Location: Filament → Multimaterial → Tool change parameters with single extruder MM printers

---

### Delay after unloading

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `filament_toolchange_delay`.  
[Type](../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--filament-toolchange-delay=1`.  
Time to wait after the filament is unloaded. May help to get reliable tool changes with flexible materials that may need more time to shrink to original dimensions.
