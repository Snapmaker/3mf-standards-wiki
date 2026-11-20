# slow_down_layer_time

> Location: Filament → Cooling → Part cooling fan
> Also in this section: `fan_min_speed`, `fan_cooling_layer_time`, `fan_max_speed` (each documented on its own page).

---

## Material Part Cooling Fan

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `slow_down_layer_time`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `5.0`.  
[Unit](../../../general_settings/option_type.md#unit): `s`.  
[Range](../../../general_settings/option_type.md#range): `0–1000`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--slow-down-layer-time=1`.  

These settings control the behavior of the part cooling fan during printing. Proper configuration of these parameters can significantly enhance print quality by optimizing cooling for different features and layer times.
