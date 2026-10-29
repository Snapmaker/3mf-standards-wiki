# filament_shrinkage_compensation_z

> 所在界面：耗材设置 → Filament → Basic information
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_basic_information.md` 的「Shrinkage (Z)」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Shrinkage (Z)

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filament_shrinkage_compensation_z`.  
[Type](option_type#list-types): `Percentage list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-shrinkage-compensation-z=20%`.  
Enter the shrinkage percentage that the filament will get after cooling (94% if you measure 94mm instead of 100mm). The part will be scaled in Z to compensate.
