# top_shell_layers

> Location: Process → Strength → Top/bottom shells
> 本小节同时涵盖：`bottom_shell_layers`（各另有独立文档）。

---

## Shell Layers

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `top_shell_layers`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[Default](../../../general_settings/option_type.md#default-value): `4`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` layers.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--top-shell-layers=1`.  
This is the number of solid shell layers, including the surface layer.  
When the thickness calculated from this value is less than [shell thickness](#shell-thickness), the shell layers will be increased.

These layers are printed over the [sparse infill](../../process/strength/sparse_infill_density.md), so increasing **shell layers** will increase overall part strength and top surface quality.
It's usually recommended to have at least 3 shell layers for most prints.
