# time_lapse_gcode

> Location: Printer → Machine G-code → Timelapse G-code

---

## Timelapse G-code

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `time_lapse_gcode`.  
[Type](../../general_settings/option_type.md#text): `Text`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--time-lapse-gcode=value`.  
This G-code is used for capturing timelapse videos. It typically includes commands to move the print head out of the way for a photo and then return it to the previous position.
