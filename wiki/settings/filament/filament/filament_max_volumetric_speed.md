# filament_max_volumetric_speed

> Location: Filament → Filament → Volumetric speed limitation

---

## Max volumetric speed

> [!WARNING] fork 未实现
> Volumetric speeds（体积速度按百分比表达）为上游特性，fork 未收录 `enable_volumetric_speeds` 等键；正文末句为上游原文保留。

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_max_volumetric_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `2`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` mm³/s.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-max-volumetric-speed=1`.  
Each material profile includes a **maximum volumetric speed** setting, which limits your [print speed](https://github.com/OrcaSlicer/OrcaSlicer/wiki/speed_settings_other_layers_speed) to prevent issues like nozzle clogs, under-extrusion, or poor layer adhesion.

> [!TIP]
> Calibrating the maximum volumetric speed for each filament you use is highly recommended. Refer to the [Max Volumetric Speed (FlowRate) Calibration](../../../calibration/volumetric_speed_calib.md) guide for detailed instructions on how to perform this calibration.

This setting is the volume of filament that can be melted and extruded per second. Printing speed is limited by max volumetric speed, in case of too high and unreasonable speed setting. This value cannot be zero.  
It is also the reference for [volumetric speeds](https://github.com/OrcaSlicer/OrcaSlicer/wiki/speed_settings_other_layers_speed#volumetric-speeds) expressed as a percentage.
