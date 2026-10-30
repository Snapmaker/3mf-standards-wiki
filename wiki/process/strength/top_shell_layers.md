# top_shell_layers

> Location: Process → Strength → Top/bottom shells
> 本小节同时涵盖：`bottom_shell_layers`（各另有独立文档）。

---

## Shell Layers

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `top_shell_layers`, `bottom_shell_layers`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--top-shell-layers=1` (same pattern for the other variables above).  
This is the number of solid shell layers, including the surface layer.  
When the thickness calculated from this value is less than [shell thickness](#shell-thickness), the shell layers will be increased.

These layers are printed over the [sparse infill](../../process/strength/strength_settings_infill.md), so increasing **shell layers** will increase overall part strength and top surface quality.
It's usually recommended to have at least 3 shell layers for most prints.
