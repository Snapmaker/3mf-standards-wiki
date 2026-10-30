# retraction_minimum_travel

> Location: Printer → Extruder N → Retraction

---

## Travel distance threshold

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `retraction_minimum_travel[extruder_idx]`.  
[Type](../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--retraction-minimum-travel=1`.  
Only trigger retraction when the travel distance is longer than this threshold.
