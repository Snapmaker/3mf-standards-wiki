# overhang_fan_speed

> 所在界面：耗材设置 → Cooling → Part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Overhangs and external bridges fan speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：需先启用 enable_overhang_bridge_fan 后显示

---

### Overhangs and external bridges fan speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `overhang_fan_speed`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--overhang-fan-speed=1`.  
Use this part cooling fan speed when printing bridges or overhang walls with an overhang threshold that exceeds the value set in the 'Overhangs cooling threshold' parameter above. Increasing the cooling specifically for overhangs and bridges can improve the overall print quality of these features.

Please note, this fan speed is clamped on the lower end by the minimum fan speed threshold set above. It is also adjusted upwards up to the maximum fan speed threshold when the minimum layer time threshold is not met.
