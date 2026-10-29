# before_layer_change_gcode

> 所在界面：打印机设置 → Machine G-code → Before layer change G-code
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/machine gcode/printer_machine_gcode.md` 的「Before layer change G-code」小节（2026-10-28），英文原文，待本地化校对。

---

## Before layer change G-code

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `before_layer_change_gcode`.  
[Type](option_type#text): `Text`.  
[CLI Example](cli_mode#setting-overrides): `--before-layer-change-gcode=value`.  
This G-code is inserted at every layer change before the Z lift.
