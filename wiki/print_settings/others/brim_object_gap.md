# brim_object_gap

> 所在界面：工艺设置 → Others → Brim
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_brim.md` 的「Brim-Object Gap」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Brim-Object Gap

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `brim_object_gap`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--brim-object-gap=1`.  
Gap between the innermost brim line and the object.  
Increasing the gap makes the brim easier to remove but reduces its adhesion benefit; very large gaps may eliminate contact and negate the brim's purpose.
