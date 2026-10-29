# exclude_object

> 所在界面：工艺设置 → Others → G-code output
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_g_code_output.md` 的「Exclude Objects」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Exclude Objects

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `exclude_object`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--exclude-object=1`.  
Add commands to the G-code that define each object and mark where it starts and ends, so the printer firmware can skip (cancel) individual objects during the print: `EXCLUDE_OBJECT_DEFINE`, `EXCLUDE_OBJECT_START` and `EXCLUDE_OBJECT_END` for Klipper, and `M486` for Marlin and RepRapFirmware.
