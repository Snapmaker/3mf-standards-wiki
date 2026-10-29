# default_acceleration

> 所在界面：工艺设置 → Speed → Acceleration
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_acceleration.md` 的「Normal printing」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Normal printing

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `default_acceleration`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--default-acceleration=1`.  
The default acceleration for both normal printing and travel after the first layer.

> [!NOTE]
> If this value is set to 0, Orca doesn't send acceleration commands, so the printer's own acceleration is used and the other acceleration settings are disabled.
