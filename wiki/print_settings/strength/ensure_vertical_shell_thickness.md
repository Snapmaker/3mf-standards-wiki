# ensure_vertical_shell_thickness

> 所在界面：工艺设置 → Strength → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_advanced.md` 的「Ensure vertical shell thickness」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Ensure vertical shell thickness

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `ensure_vertical_shell_thickness`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `none, ensure_critical_only, ensure_moderate, ensure_all`.  
[CLI Example](cli_mode#setting-overrides): `--ensure-vertical-shell-thickness=none`.  
Add solid infill near sloping surfaces to guarantee the vertical shell thickness (top and bottom solid layers).

- **None**: No solid infill will be added anywhere. **Caution:** Use this option carefully if your model has sloped surfaces.
- **Critical Only**: Avoid adding solid infill for walls.
- **Moderate**: Add solid infill for heavily sloping surfaces only.
- **All (default)**: Add solid infill for all suitable sloping surfaces.
