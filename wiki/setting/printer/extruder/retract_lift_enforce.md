# retract_lift_enforce

> Location: Printer → Extruder N → Z-Hop

---

## On surfaces

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `retract_lift_enforce[extruder_idx]`.  
[Type](../../../general_settings/option_type.md#list-types): `Choice list`.  
[Options](../../../general_settings/option_type.md#choice): `All Surfaces, Top Only, Bottom Only, Top and Bottom`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--retract-lift-enforce="All Surfaces"`.  
Enforce Z-Hop behavior. This setting is impacted by the above settings (Only lift Z above/below).
