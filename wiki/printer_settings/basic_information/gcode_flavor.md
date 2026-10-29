# gcode_flavor

> 所在界面：打印机设置 → Basic information → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_advanced.md` 的「G-code flavor」小节（2026-10-28），英文原文，待本地化校对。

---

## G-code flavor

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `gcode_flavor`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `marlin, klipper, reprapfirmware, repetier, marlin2`.  
[CLI Example](cli_mode#setting-overrides): `--gcode-flavor=marlin`.  
What kind of G-code the printer is compatible with.
