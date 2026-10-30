# nozzle_temperature_initial_layer

> Location: Filament → Filament → Print temperature
> 本小节同时涵盖：`nozzle_temperature`（各另有独立文档）。

---

## Nozzle

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `nozzle_temperature_initial_layer`, `nozzle_temperature`.  
[Type](../../general_settings/option_type.md#list-types): `Integer list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--nozzle-temperature-initial-layer=1` (same pattern for the other variables above).  
One of the most critical settings for successful 3D printing is the nozzle temperature.  
The correct nozzle temperature ensures proper melting and extrusion of the filament, leading to good layer adhesion and overall print quality.  
You can set a higher temperature for the first layer to improve bed adhesion but be cautious with deformations as [elephant foot](../../process/quality/quality_settings_precision.md#elephant-foot-compensation).
