# preheat_time

> 所在界面：工艺设置 → Multimaterial → Ooze prevention
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_ooze_prevention.md` 的「Preheat time」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Preheat time

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `preheat_time`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--preheat-time=1`.  
To reduce the waiting time after tool change, Orca can preheat the next tool while the current tool is still in use. This setting specifies the time in seconds to preheat the next tool. Orca will insert an M104 command to preheat the tool in advance.
