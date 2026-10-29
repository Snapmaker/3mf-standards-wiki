# tree_support_brim_width

> 所在界面：工艺设置 → Support → Tree supports
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_tree.md` 的「Tree support brim width」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Tree support brim width

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `tree_support_brim_width`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--tree-support-brim-width=1`.  
The brim width used when [Auto brim width](#auto-brim-width) is disabled: the distance from the edge of each branch to the outer edge of its brim. `0` disables the brim.
