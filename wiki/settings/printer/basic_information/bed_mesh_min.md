# bed_mesh_min

> Location: Printer → Basic information → Adaptive bed mesh

---

## Bed mesh

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `bed_mesh_min`.  
[Type](../../../general_settings/option_type.md#point): `Point`.  
[Default](../../../general_settings/option_type.md#default-value): `-99999×-99999`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--bed-mesh-min=100,100`.  
This option sets the min and max point for the allowed bed mesh area. Due to the probe's XY offset, most printers are unable to probe the entire bed. To ensure the probe point does not go outside the bed area, the minimum and maximum points of the bed mesh should be set appropriately.  
OrcaSlicer ensures that adaptive_bed_mesh_min/adaptive_bed_mesh_max values do not exceed these min/max points. This information can usually be obtained from your printer manufacturer.  
The default setting is (-99999, -99999), which means there are no limits, thus allowing probing across the entire bed.
