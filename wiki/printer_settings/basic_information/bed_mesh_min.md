# bed_mesh_min

> 所在界面：打印机设置 → Basic information → Adaptive bed mesh
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_adaptive_bed_mesh.md` 的「Bed mesh」小节（2026-10-28），英文原文，待本地化校对。

---

## Bed mesh

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `bed_mesh_min`, `bed_mesh_max`.  
[Type](option_type#point): `Point`.  
[CLI Example](cli_mode#setting-overrides): `--bed-mesh-min=100,100` (same pattern for the other variables above).  
This option sets the min and max point for the allowed bed mesh area. Due to the probe's XY offset, most printers are unable to probe the entire bed. To ensure the probe point does not go outside the bed area, the minimum and maximum points of the bed mesh should be set appropriately.  
OrcaSlicer ensures that adaptive_bed_mesh_min/adaptive_bed_mesh_max values do not exceed these min/max points. This information can usually be obtained from your printer manufacturer.  
The default setting is (-99999, -99999), which means there are no limits, thus allowing probing across the entire bed.
