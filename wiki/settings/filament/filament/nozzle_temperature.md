# nozzle_temperature

> Location: Filament → Filament → Print temperature
> 本小节同时涵盖：`nozzle_temperature_initial_layer`（各另有独立文档）。

---

## Nozzle

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `nozzle_temperature_initial_layer`, `nozzle_temperature`.  
[Type](../../../general_settings/option_type.md#list-types): `Integer list`.  
[Defaults](../../../general_settings/option_type.md#default-value): `nozzle_temperature_initial_layer` (200), `nozzle_temperature` (200).  
[Ranges](../../../general_settings/option_type.md#range): `nozzle_temperature_initial_layer` (`≥ 0` ℃), `nozzle_temperature` (`≥ 0` ℃).  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--nozzle-temperature-initial-layer=1` (same pattern for the other variables above).  

> [!TIP]
> Check [Temperature calibration](https://github.com/OrcaSlicer/OrcaSlicer/wiki/temp_calib) to find the optimal nozzle temperature for your filament.

One of the most critical settings for successful 3D printing is the nozzle temperature.  
The correct nozzle temperature ensures proper melting and extrusion of the filament, leading to good layer adhesion and overall print quality.  
You can set a higher temperature for the first layer to improve bed adhesion but be cautious with deformations as [elephant foot](../../process/quality/elefant_foot_compensation.md).

## Standard Temperature Ranges

The following table lists the standard temperature ranges for common 3D printing materials.  
Actual optimal temperatures may vary based on specific filament brands and printer models.  
Always refer to the filament manufacturer's recommendations and calibrations for best results.

| Material | Nozzle Temp (°C) | Bed Temp (°C) | Chamber Temp (°C) |
| --- | --- | --- | --- |
| PLA | 180-220 | 50-60 | Ambient |
| ABS | 230-250 | 90-100 | 50-70 |
| ASA | 240-260 | 90-100 | 50-70 |
| Nylon 6 | 230-260 | 90-110 | 70-100 |
| Nylon 12 | 225-260 | 90-110 | 70-100 |
| TPU | 220-245 | 40-60 | Ambient |
| PC | 270-310 | 100-120 | 80-100 |
| PC-ABS | 260-280 | 95-110 | 60-80 |
| HIPS | 220-250 | 90-110 | 50-70 |
| PP | 220-270 | 80-105 | 40-70 |
| Acetal (POM) | 210-240 | 100-130 | 70-100 |
