# tree_support_auto_brim

> Location: Process → Support → Tree supports

---

## Auto brim width

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `tree_support_auto_brim`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--tree-support-auto-brim=1`.  
On the first layer, each branch is widened by a brim that helps it stick to the build plate. When this is enabled, the brim width is calculated per branch as half the branch height divided by its radius at the plate, so tall, thin branches get a wider brim: a 40 mm tall branch with a 2 mm radius gets a 10 mm brim. It is never less than 2 mm, and is otherwise capped so that a branch and its brim stay within 12 mm of the branch center.

The brim is only added when there is no raft. With the Tree Hybrid style, it is added to the branches only; the parts printed as normal support use [Initial layer expansion](../../process/support/support_settings_support.md#initial-layer-expansion) instead.
