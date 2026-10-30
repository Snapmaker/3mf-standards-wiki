# full_fan_speed_layer

> Location: Filament → Cooling → Cooling for specific layer

---

### Full fan speed at layer

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `full_fan_speed_layer`.  
[Type](../../general_settings/option_type.md#list-types): `Integer list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--full-fan-speed-layer=1`.  
Fan speed is increased linearly from 0% starting at the layer specified by [close_fan_the_first_x_layers](#no-cooling-for-the-first) up to the maximum part-cooling speed at this specified layer.  
If this layer is less than or equal to [close_fan_the_first_x_layers](#no-cooling-for-the-first), it is ignored and the fan will reach the maximum allowed speed on the layer immediately after [close_fan_the_first_x_layers](#no-cooling-for-the-first) (i.e. at layer [close_fan_the_first_x_layers](#no-cooling-for-the-first) + 1).  
Set this option to `0` to disable the automatic ramp.
