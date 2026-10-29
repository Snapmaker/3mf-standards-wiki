# ironing_pattern

> 所在界面：工艺设置 → Quality → Ironing
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_ironing.md` 的「Pattern」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Pattern

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `ironing_pattern`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `rectilinear, concentric`.  
[CLI Example](cli_mode#setting-overrides): `--ironing-pattern=rectilinear`.  
The pattern that will be used when ironing. Usually, the best pattern is the one with the most efficient coverage of the surface.  

> [!TIP]
> See [Infill Patterns Wiki List](strength_settings_patterns) with **detailed specifications**, including their strengths and weaknesses.

The ironing patterns are:

- **[Concentric](strength_settings_patterns#concentric)**
- **[Rectilinear](strength_settings_patterns#rectilinear)**
