# prime_volume

> 所在界面：工艺设置 → Multimaterial → Prime tower
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_prime_tower.md` 的「Prime volume」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Prime volume

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `prime_volume`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--prime-volume=1`.  
Volume of material, in mm³, printed on the prime tower after each tool change to prime the new extruder. Default is 45 mm³.

Unless the printer is a single extruder multi-material printer with [Purge in prime tower](printer_multimaterial_wipe_tower#purge-in-prime-tower) enabled, the Type 2 tower purges this fixed volume at each tool change instead of the flushing volumes. On such printers the tower purges the flushing volumes and this option is hidden. The Type 1 tower takes the prime volume from each filament profile and uses this value only as a fallback.
