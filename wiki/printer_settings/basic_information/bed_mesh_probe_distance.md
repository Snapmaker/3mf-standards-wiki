# bed_mesh_probe_distance

> 所在界面：打印机设置 → Basic information → Adaptive bed mesh
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_adaptive_bed_mesh.md` 的「Probe point distance」小节（2026-10-28），英文原文，待本地化校对。

---

## Probe point distance

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `bed_mesh_probe_distance`.  
[Type](option_type#point): `Point`.  
[CLI Example](cli_mode#setting-overrides): `--bed-mesh-probe-distance=100,100`.  
This option sets the preferred distance between probe points (grid size) for the X and Y directions, with the default being 50mm for both X and Y.
