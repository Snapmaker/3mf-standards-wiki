# tree_support_branch_angle

> 所在界面：工艺设置 → Support → Tree supports
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_tree.md` 的「Branch Angle」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`tree_support_branch_angle_organic`（各另有独立文档）。

---

## Branch Angle

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `tree_support_branch_angle`, `tree_support_branch_angle_organic`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--tree-support-branch-angle=1` (same pattern for the other variables above).  
This setting determines the maximum overhang angle that the branches of tree support are allowed to make. If the angle is increased, the branches can be printed more horizontally, allowing them to reach farther.
