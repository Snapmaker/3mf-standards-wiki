# printing_by_object_gcode

> 所在界面：打印机设置 → Machine G-code → Printing by object G-code
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/machine gcode/printer_machine_gcode.md` 的「Printing by object G-code」小节（2026-10-28），英文原文，待本地化校对。

---

## Printing by object G-code

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `printing_by_object_gcode`.  
[Type](option_type#text): `Text`.  
[CLI Example](cli_mode#setting-overrides): `--printing-by-object-gcode=value`.  
This G-code is executed at the start of printing each individual object in a multi-object print job. It can be used to set specific parameters or perform actions for each object.
