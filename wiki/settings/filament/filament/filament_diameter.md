# filament_diameter

> Location: Filament → Filament → Basic information
> Visibility (preliminary, pending review): Shown only on non-pellet (filament) machines

---

## Diameter

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_diameter`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `1.75`.  
[Unit](../../../general_settings/option_type.md#unit): `mm`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-diameter=1`.  

Filament diameter is used to calculate extrusion variables in G-code, so it is important that this is accurate and precise.
