# filter_out_gap_fill

> Location: Process → Strength → Infill

---

## Filter out tiny gaps

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filter_out_gap_fill`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filter-out-gap-fill=1`.  
Don't print gap fill with a length smaller than the specified threshold (in mm).  
This setting applies to top, bottom and solid infill and, if using the [classic perimeter generator](../../process/quality/quality_settings_wall_generator.md#classic), to wall gap fill.
