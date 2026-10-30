# support_material_interface_fan_speed

> Location: Filament → Cooling → Part cooling fan

---

### Support interface fan speed

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `support_material_interface_fan_speed`.  
[Type](../../general_settings/option_type.md#list-types): `Integer list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--support-material-interface-fan-speed=1`.  
This part cooling fan speed is applied when printing support interfaces. Setting this parameter to a higher than regular speed reduces the layer binding strength between supports and the supported part, making them easier to separate.  
Set to -1 to disable it.  
This setting is overridden by disable_fan_first_layers.
