# support_interface_filament

> 所在界面：工艺设置 → Support → Support filament
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_filament.md` 的「Interface」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Interface

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `support_interface_filament`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--support-interface-filament=1`.  
Filament to print the support interface. "Default" means no specific filament for the support interface, and the current filament is used.
