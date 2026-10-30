# gcode_label_objects

> Location: Process → Others → G-code output

---

## Label Objects

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `gcode_label_objects`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--gcode-label-objects=1`.  
Insert comments that label moves with the object they belong to (object index or name). This is useful for integrations such as OctoPrint's Cancel Object plugin and for human inspection of the G-code.
