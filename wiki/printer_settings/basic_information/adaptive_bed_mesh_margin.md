# adaptive_bed_mesh_margin

> 所在界面：打印机设置 → Basic information → Adaptive bed mesh
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_adaptive_bed_mesh.md` 的「Mesh margin」小节（2026-10-28），英文原文，待本地化校对。

---

## Mesh margin

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `adaptive_bed_mesh_margin`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--adaptive-bed-mesh-margin=1`.  
This option determines the additional distance by which the adaptive bed mesh area should be expanded in the XY directions.

> [!NOTE]
> Klipper users: OrcaSlicer will adjust adaptive bed mesh area according to the margin. It is recommended to set the margin to 0 in Klipper config or pass 0 when calling BED_MESH_CALIBRATE command(please refer to the example below).
