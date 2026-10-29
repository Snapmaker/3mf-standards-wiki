# ironing_fan_speed

> 所在界面：耗材设置 → Cooling → Part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Ironing fan speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Ironing fan speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `ironing_fan_speed`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--ironing-fan-speed=1`.  
This part cooling fan speed is applied when ironing. Setting this parameter to a lower than regular speed reduces possible nozzle clogging due to the low volumetric flow rate, making the interface smoother.  
Set to -1 to disable it.
