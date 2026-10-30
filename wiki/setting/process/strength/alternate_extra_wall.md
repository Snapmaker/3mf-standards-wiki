# alternate_extra_wall

> Location: Process → Strength → Walls

---

## Alternate extra wall

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `alternate_extra_wall`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--alternate-extra-wall=1`.  
This setting adds an extra wall to every other layer. This way the infill gets wedged vertically between the walls, resulting in stronger prints.  
This option doesn't work well when Ensure vertical shell thickness is set to **All**; when both are enabled, OrcaSlicer offers to change it to **Moderate**.  

> [!WARNING]
> It's not recommended to use this option with:
>
> - [Lightning infill](../../process/strength/strength_settings_patterns.md#lightning) as there is limited infill to anchor the extra perimeters to.
> - **[Ensure vertical shell thickness: All](../../process/strength/strength_settings_advanced.md#ensure-vertical-shell-thickness)**
