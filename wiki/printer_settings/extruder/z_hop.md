# z_hop

> 所在界面：打印机设置 → Extruder N → Z-Hop
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_z_hop.md` 的「Z-hop height」小节（2026-10-28），英文原文，待本地化校对。

---

## Z-hop height

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `z_hop[extruder_idx]`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--z-hop=1`.  
Whenever there is a retraction, the nozzle is lifted a little to create clearance between the nozzle and the print. This prevents the nozzle from hitting the print when traveling more. Using spiral lines to lift z can prevent stringing.
