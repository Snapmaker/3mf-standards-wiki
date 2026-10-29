# ironing_spacing

> 所在界面：工艺设置 → Quality → Ironing
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_ironing.md` 的「Line spacing」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Line spacing

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `ironing_spacing`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--ironing-spacing=1`.  
The distance between the lines of ironing.  
It's recommended to set this value to be equal to or less than the nozzle diameter for optimal coverage and surface finish.
