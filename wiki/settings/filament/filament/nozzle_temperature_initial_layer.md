# nozzle_temperature_initial_layer

> Location: Filament → Filament → Print temperature
> 本小节同时涵盖：`nozzle_temperature`（各另有独立文档）。
> gcode 嵌入名：`first_layer_temperature`（gcode 注释段写旧名，值取本键；自定义 g-code 占位符新旧两名并存）。

---

## Nozzle

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `nozzle_temperature_initial_layer`.  
[Type](../../../general_settings/option_type.md#list-types): `Integer list`.  
[Default](../../../general_settings/option_type.md#default-value): `200`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` ℃.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--nozzle-temperature-initial-layer=1`.  
One of the most critical settings for successful 3D printing is the nozzle temperature.  
The correct nozzle temperature ensures proper melting and extrusion of the filament, leading to good layer adhesion and overall print quality.  
You can set a higher temperature for the first layer to improve bed adhesion but be cautious with deformations as [elephant foot](../../process/quality/elefant_foot_compensation.md).
