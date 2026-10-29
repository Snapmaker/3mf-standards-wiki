# infill_combination

> 所在界面：工艺设置 → Strength → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_advanced.md` 的「Infill Combination」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Infill Combination

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `infill_combination`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--infill-combination=1`.  
Automatically combine [sparse infill](strength_settings_infill) of several layers so they print together, reducing print time. Walls are still printed with the original [layer height](quality_settings_layer_height).

![fill-combination](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/fill-combination.png?raw=true)
