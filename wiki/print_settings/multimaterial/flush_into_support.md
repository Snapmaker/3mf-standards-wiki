# flush_into_support

> 所在界面：工艺设置 → Multimaterial → Flush options
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_flush_options.md` 的「Flush into objects' support」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Flush into objects' support

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `flush_into_support`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--flush-into-support=1`.  
Purging after a filament change will be done inside the objects' support. This may lower the amount of waste and decrease the print time. It will not take effect unless the prime tower is enabled. With a Type 2 [wipe tower](printer_multimaterial_wipe_tower), purging into objects is only used on single extruder multi-material printers with [Purge in prime tower](printer_multimaterial_wipe_tower#purge-in-prime-tower) enabled.
