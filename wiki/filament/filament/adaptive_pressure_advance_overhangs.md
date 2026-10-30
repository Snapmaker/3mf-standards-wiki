# adaptive_pressure_advance_overhangs

> Location: Filament → Filament → Flow ratio and Pressure Advance

---

#### Enable adaptive pressure advance for overhangs (beta)

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `adaptive_pressure_advance_overhangs`.  
[Type](../../general_settings/option_type.md#list-types): `Boolean list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--adaptive-pressure-advance-overhangs=1`.  
Enable adaptive PA for overhangs as well as when flow changes within the same feature. This is an experimental option, as if the PA profile is not set accurately, it will cause uniformity issues on the external surfaces before and after overhangs.
