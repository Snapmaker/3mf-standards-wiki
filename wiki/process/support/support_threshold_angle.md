# support_threshold_angle

> Location: Process → Support → Support

---

## Threshold angle

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `support_threshold_angle`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--support-threshold-angle=1`.  
Support will be generated for overhangs whose slope angle is below the threshold. The smaller this value is, the steeper the overhang that can be printed without support.  
If set to `0`, normal supports use the [Threshold overlap](#threshold-overlap) instead, while tree supports use 30°.
