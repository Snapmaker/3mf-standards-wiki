# support_ironing

> Location: Process → Support → Support ironing

---

# Support Ironing

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `support_ironing`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--support-ironing=1`.  
Ironing uses a small flow to print over the top support interface again at the same height to make it smoother. This setting controls whether the support interface is ironed. When enabled, the top support interface and the raft interface are also printed solid.

This option is available only when the support has [top interface layers](../../process/support/support_settings_advanced.md#interface-layers) or a [raft](../../process/support/support_settings_raft.md) is used.
