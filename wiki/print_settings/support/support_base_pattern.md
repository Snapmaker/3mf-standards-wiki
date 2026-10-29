# support_base_pattern

> 所在界面：工艺设置 → Support → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_advanced.md` 的「Base Pattern」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Base Pattern

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `support_base_pattern`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `default, rectilinear, rectilinear-grid, honeycomb, lightning, hollow`.  
[CLI Example](cli_mode#setting-overrides): `--support-base-pattern=default`.  
Line pattern for the base of the support.

`Default` depends on the support type: normal supports use `Rectilinear`, and tree supports are left `Hollow`, with only the branch walls printed. With the [Tree Hybrid](support_settings_support#tree-hybrid) style, `Default` fills the parts printed as normal support with `Rectilinear` and leaves the branches hollow, while choosing `Rectilinear` fills the branches too.
