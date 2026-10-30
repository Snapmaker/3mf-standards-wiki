# filename_format

> Location: Process → Others → G-code output

---

## Filename Format

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `filename_format`.  
[Type](../../general_settings/option_type.md#text): `Text`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--filename-format={input_filename_base}_{filament_type[initial_tool]}_{print_time}.gcode`.  
Define a filename template for exported G-code. Templates may include tokens like project name, date, or other metadata to produce consistent and informative filenames on export.

For example:

```c++
{input_filename_base}_{filament_type[initial_tool]}_{print_time}.gcode
```

This can be used to generate filenames like `OrcaCube_PLA_1h15m.gcode`.

> [!TIP]
> Check [File Name Template](../../developer_reference/built_in_placeholders_variables.md#file-name-template) for available tokens and their meanings.
