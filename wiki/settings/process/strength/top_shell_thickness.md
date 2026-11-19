# top_shell_thickness

> Location: Process → Strength → Top/bottom shells
> 本小节同时涵盖：`bottom_shell_thickness`（各另有独立文档）。

---

## Shell Thickness

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `top_shell_thickness`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[Default](../../../general_settings/option_type.md#default-value): `0.6`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` mm.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--top-shell-thickness=1`.  
The number of solid layers is increased during slicing if the thickness calculated from shell layers is thinner than this value. This avoids having too thin a shell when layer height is small.  
0 means this setting is disabled and shell thickness is determined entirely by [shell layers](#shell-layers).
