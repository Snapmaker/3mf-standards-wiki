# extrusion_rate_smoothing_external_perimeter_only

> 所在界面：工艺设置 → Speed → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_advanced.md` 的「Apply only on external features」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Apply only on external features

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `extrusion_rate_smoothing_external_perimeter_only`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--extrusion-rate-smoothing-external-perimeter-only=1`.  
Applies extrusion rate smoothing only to outer walls and overhang walls, leaving the flow of all other features unchanged. This can reduce artifacts caused by sharp speed transitions on visible overhangs without slowing down features that won't be seen.  
This option is only shown when Extrusion rate smoothing is greater than 0, and it is disabled by default.
