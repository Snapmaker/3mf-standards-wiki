# extruder_offset

> Location: Printer → Extruder N → Position

---

## Extruder offset Position

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `extruder_offset[extruder_idx]`.  
[Type](../../../general_settings/option_type.md#list-types): `Point list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--extruder-offset=100,100`.  
If your firmware doesn't handle the extruder displacement you need the G-code to take it into account. This option lets you specify the displacement of each extruder with respect to the first one. It expects positive coordinates (they will be subtracted from the XY coordinate).
