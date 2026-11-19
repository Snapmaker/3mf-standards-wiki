# fan_max_speed

> Location: Filament → Cooling → Part cooling fan
> 本小节同时涵盖：`fan_min_speed`、`fan_cooling_layer_time`、`slow_down_layer_time`（各另有独立文档）。

---

## Material Part Cooling Fan

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `fan_max_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `100`.  
[Range](../../../general_settings/option_type.md#range): `0–100` %.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--fan-max-speed=1`.  
These settings control the behavior of the part cooling fan during printing. Proper configuration of these parameters can significantly enhance print quality by optimizing cooling for different features and layer times.
