# support_remove_small_overhang

> 所在界面：工艺设置 → Support → Support
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_support.md` 的「Ignore small overhangs」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Ignore small overhangs

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `support_remove_small_overhang`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--support-remove-small-overhang=1`.  
With this setting, small overhangs that possibly don't need support are ignored by support generation.
