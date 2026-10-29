# gcode_label_objects

> 所在界面：工艺设置 → Others → G-code output
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_g_code_output.md` 的「Label Objects」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Label Objects

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `gcode_label_objects`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--gcode-label-objects=1`.  
Insert comments that label moves with the object they belong to (object index or name). This is useful for integrations such as OctoPrint's Cancel Object plugin and for human inspection of the G-code.
