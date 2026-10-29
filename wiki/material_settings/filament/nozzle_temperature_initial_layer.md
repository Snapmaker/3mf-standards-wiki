# nozzle_temperature_initial_layer

> 所在界面：耗材设置 → Filament → Print temperature
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_temperatures.md` 的「Nozzle」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`nozzle_temperature`（各另有独立文档）。

---

## Nozzle

[Mode](option_mode): `Simple`.  
[Variables](built_in_placeholders_variables): `nozzle_temperature_initial_layer`, `nozzle_temperature`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--nozzle-temperature-initial-layer=1` (same pattern for the other variables above).  
One of the most critical settings for successful 3D printing is the nozzle temperature.  
The correct nozzle temperature ensures proper melting and extrusion of the filament, leading to good layer adhesion and overall print quality.  
You can set a higher temperature for the first layer to improve bed adhesion but be cautious with deformations as [elephant foot](quality_settings_precision#elephant-foot-compensation).
