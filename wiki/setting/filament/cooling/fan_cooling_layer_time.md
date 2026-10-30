# fan_cooling_layer_time

> Location: Filament → Cooling → Part cooling fan
> 本小节同时涵盖：`fan_min_speed`、`fan_max_speed`、`slow_down_layer_time`（各另有独立文档）。

---

## Material Part Cooling Fan

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `fan_min_speed`, `fan_cooling_layer_time`, `fan_max_speed`, `slow_down_layer_time`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--fan-min-speed=1` (same pattern for the other variables above).  
These settings control the behavior of the part cooling fan during printing. Proper configuration of these parameters can significantly enhance print quality by optimizing cooling for different features and layer times.
