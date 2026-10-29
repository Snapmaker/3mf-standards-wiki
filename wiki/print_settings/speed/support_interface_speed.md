# support_interface_speed

> 所在界面：工艺设置 → Speed → Other layers speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_other_layers_speed.md` 的「Support interface」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Support interface

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `support_interface_speed`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--support-interface-speed=1`.  
Speed for the support interface layers, which are the layers directly contacting the model. This is usually set even slower than the main [support speed](#support) to maximize surface quality where the support meets the model and to make support removal easier.
