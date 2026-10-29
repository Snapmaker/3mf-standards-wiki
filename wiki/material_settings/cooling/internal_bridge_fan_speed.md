# internal_bridge_fan_speed

> 所在界面：耗材设置 → Cooling → Part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Internal bridges fan speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：需先启用 enable_overhang_bridge_fan 后显示

---

### Internal bridges fan speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `internal_bridge_fan_speed`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--internal-bridge-fan-speed=1`.  
The part cooling fan speed used for all internal bridges. Set to -1 to use the overhang fan speed settings instead.

Reducing the internal bridges fan speed, compared to your regular fan speed, can help reduce part warping due to excessive cooling applied over a large surface for a prolonged period of time.
