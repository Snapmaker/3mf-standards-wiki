# temperature_vitrification

> 所在界面：耗材设置 → Filament → Basic information
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_basic_information.md` 的「Softening temperature」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Softening temperature

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `temperature_vitrification`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--temperature-vitrification=1`.  
The material softens at this temperature, so when the bed temperature is equal to or greater than this, it's highly recommended to open the front door and/or remove the upper glass to avoid clogs.
