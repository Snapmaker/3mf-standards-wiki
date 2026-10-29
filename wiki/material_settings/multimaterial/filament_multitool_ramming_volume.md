# filament_multitool_ramming_volume

> 所在界面：耗材设置 → Multimaterial → Tool change parameters with multi extruder MM printers
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/multimaterial/material_multimaterial.md` 的「Multi-tool ramming volume」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：需先启用 filament_multitool_ramming 后显示

---

#### Multi-tool ramming volume

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filament_multitool_ramming_volume`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-multitool-ramming-volume=1`.  
The volume to be rammed before the tool change.
