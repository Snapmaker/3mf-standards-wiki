# flush_into_infill

> 所在界面：工艺设置 → Multimaterial → Flush options
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_flush_options.md` 的「Flush into objects' infill」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Flush into objects' infill

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `flush_into_infill`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--flush-into-infill=1`.  
Purging after a filament change will be done inside the objects' infill. This may lower the amount of waste and decrease the print time. If the walls are printed with transparent filament, the mixed color infill will be visible. It will not take effect unless the prime tower is enabled. With a Type 2 [wipe tower](printer_multimaterial_wipe_tower), purging into objects is only used on single extruder multi-material printers with [Purge in prime tower](printer_multimaterial_wipe_tower#purge-in-prime-tower) enabled.
