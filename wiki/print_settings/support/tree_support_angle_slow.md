# tree_support_angle_slow

> 所在界面：工艺设置 → Support → Tree supports
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_tree.md` 的「Preferred Branch Angle」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Preferred Branch Angle

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `tree_support_angle_slow`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--tree-support-angle-slow=1`.  
The preferred angle of the branches, when they do not have to avoid the model. Use a lower angle to make them more vertical and more stable. Use a higher angle for branches to merge faster.
