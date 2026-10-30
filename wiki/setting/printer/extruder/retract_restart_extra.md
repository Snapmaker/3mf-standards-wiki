# retract_restart_extra

> Location: Printer → Extruder N → Retraction

---

## Extra length on restart

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `retract_restart_extra[extruder_idx]`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--retract-restart-extra=1`.  
When the retraction is compensated after changing tool, the extruder will push this additional amount of filament.
