# compatible_printers_condition

> 所在界面：耗材设置 → Dependencies → Compatible printers
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/dependencies/material_dependencies.md` 的「Printer Condition」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Printer Condition

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `compatible_printers_condition`.  
[Type](option_type#text): `Text`.  
Not available via CLI — see [Setting Overrides](cli_mode#setting-overrides) for the full list of excluded keys.  
 boolean expression using the configuration values of an active printer profile.  
 If this expression evaluates to true, this profile is considered compatible with the active printer profile.
