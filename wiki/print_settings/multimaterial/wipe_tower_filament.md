# wipe_tower_filament

> 所在界面：工艺设置 → Multimaterial → Filament for Features
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_filament_for_features.md` 的「Wipe Tower」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅多耗材（非单喷头多耗材）配置下显示

---

## Wipe Tower

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wipe_tower_filament`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--wipe-tower-filament=1`.  
Filament to print the perimeter of the wipe tower. Set to `Default` to use any available filament, preferring a non-soluble one.
