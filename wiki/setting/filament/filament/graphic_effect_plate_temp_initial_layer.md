# graphic_effect_plate_temp_initial_layer

> Location: Filament → Filament → Bed temperature
> 显隐条件（初步梳理，待校对）：仅当打印机启用对应床型时显示
> 本小节同时涵盖：`initial_layer_jerk`（各另有独立文档）。

---

### Initial layer

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `initial_layer_jerk`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--initial-layer-jerk=1`.  
Jerk for initial layer printing. This is usually set to a lower value than top surface to improve adhesion.
