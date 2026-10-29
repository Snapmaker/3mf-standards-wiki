# alternate_extra_wall

> 所在界面：工艺设置 → Strength → Walls
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_walls.md` 的「Alternate extra wall」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Alternate extra wall

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `alternate_extra_wall`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--alternate-extra-wall=1`.  
This setting adds an extra wall to every other layer. This way the infill gets wedged vertically between the walls, resulting in stronger prints.  
This option doesn't work well when Ensure vertical shell thickness is set to **All**; when both are enabled, OrcaSlicer offers to change it to **Moderate**.  

> [!WARNING]
> It's not recommended to use this option with:
>
> - [Lightning infill](strength_settings_patterns#lightning) as there is limited infill to anchor the extra perimeters to.
> - **[Ensure vertical shell thickness: All](strength_settings_advanced#ensure-vertical-shell-thickness)**
