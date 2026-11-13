# internal_solid_infill_line_width

> Location: Process → Quality → Line width

---

### Internal Solid Infill

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `internal_solid_infill_line_width`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float or Percentage`.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[Range](../../../general_settings/option_type.md#range): `0–1000` mm or %.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--internal-solid-infill-line-width=20%`.  
Used for internal solid infill, bottom surfaces, and [100% infill](../../process/strength/sparse_infill_density.md).  
Recommended: **~110%** for good layer adhesion and visual quality.
