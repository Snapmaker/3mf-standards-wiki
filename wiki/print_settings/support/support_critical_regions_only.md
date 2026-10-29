# support_critical_regions_only

> 所在界面：工艺设置 → Support → Support
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_support.md` 的「Support critical regions only」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

#### Support critical regions only

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `support_critical_regions_only`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--support-critical-regions-only=1`.  
Only creates support for critical regions, such as sharp tails and cantilevers. Available only with `Tree (auto)`.
