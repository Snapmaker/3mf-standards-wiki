# tree_support_branch_diameter_angle

> 所在界面：工艺设置 → Support → Tree supports
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_tree.md` 的「Branch Diameter Angle」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Branch Diameter Angle

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `tree_support_branch_diameter_angle`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--tree-support-branch-diameter-angle=1`.  
The angle of the branches' diameter as they gradually become thicker towards the bottom. An angle of 0 will cause the branches to have uniform thickness over their length. A bit of an angle can increase the stability of the organic support.
