# pellet_flow_coefficient

> Location: Filament → Filament → Flow ratio and Pressure Advance → Pellet flow coefficient
> Status: placeholder — to be completed.
> Visibility (preliminary, pending review): Shown only on pellet machines

---

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `pellet_flow_coefficient`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `0.4157`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--pellet-flow-coefficient=1`.  

Pellet flow coefficient is empirically derived and allows for volume calculation for pellet printers.\n\nInternally it is converted to filament_diameter. All other volume calculations remain the same.\n\nfilament_diameter = sqrt( (4 * pellet_flow_coefficient) / PI )
