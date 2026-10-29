# bridge_no_support

> 所在界面：工艺设置 → Support → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_advanced.md` 的「Don't support bridges」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Don't support bridges

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `bridge_no_support`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--bridge-no-support=1`.  
Don't support bridge areas, which would otherwise make the support very large. Bridges can usually be printed directly without support if they are not very long.

This option is only shown for normal supports. Tree supports use [Max bridge length](#max-bridge-length) instead.
