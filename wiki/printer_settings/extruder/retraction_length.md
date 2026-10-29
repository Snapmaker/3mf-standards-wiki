# retraction_length

> 所在界面：打印机设置 → Extruder N → Retraction
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_retraction.md` 的「Length」小节（2026-10-28），英文原文，待本地化校对。

---

## Length

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `retraction_length[extruder_idx]`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--retraction-length=1`.  
When retraction is triggered before changing tool, filament is pulled back by the specified amount (the length is measured on raw filament, before it enters the extruder).
