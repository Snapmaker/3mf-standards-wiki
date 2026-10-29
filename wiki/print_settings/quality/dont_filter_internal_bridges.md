# dont_filter_internal_bridges

> 所在界面：工艺设置 → Quality → Bridging
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_bridging.md` 的「Filter out small internal bridges」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Filter out small internal bridges

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `dont_filter_internal_bridges`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `disabled, limited, nofilter`.  
[CLI Example](cli_mode#setting-overrides): `--dont-filter-internal-bridges=disabled`.  
This option can help reduce pillowing on top surfaces in heavily slanted or curved models.

By default, small internal bridges are filtered out and the internal solid infill is printed directly over the sparse infill. This works well in most cases, speeding up printing without too much compromise on top surface quality.

However, in heavily slanted or curved models, especially where too low a sparse infill density is used, this may result in curling of the unsupported solid infill, causing pillowing.

Enabling limited filtering or no filtering will print an internal bridge layer over slightly unsupported internal solid infill. The options below control the sensitivity of the filtering, i.e. they control where internal bridges are created:

- **Filter:** enables this option. This is the default behavior and works well in most cases.
- **Limited filtering:** creates internal bridges on heavily slanted surfaces while avoiding unnecessary bridges. This works well for most difficult models.
- **No filtering:** creates internal bridges on every potential internal overhang. This option is useful for heavily slanted top surface models; however, in most cases, it creates too many unnecessary bridges.
