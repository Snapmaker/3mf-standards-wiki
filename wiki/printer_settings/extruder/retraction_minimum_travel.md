# retraction_minimum_travel

> 所在界面：打印机设置 → Extruder N → Retraction
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_retraction.md` 的「Travel distance threshold」小节（2026-10-28），英文原文，待本地化校对。

---

## Travel distance threshold

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `retraction_minimum_travel[extruder_idx]`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--retraction-minimum-travel=1`.  
Only trigger retraction when the travel distance is longer than this threshold.
