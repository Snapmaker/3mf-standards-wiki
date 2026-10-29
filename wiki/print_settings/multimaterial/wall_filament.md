# wall_filament

> 所在界面：工艺设置 → Multimaterial → Filament for Features
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_filament_for_features.md` 的「Outer Walls」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅多耗材（非单喷头多耗材）配置下显示

---

## Outer Walls

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `outer_wall_filament_id`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--outer-wall-filament-id=1`.  
Filament to print outer walls.  
You can also print the outer walls with a translucent filament to achieve a frosted glass effect.  
When using a [mixed nozzle size setup](mixed_nozzle_sizes), it's recommended to use the smaller nozzle for outer walls to achieve better surface quality and detail.
