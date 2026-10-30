# support_bottom_interface_spacing

> Location: Process → Support → Advanced
> 本小节同时涵盖：`support_interface_spacing`（各另有独立文档）。

---

## Interface spacing

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `support_interface_spacing`, `support_bottom_interface_spacing`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--support-interface-spacing=1` (same pattern for the other variables above).  
Spacing of interface lines. Zero means solid interface.

The top (`support_interface_spacing`) and bottom (`support_bottom_interface_spacing`) values are set separately and neither one affects the other, so a bottom interface keeps the spacing you gave it even if you have turned top interfaces off.

When [Support ironing](../../process/support/support_settings_ironing.md) is enabled, the top interface is always printed solid and the top value is ignored.
