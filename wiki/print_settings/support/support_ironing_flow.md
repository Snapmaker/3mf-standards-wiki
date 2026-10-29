# support_ironing_flow

> 所在界面：工艺设置 → Support → Support ironing
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_ironing.md` 的「Flow」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Flow

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `support_ironing_flow`.  
[Type](option_type#integer-float-percentage): `Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--support-ironing-flow=20%`.  
The amount of material to extrude during ironing, relative to the flow of a normal support interface layer. Too high a value results in over-extrusion on the surface.
