# wipe

> 所在界面：打印机设置 → Extruder N → Retraction
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_retraction.md` 的「Wipe while retracting」小节（2026-10-28），英文原文，待本地化校对。

---

## Wipe while retracting

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wipe[extruder_idx]`.  
[Type](option_type#list-types): `Boolean list`.  
[CLI Example](cli_mode#setting-overrides): `--wipe=1`.  
This moves the nozzle along the last extrusion path when retracting to clean any leaked material on the nozzle. This can minimize blobs when printing a new part after traveling.
