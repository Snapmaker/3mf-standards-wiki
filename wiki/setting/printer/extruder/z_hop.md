# z_hop

> Location: Printer → Extruder N → Z-Hop

---

## Z-hop height

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `z_hop[extruder_idx]`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `0.4`.  
[Range](../../../general_settings/option_type.md#range): `0–5` mm.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--z-hop=1`.  
Whenever there is a retraction, the nozzle is lifted a little to create clearance between the nozzle and the print. This prevents the nozzle from hitting the print when traveling more. Using spiral lines to lift z can prevent stringing.
