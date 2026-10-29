# retract_lift_enforce

> 所在界面：打印机设置 → Extruder N → Z-Hop
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_z_hop.md` 的「On surfaces」小节（2026-10-28），英文原文，待本地化校对。

---

## On surfaces

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `retract_lift_enforce[extruder_idx]`.  
[Type](option_type#list-types): `Choice list`.  
[Options](option_type#choice): `All Surfaces, Top Only, Bottom Only, Top and Bottom`.  
[CLI Example](cli_mode#setting-overrides): `--retract-lift-enforce="All Surfaces"`.  
Enforce Z-Hop behavior. This setting is impacted by the above settings (Only lift Z above/below).
