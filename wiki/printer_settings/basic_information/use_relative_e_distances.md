# use_relative_e_distances

> 所在界面：打印机设置 → Basic information → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_advanced.md` 的「Use relative E distances」小节（2026-10-28），英文原文，待本地化校对。

---

## Use relative E distances

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `use_relative_e_distances`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--use-relative-e-distances=1`.  
Relative extrusion is recommended when using "label_objects" option. Some extruders work better with this option unchecked (absolute extrusion mode). Wipe tower is only compatible with relative mode. It is recommended on most printers. Default is checked.
