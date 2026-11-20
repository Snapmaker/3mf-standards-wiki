# long_retractions_when_cut

> Location: Printer → Extruder N → Retraction when switching material → Long retraction when cut (beta)
> Status: placeholder — code notes it is not yet shown in the UI; to be completed.

---

[Mode](../../../general_settings/option_mode.md): `Developer`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `long_retractions_when_cut`.  
[Type](../../../general_settings/option_type.md#list-types): `Boolean list`.  
[Default](../../../general_settings/option_type.md#default-value): `false`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--long-retractions-when-cut=1`.  

Experimental feature: Retracting and cutting off the filament at a longer distance during changes to minimize purge. While this reduces flush significantly, it may also raise the risk of nozzle clogs or other printing problems.
