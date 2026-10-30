# internal_bridge_fan_speed

> Location: Filament → Cooling → Part cooling fan
> 显隐条件（初步梳理，待校对）：需先启用 enable_overhang_bridge_fan 后显示

---

### Internal bridges fan speed

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `internal_bridge_fan_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Integer list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--internal-bridge-fan-speed=1`.  
The part cooling fan speed used for all internal bridges. Set to -1 to use the overhang fan speed settings instead.

Reducing the internal bridges fan speed, compared to your regular fan speed, can help reduce part warping due to excessive cooling applied over a large surface for a prolonged period of time.
