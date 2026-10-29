# graphic_effect_plate_temp_initial_layer

> 所在界面：耗材设置 → Filament → Bed temperature
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_jerk_xy.md` 的「Initial layer」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅当打印机启用对应床型时显示
> 本小节同时涵盖：`initial_layer_jerk`（各另有独立文档）。

---

### Initial layer

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `initial_layer_jerk`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--initial-layer-jerk=1`.  
Jerk for initial layer printing. This is usually set to a lower value than top surface to improve adhesion.
