# gcode_add_line_number

> 所在界面：工艺设置 → Others → G-code output
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_g_code_output.md` 的「Add line number」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Add line number

[Mode](option_mode): `Developer`.  
[Variable](built_in_placeholders_variables): `gcode_add_line_number`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--gcode-add-line-number=1`.  
Prefix each G-code line with a sequential line number (N1, N2, ...). Useful for debugging or tools that expect numbered G-code.
