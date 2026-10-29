# preheat_steps

> 所在界面：工艺设置 → Multimaterial → Ooze prevention
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_ooze_prevention.md` 的「Preheat steps」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Preheat steps

[Mode](option_mode): `Developer`.  
[Variable](built_in_placeholders_variables): `preheat_steps`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--preheat-steps=1`.  
Inserts multiple preheat commands (e.g. M104.1). Only useful for the Prusa XL. For other printers, set it to 1.
