# adaptive_pressure_advance_bridges

> Location: Filament → Filament → Flow ratio and Pressure Advance

---

#### Pressure advance for bridges

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `adaptive_pressure_advance_bridges`.  
[Type](../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--adaptive-pressure-advance-bridges=1`.  
Pressure advance value for bridges. Set to 0 to disable.  
A lower PA value when printing bridges helps reduce the appearance of slight under extrusion immediately after bridges.  
This is caused by the pressure drop in the nozzle when printing in the air and a lower PA helps counteract this.
