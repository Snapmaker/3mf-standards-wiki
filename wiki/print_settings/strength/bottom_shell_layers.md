# bottom_shell_layers

> 所在界面：工艺设置 → Strength → Top/bottom shells
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_top_bottom_shells.md` 的「Shell Layers」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`top_shell_layers`（各另有独立文档）。

---

## Shell Layers

[Mode](option_mode): `Simple`.  
[Variables](built_in_placeholders_variables): `top_shell_layers`, `bottom_shell_layers`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--top-shell-layers=1` (same pattern for the other variables above).  
This is the number of solid shell layers, including the surface layer.  
When the thickness calculated from this value is less than [shell thickness](#shell-thickness), the shell layers will be increased.

These layers are printed over the [sparse infill](strength_settings_infill), so increasing **shell layers** will increase overall part strength and top surface quality.
It's usually recommended to have at least 3 shell layers for most prints.
