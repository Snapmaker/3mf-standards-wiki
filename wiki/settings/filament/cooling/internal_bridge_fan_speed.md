# internal_bridge_fan_speed

> Location: Filament → Cooling → Part cooling fan → Internal bridges fan speed
> Visibility (preliminary, pending review): Shown after enable_overhang_bridge_fan is enabled

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `internal_bridge_fan_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Integer list`.  
[Default](../../../general_settings/option_type.md#default-value): `-1`.  
[Unit](../../../general_settings/option_type.md#unit): `%`.  
[Range](../../../general_settings/option_type.md#range): `-1–100`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--internal-bridge-fan-speed=1`.  

The part cooling fan speed used for all internal bridges. Set to -1 to use the overhang fan speed settings instead.

Reducing the internal bridges fan speed, compared to your regular fan speed, can help reduce part warping due to excessive cooling applied over a large surface for a prolonged period of time.
