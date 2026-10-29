# overhang_4_4_speed

> 所在界面：工艺设置 → Speed → Overhang speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_overhang_speed.md` 的「Speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`overhang_1_4_speed`、`overhang_2_4_speed`、`overhang_3_4_speed`（各另有独立文档）。

---

### Speed

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `overhang_1_4_speed`, `overhang_2_4_speed`, `overhang_3_4_speed`, `overhang_4_4_speed`.  
[Type](option_type#list-types): `Float or Percentage list`.  
[CLI Example](cli_mode#setting-overrides): `--overhang-1-4-speed=20%` (same pattern for the other variables above).  
This is the speed for various overhang degrees. Overhang degrees are expressed as a percentage of [line width](quality_settings_line_width).  
If expressed as a percentage, the speed is calculated from the [outer wall speed](speed_settings_other_layers_speed#outer-wall) for outer walls and from the [inner wall speed](speed_settings_other_layers_speed#inner-wall) for inner walls.

> [!NOTE]
> 0 speed means no slowing down for the overhang degree range and wall speed is used.
