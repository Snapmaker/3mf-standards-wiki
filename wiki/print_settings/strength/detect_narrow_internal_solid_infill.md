# detect_narrow_internal_solid_infill

> 所在界面：工艺设置 → Strength → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_advanced.md` 的「Detect narrow internal solid infill」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Detect narrow internal solid infill

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `detect_narrow_internal_solid_infill`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--detect-narrow-internal-solid-infill=1`.  
This option auto-detects narrow internal solid infill areas. If enabled, the [concentric pattern](strength_settings_patterns#concentric) will be used in those areas to speed up printing. Otherwise, they use the selected [internal solid infill](strength_settings_infill#internal-solid-infill) pattern (for example, the [rectilinear pattern](strength_settings_patterns#rectilinear)).
