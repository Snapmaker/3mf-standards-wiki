# overhang_fan_threshold

> Location: Filament → Cooling → Part cooling fan
> 显隐条件（初步梳理，待校对）：需先启用 enable_overhang_bridge_fan 后显示

---

### Overhang cooling activation threshold

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `overhang_fan_threshold`.  
[Type](../../general_settings/option_type.md#list-types): `Choice list`.  
[Options](../../general_settings/option_type.md#choice): `0%, 10%, 25%, 50%, 75%, 95%`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--overhang-fan-threshold=0%`.  
When the overhang exceeds this specified threshold, force the cooling fan to run at the 'Overhang Fan Speed' set below. This threshold is expressed as a percentage, indicating the portion of each line's width that is unsupported by the layer beneath it. Setting this value to 0% forces the cooling fan to run for all outer walls, regardless of the overhang degree.
