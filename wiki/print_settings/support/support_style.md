# support_style

> 所在界面：工艺设置 → Support → Support
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_support.md` 的「Style」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Style

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `support_style`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `default, grid, snug, organic, tree_slim, tree_strong, tree_hybrid`.  
[CLI Example](cli_mode#setting-overrides): `--support-style=default`.  
Style and shape of the support.  
Grid and Snug apply to normal supports, while Organic, Tree Slim, Tree Strong and Tree Hybrid apply to tree supports. `Default (Grid/Organic)` uses Grid for normal supports and Organic for tree supports.
