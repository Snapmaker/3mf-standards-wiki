# bed_exclude_area

> 所在界面：打印机设置 → Basic information → Printable space
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_printable_space.md` 的「Excluded bed area」小节（2026-10-28），英文原文，待本地化校对。

---

## Excluded bed area

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `bed_exclude_area`.  
[Type](option_type#list-types): `Point list`.  
[CLI Example](cli_mode#setting-overrides): `--bed-exclude-area=100,100`.  
Unprintable area in XY plane. For example, X1 Series printers use the front left corner to cut filament during filament change. The area is expressed as polygon by points in following format: "XxY, XxY, ..."  
It keeps models and printed material out of the area, but the toolhead can still travel through it, as the X1 does to cut the filament. To also keep the toolhead's moves out, set [Toolhead collision volumes](#toolhead-collision-volumes).
