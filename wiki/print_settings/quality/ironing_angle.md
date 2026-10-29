# ironing_angle

> 所在界面：工艺设置 → Quality → Ironing
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_ironing.md` 的「Angle Offset」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Angle Offset

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `ironing_angle`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--ironing-angle=1`.  
The angle of ironing lines offset relative to the top surface solid infill direction.  
This option can only be edited when the ironing [Pattern](#pattern) is Rectilinear.

Commonly used ironing angle offsets are 0°, 45°, and 90°, each producing a [different surface finish](https://github.com/OrcaSlicer/OrcaSlicer/issues/10834#issuecomment-3322628589) which will depend on your printer nozzle.

> [!TIP]
> Enable [Align directions to model](strength_settings_advanced#align-directions-to-model) to make the ironing direction follow the model's orientation on the build plate.
