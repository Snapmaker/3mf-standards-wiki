# travel_slope

> 所在界面：打印机设置 → Extruder N → Z-Hop
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_z_hop.md` 的「Traveling angle」小节（2026-10-28），英文原文，待本地化校对。

---

## Traveling angle

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `travel_slope[extruder_idx]`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--travel-slope=1`.  
Traveling angle for Slope and Spiral Z-hop type. Setting it to 90° results in Normal Lift.
