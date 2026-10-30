# overhang_4_4_speed

> Location: Process → Speed → Overhang speed
> 本小节同时涵盖：`overhang_1_4_speed`、`overhang_2_4_speed`、`overhang_3_4_speed`（各另有独立文档）。

---

### Speed

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `overhang_1_4_speed`, `overhang_2_4_speed`, `overhang_3_4_speed`, `overhang_4_4_speed`.  
[Type](../../general_settings/option_type.md#list-types): `Float or Percentage list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--overhang-1-4-speed=20%` (same pattern for the other variables above).  
This is the speed for various overhang degrees. Overhang degrees are expressed as a percentage of [line width](../../process/quality/quality_settings_line_width.md).  
If expressed as a percentage, the speed is calculated from the [outer wall speed](../../process/speed/speed_settings_other_layers_speed.md#outer-wall) for outer walls and from the [inner wall speed](../../process/speed/speed_settings_other_layers_speed.md#inner-wall) for inner walls.

> [!NOTE]
> 0 speed means no slowing down for the overhang degree range and wall speed is used.
