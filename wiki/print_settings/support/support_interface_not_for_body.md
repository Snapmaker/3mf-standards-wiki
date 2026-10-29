# support_interface_not_for_body

> 所在界面：工艺设置 → Support → Support filament
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_filament.md` 的「Avoid interface filament for base」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Avoid interface filament for base

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `support_interface_not_for_body`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--support-interface-not-for-body=1`.  
Avoid using the support interface filament to print the support base if possible. This option is shown only when an interface filament is selected and **Support/raft base** is `Default`.

This affects the support **body** only. It is a separate thing from the bonding layer described below, which is part of the interface itself.
