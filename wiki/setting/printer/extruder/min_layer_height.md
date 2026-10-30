# min_layer_height

> Location: Printer → Extruder N → Layer height limits

---

## Extruder Layer Height Limits

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `extruder_printable_height[extruder_idx]`, `min_layer_height[extruder_idx]`, `max_layer_height[extruder_idx]`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--extruder-printable-height=1` (same pattern for the other variables above).  
Min and max layer height limits for the extruder. These settings are used when adaptive layer height is enabled.
