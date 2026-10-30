# sparse_infill_line_width

> Location: Process → Quality → Line width

---

### Sparse Infill

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `sparse_infill_line_width`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float or Percentage`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--sparse-infill-line-width=20%`.  
Recommended to use a conservative value, typically around 115% to improve layer adhesion without getting near volumetric flow limitations.  
If you need stronger infill, it's recommended to use [infill line multiplier](../../process/strength/strength_settings_infill.md#fill-multiline) when possible.
