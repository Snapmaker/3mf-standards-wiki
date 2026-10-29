# filament_cooling_moves

> 所在界面：耗材设置 → Multimaterial → Tool change parameters with single extruder MM printers
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/multimaterial/material_multimaterial.md` 的「Number of cooling moves」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Number of cooling moves

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filament_cooling_moves`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-cooling-moves=1`.  
Filament is cooled by being moved back and forth in the cooling tubes. Specify desired number of these moves.
