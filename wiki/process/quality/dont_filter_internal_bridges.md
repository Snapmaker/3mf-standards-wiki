# dont_filter_internal_bridges

> Location: Process → Quality → Bridging

---

## Filter out small internal bridges

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `dont_filter_internal_bridges`.  
[Type](../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../general_settings/option_type.md#choice): `disabled, limited, nofilter`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--dont-filter-internal-bridges=disabled`.  
This option can help reduce pillowing on top surfaces in heavily slanted or curved models.

By default, small internal bridges are filtered out and the internal solid infill is printed directly over the sparse infill. This works well in most cases, speeding up printing without too much compromise on top surface quality.

However, in heavily slanted or curved models, especially where too low a sparse infill density is used, this may result in curling of the unsupported solid infill, causing pillowing.

Enabling limited filtering or no filtering will print an internal bridge layer over slightly unsupported internal solid infill. The options below control the sensitivity of the filtering, i.e. they control where internal bridges are created:

- **Filter:** enables this option. This is the default behavior and works well in most cases.
- **Limited filtering:** creates internal bridges on heavily slanted surfaces while avoiding unnecessary bridges. This works well for most difficult models.
- **No filtering:** creates internal bridges on every potential internal overhang. This option is useful for heavily slanted top surface models; however, in most cases, it creates too many unnecessary bridges.
