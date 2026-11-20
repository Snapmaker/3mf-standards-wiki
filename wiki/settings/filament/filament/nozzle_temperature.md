# nozzle_temperature

> Location: Filament → Filament → Print temperature → Nozzle
> Also in this section: `nozzle_temperature_initial_layer` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `nozzle_temperature`.  
[Type](../../../general_settings/option_type.md#list-types): `Integer list`.  
[Default](../../../general_settings/option_type.md#default-value): `200`.  
[Unit](../../../general_settings/option_type.md#unit): `℃`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--nozzle-temperature=1`.  

> [!TIP]
> Check [Temperature calibration](../../../calibration/temp_calib.md) to find the optimal nozzle temperature for your filament.

One of the most critical settings for successful 3D printing is the nozzle temperature.  
The correct nozzle temperature ensures proper melting and extrusion of the filament, leading to good layer adhesion and overall print quality.  
You can set a higher temperature for the first layer to improve bed adhesion but be cautious with deformations as [elephant foot](../../process/quality/elefant_foot_compensation.md).

## Temperature Reference (U1 Presets)

The following table lists the values configured in the U1 filament presets shipped with this fork (`Generic @U1` and `Snapmaker @U1` families).  
Numbers in parentheses are the nozzle temperature ranges defined in the presets.  
Actual optimal temperatures still vary between filament brands — always follow the manufacturer's recommendations and run calibrations for best results.

| Material | Nozzle Temp (°C) | Bed Temp (°C) | Chamber Temp (°C) |
| --- | --- | --- | --- |
| PLA | 220 (190-240) | 65 | 0 |
| PETG | 245-255 (220-270) | 70-80 | 0 |
| ABS | 265-280 (240-280) | 90-100 | 60 (Snapmaker ABS) / 0 (Generic ABS) |
| ASA | 260-280 (240-280) | 90-100 | 0 |
| PA (Nylon) | 260 (240-280) | 100 | 60 |
| PA-CF | 290 (260-300) | 100 | 0 |
| PC | 280 (260-290) | 100 | 0 |
| PCTG | 255 (240-270) | 100 | 0 |
| TPU | 215-240 (200-250) | 35 | 0 |
| PVA / BVOH (support) | 240 (190-250) | 65-70 | 0 |

Where a preset sets a different first-layer temperature, the span covers both values — e.g. Snapmaker ABS prints the first layer at 280 °C and the remaining layers at 265 °C (see [nozzle_temperature_initial_layer](nozzle_temperature_initial_layer.md)).
