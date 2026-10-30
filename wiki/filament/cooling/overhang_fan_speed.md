# overhang_fan_speed

> Location: Filament → Cooling → Part cooling fan
> 显隐条件（初步梳理，待校对）：需先启用 enable_overhang_bridge_fan 后显示

---

### Overhangs and external bridges fan speed

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `overhang_fan_speed`.  
[Type](../../general_settings/option_type.md#list-types): `Integer list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--overhang-fan-speed=1`.  
Use this part cooling fan speed when printing bridges or overhang walls with an overhang threshold that exceeds the value set in the 'Overhangs cooling threshold' parameter above. Increasing the cooling specifically for overhangs and bridges can improve the overall print quality of these features.

Please note, this fan speed is clamped on the lower end by the minimum fan speed threshold set above. It is also adjusted upwards up to the maximum fan speed threshold when the minimum layer time threshold is not met.
