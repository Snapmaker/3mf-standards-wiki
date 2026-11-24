# filament_max_volumetric_speed

> Location: Filament → Filament → Volumetric speed limitation → Max volumetric speed

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_max_volumetric_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `2`.  
[Unit](../../../general_settings/option_type.md#unit): `mm³/s`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-max-volumetric-speed=1`.  

Each material profile includes a **maximum volumetric speed** setting, which limits your print speed to prevent issues like nozzle clogs, under-extrusion, or poor layer adhesion.

> [!TIP]
> Calibrating the maximum volumetric speed for each filament you use is highly recommended. Refer to the Max Volumetric Speed (FlowRate) Calibration guide for detailed instructions on how to perform this calibration.

This setting is the volume of filament that can be melted and extruded per second. Printing speed is limited by max volumetric speed, in case of too high and unreasonable speed setting. This value cannot be zero.  
It is also the reference for volumetric speeds expressed as a percentage.
