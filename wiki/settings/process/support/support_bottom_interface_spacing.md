# support_bottom_interface_spacing

> Location: Process → Support → Advanced
> Also in this section: `support_interface_spacing` (each documented on its own page).

---

## Interface spacing

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `support_bottom_interface_spacing`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[Default](../../../general_settings/option_type.md#default-value): `0.5`.  
[Unit](../../../general_settings/option_type.md#unit): `mm`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--support-bottom-interface-spacing=1`.  

Spacing of interface lines. Zero means solid interface.

The top (`support_interface_spacing`) and bottom (`support_bottom_interface_spacing`) values are set separately and neither one affects the other, so a bottom interface keeps the spacing you gave it even if you have turned top interfaces off.

When [Support ironing](../../process/support/support_ironing.md) is enabled, the top interface is always printed solid and the top value is ignored.
