# travel_speed

> Location: Process → Speed → Travel speed

---

# Travel

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `travel_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--travel-speed=1`.  
![travel-lines](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/speed/travel-lines.png?raw=true)

Travel speed is the speed at which the print head moves when not extruding filament.  
This speed is typically faster than the printing speed, as there is no need to carefully place material. However, setting the travel speed too high can lead to issues such as missed steps or ringing artifacts.
