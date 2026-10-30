# retract_lift_below

> Location: Printer → Extruder N → Z-Hop

---

## Only lift Z below

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `retract_lift_below[extruder_idx]`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--retract-lift-below=1`.  
If you set this to a positive value, Z lift will only take place below the specified absolute Z.
