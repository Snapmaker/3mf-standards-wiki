# retract_restart_extra

> 所在界面：打印机设置 → Extruder N → Retraction
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_retraction.md` 的「Extra length on restart」小节（2026-10-28），英文原文，待本地化校对。

---

## Extra length on restart

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `retract_restart_extra[extruder_idx]`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--retract-restart-extra=1`.  
When the retraction is compensated after changing tool, the extruder will push this additional amount of filament.
