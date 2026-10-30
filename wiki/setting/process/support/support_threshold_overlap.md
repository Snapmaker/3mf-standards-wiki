# support_threshold_overlap

> Location: Process → Support → Support

---

## Threshold overlap

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `support_threshold_overlap`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float or Percentage`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--support-threshold-overlap=20%`.  
If [Threshold angle](#threshold-angle) is zero, support will be generated for overhangs whose overlap with the layer below is below the threshold. A percentage is relative to the outer wall line width.
The smaller this value is, the steeper the overhang that can be printed without support.  
Tree supports don't use this setting, so it is hidden for them.
