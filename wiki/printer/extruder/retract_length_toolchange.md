# retract_length_toolchange

> Location: Printer → Extruder N → Retraction when switching material

---

## Retraction When Switching Materials

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `retract_length_toolchange[extruder_idx]`, `retract_restart_extra_toolchange[extruder_idx]`.  
[Type](../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--retract-length-toolchange=1` (same pattern for the other variables above).  
Retraction settings specifically for material changes during tool changes in multi-material prints.

### Long retraction when cut (beta)

[Mode](../../general_settings/option_mode.md): `Developer`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `long_retractions_when_cut[extruder_idx]`, `retraction_distances_when_cut[extruder_idx]`.  
[Type](../../general_settings/option_type.md): `long_retractions_when_cut` (Boolean list), `retraction_distances_when_cut` (Float list).  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--long-retractions-when-cut=1` (`long_retractions_when_cut` shown; other variables above follow their own type).  
Experimental feature: Retracting and cutting off the filament at a longer distance during changes to minimize purge. While this reduces flush significantly, it may also raise the risk of nozzle clogs or other printing problems.
