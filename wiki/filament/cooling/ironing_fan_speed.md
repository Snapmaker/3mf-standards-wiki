# ironing_fan_speed

> Location: Filament → Cooling → Part cooling fan

---

### Ironing fan speed

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `ironing_fan_speed`.  
[Type](../../general_settings/option_type.md#list-types): `Integer list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--ironing-fan-speed=1`.  
This part cooling fan speed is applied when ironing. Setting this parameter to a lower than regular speed reduces possible nozzle clogging due to the low volumetric flow rate, making the interface smoother.  
Set to -1 to disable it.
