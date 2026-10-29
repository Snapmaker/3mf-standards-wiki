# filament_diameter

> 所在界面：耗材设置 → Filament → Basic information
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_basic_information.md` 的「Diameter」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅非 pellet（丝料）机型显示

---

## Diameter

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `filament_diameter`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-diameter=1`.  
Filament diameter is used to calculate extrusion variables in G-code, so it is important that this is accurate and precise.
