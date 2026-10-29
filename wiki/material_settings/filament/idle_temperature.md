# idle_temperature

> 所在界面：耗材设置 → Filament → Basic information
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_basic_information.md` 的「Idle temperature」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Idle temperature

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `idle_temperature`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--idle-temperature=1`.  
Nozzle temperature when the tool is currently not used in multi-tool setups. This is only used when 'Ooze prevention' is active in Print Settings. Set to 0 to disable.
