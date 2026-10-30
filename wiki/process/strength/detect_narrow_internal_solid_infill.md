# detect_narrow_internal_solid_infill

> Location: Process → Strength → Advanced

---

## Detect narrow internal solid infill

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `detect_narrow_internal_solid_infill`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--detect-narrow-internal-solid-infill=1`.  
This option auto-detects narrow internal solid infill areas. If enabled, the [concentric pattern](../../process/strength/strength_settings_patterns.md#concentric) will be used in those areas to speed up printing. Otherwise, they use the selected [internal solid infill](../../process/strength/strength_settings_infill.md#internal-solid-infill) pattern (for example, the [rectilinear pattern](../../process/strength/strength_settings_patterns.md#rectilinear)).
