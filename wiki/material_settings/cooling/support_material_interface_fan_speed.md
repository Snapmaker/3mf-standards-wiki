# support_material_interface_fan_speed

> 所在界面：耗材设置 → Cooling → Part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Support interface fan speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Support interface fan speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `support_material_interface_fan_speed`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--support-material-interface-fan-speed=1`.  
This part cooling fan speed is applied when printing support interfaces. Setting this parameter to a higher than regular speed reduces the layer binding strength between supports and the supported part, making them easier to separate.  
Set to -1 to disable it.  
This setting is overridden by disable_fan_first_layers.
