# tree_support_auto_brim

> 所在界面：工艺设置 → Support → Tree supports
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_tree.md` 的「Auto brim width」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Auto brim width

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `tree_support_auto_brim`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--tree-support-auto-brim=1`.  
On the first layer, each branch is widened by a brim that helps it stick to the build plate. When this is enabled, the brim width is calculated per branch as half the branch height divided by its radius at the plate, so tall, thin branches get a wider brim: a 40 mm tall branch with a 2 mm radius gets a 10 mm brim. It is never less than 2 mm, and is otherwise capped so that a branch and its brim stay within 12 mm of the branch center.

The brim is only added when there is no raft. With the Tree Hybrid style, it is added to the branches only; the parts printed as normal support use [Initial layer expansion](support_settings_support#initial-layer-expansion) instead.
