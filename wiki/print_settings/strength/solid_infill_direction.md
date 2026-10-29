# solid_infill_direction

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_infill.md` 的「Direction」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`infill_direction`（各另有独立文档）。

---

### Direction

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `infill_direction`, `solid_infill_direction`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--infill-direction=1` (same pattern for the other variables above).  
Controls the direction of the infill lines to optimize or strengthen the print.

[Adaptive Cubic](strength_settings_patterns#adaptive-cubic) and [Support Cubic](strength_settings_patterns#support-cubic) do not support rotation, so the sparse infill direction and the sparse infill [rotation template](#rotation) are disabled for them. The solid infill direction and rotation template are not affected.

![fill-direction](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/fill-direction.png?raw=true)

> [!TIP]
> Enable [Align directions to model](strength_settings_advanced#align-directions-to-model) to make this direction follow the model's orientation on the build plate.
