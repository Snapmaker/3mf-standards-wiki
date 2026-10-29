# change_filament_gcode

> 所在界面：打印机设置 → Machine G-code → Change filament G-code
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/machine gcode/printer_machine_gcode.md` 的「Change filament G-code」小节（2026-10-28），英文原文，待本地化校对。

---

## Change filament G-code

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `change_filament_gcode`.  
[Type](option_type#text): `Text`.  
[CLI Example](cli_mode#setting-overrides): `--change-filament-gcode=value`.  
This G-code is inserted when filament is changed, including T commands to trigger tool change.
