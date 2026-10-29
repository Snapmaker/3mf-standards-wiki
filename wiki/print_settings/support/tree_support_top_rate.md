# tree_support_top_rate

> 所在界面：工艺设置 → Support → Tree supports
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_tree.md` 的「Branch Density」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Branch Density

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `tree_support_top_rate`.  
[Type](option_type#integer-float-percentage): `Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--tree-support-top-rate=20%`.  
Adjusts the density of the support structure used to generate the tips of the branches. A higher value results in better overhangs, but the supports are harder to remove. It is therefore recommended to enable top support interfaces instead of using a high branch density value if dense interfaces are needed.
