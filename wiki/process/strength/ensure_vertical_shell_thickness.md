# ensure_vertical_shell_thickness

> Location: Process → Strength → Advanced

---

## Ensure vertical shell thickness

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `ensure_vertical_shell_thickness`.  
[Type](../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../general_settings/option_type.md#choice): `none, ensure_critical_only, ensure_moderate, ensure_all`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--ensure-vertical-shell-thickness=none`.  
Add solid infill near sloping surfaces to guarantee the vertical shell thickness (top and bottom solid layers).

- **None**: No solid infill will be added anywhere. **Caution:** Use this option carefully if your model has sloped surfaces.
- **Critical Only**: Avoid adding solid infill for walls.
- **Moderate**: Add solid infill for heavily sloping surfaces only.
- **All (default)**: Add solid infill for all suitable sloping surfaces.
