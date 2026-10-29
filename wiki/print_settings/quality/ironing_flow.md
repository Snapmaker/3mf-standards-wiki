# ironing_flow

> 所在界面：工艺设置 → Quality → Ironing
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_ironing.md` 的「Flow」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Flow

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `ironing_flow`.  
[Type](option_type#integer-float-percentage): `Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--ironing-flow=20%`.  
The amount of material to extrude during ironing.  
It is a percentage of the flow of a normal layer height. A lower value will result in a smoother finish but may not cover the surface completely. A higher value may cover the surface better but can lead to over-extrusion or a rougher finish.

A lower layer height may require higher flow due to less volumetric extrusion per distance.
