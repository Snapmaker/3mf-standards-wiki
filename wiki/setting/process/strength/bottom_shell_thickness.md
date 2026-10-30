# bottom_shell_thickness

> Location: Process → Strength → Top/bottom shells
> 本小节同时涵盖：`top_shell_thickness`（各另有独立文档）。

---

## Shell Thickness

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `top_shell_thickness`, `bottom_shell_thickness`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--top-shell-thickness=1` (same pattern for the other variables above).  
The number of solid layers is increased during slicing if the thickness calculated from shell layers is thinner than this value. This avoids having too thin a shell when layer height is small.  
0 means this setting is disabled and shell thickness is determined entirely by [shell layers](#shell-layers).
