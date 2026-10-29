# retract_lift_above

> 所在界面：打印机设置 → Extruder N → Z-Hop
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_z_hop.md` 的「Only lift Z above」小节（2026-10-28），英文原文，待本地化校对。

---

## Only lift Z above

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `retract_lift_above[extruder_idx]`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--retract-lift-above=1`.  
If you set this to a positive value, Z lift will only take place above the specified absolute Z.
