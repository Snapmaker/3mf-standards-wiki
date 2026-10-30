# wipe

> Location: Printer → Extruder N → Retraction

---

## Wipe while retracting

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `wipe[extruder_idx]`.  
[Type](../../../general_settings/option_type.md#list-types): `Boolean list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--wipe=1`.  
This moves the nozzle along the last extrusion path when retracting to clean any leaked material on the nozzle. This can minimize blobs when printing a new part after traveling.
