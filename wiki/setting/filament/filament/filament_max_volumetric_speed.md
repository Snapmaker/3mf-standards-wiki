# filament_max_volumetric_speed

> Location: Filament → Filament → Volumetric speed limitation

---

## Max volumetric speed

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_max_volumetric_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-max-volumetric-speed=1`.  
This setting is the volume of filament that can be melted and extruded per second. Printing speed is limited by max volumetric speed, in case of too high and unreasonable speed setting. This value cannot be zero.
