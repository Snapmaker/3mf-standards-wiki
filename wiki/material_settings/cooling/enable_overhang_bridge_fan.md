# enable_overhang_bridge_fan

> 所在界面：耗材设置 → Cooling → Part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Force cooling for overhangs and bridges」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Force cooling for overhangs and bridges

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `enable_overhang_bridge_fan`.  
[Type](option_type#list-types): `Boolean list`.  
[CLI Example](cli_mode#setting-overrides): `--enable-overhang-bridge-fan=1`.  
Enable this option to allow adjustment of the part cooling fan speed for specifically for overhangs, internal and external bridges. Setting the fan speed specifically for these features can improve overall print quality and reduce warping.
