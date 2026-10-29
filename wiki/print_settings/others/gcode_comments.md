# gcode_comments

> 所在界面：工艺设置 → Others → G-code output
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_g_code_output.md` 的「Verbose G-code」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Verbose G-code

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `gcode_comments`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--gcode-comments=1`.  
Include descriptive comments for G-code lines and blocks to make the file human-readable and easier to debug.  
Verbose mode produces much larger files and may slow down SD-card printing on some printers.
