# complete_print_exhaust_fan_speed

> 所在界面：耗材设置 → Cooling → Exhaust fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Complete print」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

#### Complete print

[Mode](option_mode): `Simple`.  
[Variables](built_in_placeholders_variables): `activate_air_filtration_on_completion`, `complete_print_exhaust_fan_speed`.  
[Type](option_type): `activate_air_filtration_on_completion` (Boolean list), `complete_print_exhaust_fan_speed` (Integer list).  
[CLI Example](cli_mode#setting-overrides): `--activate-air-filtration-on-completion=1` (`activate_air_filtration_on_completion` shown; other variables above follow their own type).  
Speed of exhaust fan after printing completes.
