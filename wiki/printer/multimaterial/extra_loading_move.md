# extra_loading_move

> Location: Printer → Multimaterial → Single extruder multi-material parameters

---

## Extra loading distance

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `extra_loading_move`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--extra-loading-move=1`.  
 When set to zero, the distance the filament is moved from parking position during load is exactly the same as it was moved back during unload. When positive, it is loaded further, if negative, the loading move is shorter than unloading.
