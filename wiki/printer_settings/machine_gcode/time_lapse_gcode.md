# time_lapse_gcode

> 所在界面：打印机设置 → Machine G-code → Timelapse G-code
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/machine gcode/printer_machine_gcode.md` 的「Timelapse G-code」小节（2026-10-28），英文原文，待本地化校对。

---

## Timelapse G-code

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `time_lapse_gcode`.  
[Type](option_type#text): `Text`.  
[CLI Example](cli_mode#setting-overrides): `--time-lapse-gcode=value`.  
This G-code is used for capturing timelapse videos. It typically includes commands to move the print head out of the way for a photo and then return it to the previous position.
