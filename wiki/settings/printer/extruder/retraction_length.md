# retraction_length

> Location: Printer → Extruder N → Retraction

---

## Length

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `retraction_length[extruder_idx]`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `0.8`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--retraction-length=1`.  
When retraction is triggered before changing tool, filament is pulled back by the specified amount (the length is measured on raw filament, before it enters the extruder).
