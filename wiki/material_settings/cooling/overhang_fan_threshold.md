# overhang_fan_threshold

> 所在界面：耗材设置 → Cooling → Part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Overhang cooling activation threshold」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：需先启用 enable_overhang_bridge_fan 后显示

---

### Overhang cooling activation threshold

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `overhang_fan_threshold`.  
[Type](option_type#list-types): `Choice list`.  
[Options](option_type#choice): `0%, 10%, 25%, 50%, 75%, 95%`.  
[CLI Example](cli_mode#setting-overrides): `--overhang-fan-threshold=0%`.  
When the overhang exceeds this specified threshold, force the cooling fan to run at the 'Overhang Fan Speed' set below. This threshold is expressed as a percentage, indicating the portion of each line's width that is unsupported by the layer beneath it. Setting this value to 0% forces the cooling fan to run for all outer walls, regardless of the overhang degree.
