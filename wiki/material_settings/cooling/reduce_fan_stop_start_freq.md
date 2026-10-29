# reduce_fan_stop_start_freq

> 所在界面：耗材设置 → Cooling → Part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Keep fan always on」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Keep fan always on

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `reduce_fan_stop_start_freq`.  
[Type](option_type#list-types): `Boolean list`.  
[CLI Example](cli_mode#setting-overrides): `--reduce-fan-stop-start-freq=1`.  
Enabling this setting means that part cooling fan will never stop entirely and will instead run at least at minimum speed to reduce the frequency of starting and stopping.
