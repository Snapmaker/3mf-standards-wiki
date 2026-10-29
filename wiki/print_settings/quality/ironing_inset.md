# ironing_inset

> 所在界面：工艺设置 → Quality → Ironing
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_ironing.md` 的「Inset」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Inset

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `ironing_inset`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--ironing-inset=1`.  
The distance to keep from the edges, which can help prevent over-extrusion at the edges of the surface being ironed.

![ironing-inset](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/ironing/ironing-inset.png?raw=true)

If this value is set to 0, an inset of half the nozzle diameter is used, so the [ironing pattern](#pattern) stays slightly inside the outer boundaries of the top surface being ironed.
