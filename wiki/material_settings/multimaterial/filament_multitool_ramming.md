# filament_multitool_ramming

> 所在界面：耗材设置 → Multimaterial → Tool change parameters with multi extruder MM printers
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/multimaterial/material_multimaterial.md` 的「Tool change parameters with multi extruder」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Tool change parameters with multi extruder

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filament_multitool_ramming`.  
[Type](option_type#list-types): `Boolean list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-multitool-ramming=1`.  
These options apply to printers that use multiple independent extruders or hotends (multi-tool setups). When enabled, ramming and related parameters define a small, controlled extrusion on the wipe tower immediately before a tool change to ensure the outgoing tool is cleared and the incoming tool begins with consistent filament at the nozzle. Use these settings to tune multi-tool handoffs and avoid color or material mixing.
