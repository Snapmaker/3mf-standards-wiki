# z_hop_types

> Location: Printer → Extruder N → Z-Hop

---

## Z-hop type

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `z_hop_types[extruder_idx]`.  
[Type](../../general_settings/option_type.md#list-types): `Choice list`.  
[Options](../../general_settings/option_type.md#choice): `Auto Lift, Normal Lift, Slope Lift, Spiral Lift`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--z-hop-types="Auto Lift"`.  
- Auto: Selects automatically between Spiral based on whether the travel move crosses over overhang areas
- Normal Lift: The nozzle is lifted vertically during retraction and lowered back down before resuming printing.
- Slope: The nozzle moves diagonally (at an angle) during retraction, creating a sloped path.
- Spiral: The nozzle moves in a spiral pattern while lifting, which can help reduce stringing and improve print quality.
