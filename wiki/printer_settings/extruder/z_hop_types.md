# z_hop_types

> 所在界面：打印机设置 → Extruder N → Z-Hop
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_z_hop.md` 的「Z-hop type」小节（2026-10-28），英文原文，待本地化校对。

---

## Z-hop type

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `z_hop_types[extruder_idx]`.  
[Type](option_type#list-types): `Choice list`.  
[Options](option_type#choice): `Auto Lift, Normal Lift, Slope Lift, Spiral Lift`.  
[CLI Example](cli_mode#setting-overrides): `--z-hop-types="Auto Lift"`.  
- Auto: Selects automatically between Spiral based on whether the travel move crosses over overhang areas
- Normal Lift: The nozzle is lifted vertically during retraction and lowered back down before resuming printing.
- Slope: The nozzle moves diagonally (at an angle) during retraction, creating a sloped path.
- Spiral: The nozzle moves in a spiral pattern while lifting, which can help reduce stringing and improve print quality.
