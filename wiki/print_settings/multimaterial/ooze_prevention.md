# ooze_prevention

> 所在界面：工艺设置 → Multimaterial → Ooze prevention
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_ooze_prevention.md` 的「Ooze prevention」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅多耗材打印时显示

---

# Ooze prevention

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `ooze_prevention`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--ooze-prevention=1`.  
This option will drop the temperature of the inactive extruders to prevent oozing.
