# first_layer_travel_jerk

> Location: Process → Speed → Jerk(XY)

---

### Initial layer travel

> [!WARNING] fork 未实现
> `initial_layer_travel_jerk` 为上游 OrcaSlicer 参数，fork 源码未收录，以下内容保留供参考。

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `initial_layer_travel_jerk`.  
[Type](../../../general_settings/option_type.md#list-types): `Float or Percentage list`.  
[Default](../../../general_settings/option_type.md#default-value): —.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--initial-layer-travel-jerk=20%`.  
Jerk for initial layer travel.
Using a lower value can improve build plate adhesion. If the value is expressed as a percentage (e.g. 50%), it will be calculated based on the [Travel Jerk](#travel).
