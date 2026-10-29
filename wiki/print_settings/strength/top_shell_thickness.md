# top_shell_thickness

> 所在界面：工艺设置 → Strength → Top/bottom shells
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_top_bottom_shells.md` 的「Shell Thickness」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`bottom_shell_thickness`（各另有独立文档）。

---

## Shell Thickness

[Mode](option_mode): `Simple`.  
[Variables](built_in_placeholders_variables): `top_shell_thickness`, `bottom_shell_thickness`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--top-shell-thickness=1` (same pattern for the other variables above).  
The number of solid layers is increased during slicing if the thickness calculated from shell layers is thinner than this value. This avoids having too thin a shell when layer height is small.  
0 means this setting is disabled and shell thickness is determined entirely by [shell layers](#shell-layers).
