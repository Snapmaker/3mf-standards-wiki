# overhang_2_4_speed

> Location: Process → Speed → Overhang speed
> 本小节同时涵盖：`overhang_1_4_speed`、`overhang_3_4_speed`、`overhang_4_4_speed`（各另有独立文档）。

---

### Speed

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `overhang_2_4_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float or Percentage list`.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` mm/s or %.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--overhang-2-4-speed=1`.  
This is the speed for various overhang degrees. Overhang degrees are expressed as a percentage of [line width](../../process/quality/line_width.md).  
If expressed as a percentage, the speed is calculated from the [outer wall speed](../../process/speed/outer_wall_acceleration.md) for outer walls and from the [inner wall speed](../../process/speed/inner_wall_acceleration.md) for inner walls.

> [!NOTE]
> 0 speed means no slowing down for the overhang degree range and wall speed is used.
