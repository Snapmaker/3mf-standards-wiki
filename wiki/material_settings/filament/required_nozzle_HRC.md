# required_nozzle_HRC

> 所在界面：耗材设置 → Filament → Basic information
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_basic_information.md` 的「Required nozzle HRC」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Required nozzle HRC

[Mode](option_mode): `Developer`.  
[Variable](built_in_placeholders_variables): `required_nozzle_HRC`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--required-nozzle-HRC=1`.  
Minimum HRC of nozzle required to print the filament. A value of 0 means no checking of the nozzle's HRC.
