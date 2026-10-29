# interlocking_boundary_avoidance

> 所在界面：工艺设置 → Multimaterial → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_advanced.md` 的「Interlocking Boundary Avoidance」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Interlocking Boundary Avoidance

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `interlocking_boundary_avoidance`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--interlocking-boundary-avoidance=1`.  
The distance from the outside of a model where interlocking structures will not be generated, measured in cells.
