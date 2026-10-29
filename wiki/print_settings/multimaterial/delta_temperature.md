# delta_temperature

> 所在界面：工艺设置 → Multimaterial → Ooze prevention
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_ooze_prevention.md` 的「Temperature variation」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`standby_temperature_delta`（各另有独立文档）。

---

## Temperature variation

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `standby_temperature_delta`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--standby-temperature-delta=1`.  
Temperature difference to be applied when an extruder is not active. The value is not used when [Idle temperature](material_basic_information#idle-temperature) in the filament settings is set to a non-zero value.
