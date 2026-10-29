# filename_format

> 所在界面：工艺设置 → Others → G-code output
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_g_code_output.md` 的「Filename Format」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Filename Format

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filename_format`.  
[Type](option_type#text): `Text`.  
[CLI Example](cli_mode#setting-overrides): `--filename-format={input_filename_base}_{filament_type[initial_tool]}_{print_time}.gcode`.  
Define a filename template for exported G-code. Templates may include tokens like project name, date, or other metadata to produce consistent and informative filenames on export.

For example:

```c++
{input_filename_base}_{filament_type[initial_tool]}_{print_time}.gcode
```

This can be used to generate filenames like `OrcaCube_PLA_1h15m.gcode`.

> [!TIP]
> Check [File Name Template](built_in_placeholders_variables#file-name-template) for available tokens and their meanings.
