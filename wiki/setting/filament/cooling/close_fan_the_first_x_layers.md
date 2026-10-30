# close_fan_the_first_x_layers

> Location: Filament → Cooling → Cooling for specific layer

---

### No cooling for the first

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `close_fan_the_first_x_layers`.  
[Type](../../../general_settings/option_type.md#list-types): `Integer list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--close-fan-the-first-x-layers=1`.  
Number of initial layers during which part-cooling fans are disabled.
Disabling the fan for the first few layers improves build-plate adhesion and reduces early-layer warping.
