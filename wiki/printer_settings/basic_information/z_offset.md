# z_offset

> 所在界面：打印机设置 → Basic information → Printable space
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_printable_space.md` 的「Z offset」小节（2026-10-28），英文原文，待本地化校对。

---

## Z offset

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `z_offset`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--z-offset=1`.  
This value will be added (or subtracted) from all the Z coordinates in the output G-code. It is used to compensate for bad Z endstop position: for example, if your endstop zero actually leaves the nozzle 0.3mm far from the print bed, set this to -0.3 (or fix your endstop).
