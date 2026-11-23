# ramming_line_width_ratio

> Location: Printer → Multimaterial → Wipe tower → Ramming line width ratio
> Status: placeholder — Snapmaker Orca-specific parameter, to be completed.

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `ramming_line_width_ratio`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[Default](../../../general_settings/option_type.md#default-value): `2.0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--ramming-line-width-ratio=1`.  

This is used to decide the line width of wipe tower when ramming, ramming line width = [this ratio] * extruder * 1.25
