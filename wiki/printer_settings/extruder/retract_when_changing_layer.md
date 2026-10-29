# retract_when_changing_layer

> 所在界面：打印机设置 → Extruder N → Retraction
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_retraction.md` 的「Retract on layer change」小节（2026-10-28），英文原文，待本地化校对。

---

## Retract on layer change

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `retract_when_changing_layer[extruder_idx]`.  
[Type](option_type#list-types): `Boolean list`.  
[CLI Example](cli_mode#setting-overrides): `--retract-when-changing-layer=1`.  
This forces a retraction on layer changes.
