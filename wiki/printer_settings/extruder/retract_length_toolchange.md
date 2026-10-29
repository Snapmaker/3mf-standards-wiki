# retract_length_toolchange

> 所在界面：打印机设置 → Extruder N → Retraction when switching material
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_retraction.md` 的「Retraction When Switching Materials」小节（2026-10-28），英文原文，待本地化校对。

---

## Retraction When Switching Materials

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `retract_length_toolchange[extruder_idx]`, `retract_restart_extra_toolchange[extruder_idx]`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--retract-length-toolchange=1` (same pattern for the other variables above).  
Retraction settings specifically for material changes during tool changes in multi-material prints.

### Long retraction when cut (beta)

[Mode](option_mode): `Developer`.  
[Variables](built_in_placeholders_variables): `long_retractions_when_cut[extruder_idx]`, `retraction_distances_when_cut[extruder_idx]`.  
[Type](option_type): `long_retractions_when_cut` (Boolean list), `retraction_distances_when_cut` (Float list).  
[CLI Example](cli_mode#setting-overrides): `--long-retractions-when-cut=1` (`long_retractions_when_cut` shown; other variables above follow their own type).  
Experimental feature: Retracting and cutting off the filament at a longer distance during changes to minimize purge. While this reduces flush significantly, it may also raise the risk of nozzle clogs or other printing problems.
