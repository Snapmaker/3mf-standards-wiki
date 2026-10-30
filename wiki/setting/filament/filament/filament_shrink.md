# filament_shrink

> Location: Filament → Filament → Basic information

---

## Shrinkage (XY)

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_shrink`.  
[Type](../../../general_settings/option_type.md#list-types): `Percentage list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-shrink=20%`.  
Enter the shrinkage percentage that the filament will get after cooling (94% if you measure 94mm instead of 100mm).  
The part will be scaled in XY to compensate. Only the filament used for the perimeter is taken into account.  
Be sure to allow enough space between objects, as this compensation is done after the checks.
