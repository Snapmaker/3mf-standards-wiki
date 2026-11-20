# wipe_tower_wall_gap

> Location: Process → Multimaterial → Prime tower → Wall gap
> Status: placeholder — to be completed.

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `wipe_tower_wall_gap`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `true`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--wipe-tower-wall-gap=1`.  

Create small gaps in the wipe tower outer wall at tool change entry points. The first extrusion path after a filament change will enter through the gap, leaving the filament blob on the gap edge instead of on the outer wall surface.
