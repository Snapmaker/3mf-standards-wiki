# internal_solid_infill_pattern

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_infill.md` 的「Internal Solid Infill」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Internal Solid Infill

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `internal_solid_infill_pattern`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `monotonic, monotonicline, rectilinear, alignedrectilinear, concentric, spiralinset, hilbertcurve, archimedeanchords, octagramspiral`.  
[CLI Example](cli_mode#setting-overrides): `--internal-solid-infill-pattern=monotonic`.  
Line pattern of internal solid infill. If [Detect narrow internal solid infill](strength_settings_advanced#detect-narrow-internal-solid-infill) is enabled, the [Concentric pattern](strength_settings_patterns#concentric) will be used for small areas.
