# filament_tower_ironing_area

> 所在界面：耗材设置 → Filament → Basic information
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/multimaterial/material_multimaterial.md` 的「Multimaterial Wipe Tower Parameters」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`filament_tower_interface_pre_extrusion_dist`、`filament_tower_interface_pre_extrusion_length`、`filament_tower_interface_print_temp`、`filament_minimal_purge_on_wipe_tower`（各另有独立文档）。

---

## Multimaterial Wipe Tower Parameters

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `filament_minimal_purge_on_wipe_tower`, `filament_tower_interface_pre_extrusion_dist`, `filament_tower_interface_pre_extrusion_length`, `filament_tower_ironing_area`, `filament_tower_interface_purge_volume`, `filament_tower_interface_print_temp`.  
[Type](option_type): `filament_minimal_purge_on_wipe_tower` (Float list), `filament_tower_interface_pre_extrusion_dist` (Float list), `filament_tower_interface_pre_extrusion_length` (Float list), `filament_tower_ironing_area` (Float list), `filament_tower_interface_purge_volume` (Float list), `filament_tower_interface_print_temp` (Integer list).  
[CLI Example](cli_mode#setting-overrides): `--filament-minimal-purge-on-wipe-tower=1` (`filament_minimal_purge_on_wipe_tower` shown; other variables above follow their own type).  
Wipe towers are sacrificial structures printed alongside the main object to purge excess material from the nozzle after a tool change in multimaterial printing. This ensures that the next extrusion uses the correct filament color or type without contamination from the previous material.
