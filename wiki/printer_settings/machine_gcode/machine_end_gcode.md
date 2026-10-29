# machine_end_gcode

> 所在界面：打印机设置 → Machine G-code → Machine end G-code
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/machine gcode/printer_machine_gcode.md` 的「Machine end G-code」小节（2026-10-28），英文原文，待本地化校对。

---

## Machine end G-code

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `machine_end_gcode`.  
[Type](option_type#text): `Text`.  
[CLI Example](cli_mode#setting-overrides): `--machine-end-gcode=value`.  
This G-code is executed at the end of a print job, after all printing is complete. It is typically used to turn off heaters, move the print head away from the print, and perform any necessary post-print actions.
