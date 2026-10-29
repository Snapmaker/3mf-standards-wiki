# use_firmware_retraction

> 所在界面：打印机设置 → Basic information → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_advanced.md` 的「Use firmware retraction」小节（2026-10-28），英文原文，待本地化校对。

---

## Use firmware retraction

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `use_firmware_retraction`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--use-firmware-retraction=1`.  
This experimental setting uses G10 and G11 commands to have the firmware handle the retraction. This is only supported in recent Marlin.
