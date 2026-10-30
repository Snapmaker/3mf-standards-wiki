# internal_solid_infill_pattern

> Location: Process → Strength → Infill

---

## Internal Solid Infill

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `internal_solid_infill_pattern`.  
[Type](../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../general_settings/option_type.md#choice): `monotonic, monotonicline, rectilinear, alignedrectilinear, concentric, spiralinset, hilbertcurve, archimedeanchords, octagramspiral`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--internal-solid-infill-pattern=monotonic`.  
Line pattern of internal solid infill. If [Detect narrow internal solid infill](../../process/strength/strength_settings_advanced.md#detect-narrow-internal-solid-infill) is enabled, the [Concentric pattern](../../process/strength/strength_settings_patterns.md#concentric) will be used for small areas.
