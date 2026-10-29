# support_ironing

> 所在界面：工艺设置 → Support → Support ironing
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_ironing.md` 的「Support Ironing」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

# Support Ironing

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `support_ironing`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--support-ironing=1`.  
Ironing uses a small flow to print over the top support interface again at the same height to make it smoother. This setting controls whether the support interface is ironed. When enabled, the top support interface and the raft interface are also printed solid.

This option is available only when the support has [top interface layers](support_settings_advanced#interface-layers) or a [raft](support_settings_raft) is used.
