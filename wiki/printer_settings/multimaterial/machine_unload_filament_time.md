# machine_unload_filament_time

> 所在界面：打印机设置 → Multimaterial → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/multimaterial/printer_multimaterial_advanced.md` 的「Filament unload time」小节（2026-10-28），英文原文，待本地化校对。

---

## Filament unload time

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `machine_unload_filament_time`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--machine-unload-filament-time=1`.  
Time to unload old filament when switch filament. It's usually applicable for single-extruder multi-material machines. For tool changers or multi-tool machines, it's typically 0. For statistics only.
