# thumbnails

> 所在界面：打印机设置 → Basic information → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_advanced.md` 的「G-code thumbnails」小节（2026-10-28），英文原文，待本地化校对。

---

## G-code thumbnails

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `thumbnails`.  
[Type](option_type#text): `Text`.  
[CLI Example](cli_mode#setting-overrides): `--thumbnails=48x48/PNG,300x300/PNG`.  
Picture sizes to be stored into a .gcode and .sl1 / .sl1s files, in the following format: "XxY, XxY, ..."
