# gcode_add_line_number

> Location: Process → Others → G-code output

---

## Add line number

[Mode](../../general_settings/option_mode.md): `Developer`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `gcode_add_line_number`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--gcode-add-line-number=1`.  
Prefix each G-code line with a sequential line number (N1, N2, ...). Useful for debugging or tools that expect numbered G-code.
