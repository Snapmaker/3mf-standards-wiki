# filament_type

> 所在界面：耗材设置 → Filament → Basic information
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_basic_information.md` 的「Type」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Type

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `filament_type`.  
[Type](option_type#list-types): `Text list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-type=value`.  
Material base type (e.g., PLA, ABS, PETG, etc.).  
This setting affects coefficients used in various calculations, such as brim width or temperature warnings.
