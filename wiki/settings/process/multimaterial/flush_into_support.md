# flush_into_support

> Location: Process → Multimaterial → Flush options

---

## Flush into objects' support

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `flush_into_support`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `true`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--flush-into-support=1`.  
Purging after a filament change will be done inside the objects' support. This may lower the amount of waste and decrease the print time. It will not take effect unless the prime tower is enabled. With a Type 2 [wipe tower](../../process/multimaterial/wipe_tower_cone_angle.md), purging into objects is only used on single extruder multi-material printers with [Purge in prime tower](../../printer/multimaterial/purge_in_prime_tower.md) enabled.
