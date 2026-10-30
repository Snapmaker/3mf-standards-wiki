# adaptive_bed_mesh_margin

> Location: Printer → Basic information → Adaptive bed mesh

---

## Mesh margin

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `adaptive_bed_mesh_margin`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--adaptive-bed-mesh-margin=1`.  
This option determines the additional distance by which the adaptive bed mesh area should be expanded in the XY directions.

> [!NOTE]
> Klipper users: OrcaSlicer will adjust adaptive bed mesh area according to the margin. It is recommended to set the margin to 0 in Klipper config or pass 0 when calling BED_MESH_CALIBRATE command(please refer to the example below).
