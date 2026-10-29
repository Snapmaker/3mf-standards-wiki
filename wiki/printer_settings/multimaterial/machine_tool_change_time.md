# machine_tool_change_time

> 所在界面：打印机设置 → Multimaterial → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/multimaterial/printer_multimaterial_advanced.md` 的「Tool change time」小节（2026-10-28），英文原文，待本地化校对。

---

## Tool change time

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `machine_tool_change_time`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--machine-tool-change-time=1`.  
Time taken to switch tools. It's usually applicable for tool changers or multi-tool machines. For single-extruder multi-material machines, it's typically 0. For statistics only.
