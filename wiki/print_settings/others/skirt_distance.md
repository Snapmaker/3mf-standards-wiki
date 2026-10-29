# skirt_distance

> 所在界面：工艺设置 → Others → Skirt
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_skirt.md` 的「Distance」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Distance

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `skirt_distance`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--skirt-distance=1`.  
Distance from skirt to brim or object.  
Increasing this distance can help avoid collisions with brims or supports, but will increase the footprint of the skirt and filament usage.
