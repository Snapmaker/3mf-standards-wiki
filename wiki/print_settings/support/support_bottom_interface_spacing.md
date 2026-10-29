# support_bottom_interface_spacing

> 所在界面：工艺设置 → Support → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_advanced.md` 的「Interface spacing」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`support_interface_spacing`（各另有独立文档）。

---

## Interface spacing

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `support_interface_spacing`, `support_bottom_interface_spacing`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--support-interface-spacing=1` (same pattern for the other variables above).  
Spacing of interface lines. Zero means solid interface.

The top (`support_interface_spacing`) and bottom (`support_bottom_interface_spacing`) values are set separately and neither one affects the other, so a bottom interface keeps the spacing you gave it even if you have turned top interfaces off.

When [Support ironing](support_settings_ironing) is enabled, the top interface is always printed solid and the top value is ignored.
