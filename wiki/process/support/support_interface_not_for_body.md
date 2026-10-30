# support_interface_not_for_body

> Location: Process → Support → Support filament

---

### Avoid interface filament for base

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `support_interface_not_for_body`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--support-interface-not-for-body=1`.  
Avoid using the support interface filament to print the support base if possible. This option is shown only when an interface filament is selected and **Support/raft base** is `Default`.

This affects the support **body** only. It is a separate thing from the bonding layer described below, which is part of the interface itself.
