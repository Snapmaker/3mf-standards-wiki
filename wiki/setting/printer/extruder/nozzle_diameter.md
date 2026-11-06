# nozzle_diameter

> Location: Printer → Extruder N → Size

---

## Nozzle diameter

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `nozzle_diameter[extruder_idx]`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `0.4`.  
[Range](../../../general_settings/option_type.md#range): `≤ 100` mm.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--nozzle-diameter=1`.  
The diameter of the nozzle for each extruder.  

> [!TIP]
> You can use different nozzle diameters for each extruder to achieve different print qualities and speeds.  
> Follow the [Mixed Nozzle Sizes](../../../guides/mixed_nozzle_sizes.md) guide for more information on how to use this feature.
