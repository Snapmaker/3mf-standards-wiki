# align_infill_direction_to_model

> 所在界面：工艺设置 → Strength → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_advanced.md` 的「Align directions to model」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Align directions to model

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `align_infill_direction_to_model`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--align-infill-direction-to-model=1`.  
Aligns [infill](strength_settings_infill#direction), [bridge](#bridge-infill-direction), [ironing](quality_settings_ironing#angle-offset) and [top/bottom surface fill](strength_settings_top_bottom_shells#surface-pattern) directions to follow the model's orientation on the build plate.  
When enabled, these directions rotate together with the model so the printed features keep their intended orientation relative to the part, preserving optimal strength and surface characteristics regardless of how the model is placed.

![fill-direction-to-model](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/fill-direction-to-model.png?raw=true)
