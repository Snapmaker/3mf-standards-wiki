# high_current_on_filament_swap

> 所在界面：打印机设置 → Multimaterial → Single extruder multi-material parameters
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/multimaterial/printer_multimaterial_semm_parameters.md` 的「High extruder current on filament swap」小节（2026-10-28），英文原文，待本地化校对。

---

## High extruder current on filament swap

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `high_current_on_filament_swap`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--high-current-on-filament-swap=1`.  
 It may be beneficial to increase the extruder motor current during the filament exchange sequence to allow for rapid ramming feed rates and to overcome resistance when loading a filament with an ugly shaped tip.
