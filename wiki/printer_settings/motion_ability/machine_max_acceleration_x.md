# machine_max_acceleration_x

> 所在界面：打印机设置 → Motion ability → Acceleration limitation
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/motion ability/printer_motion_ability.md` 的「Acceleration limitation」小节（2026-10-28），英文原文，待本地化校对。

---

## Acceleration limitation

[Modes](option_mode):  
`Simple` [Variables](built_in_placeholders_variables): `machine_max_acceleration_x`, `machine_max_acceleration_y`, `machine_max_acceleration_z`, `machine_max_acceleration_e`, `machine_max_acceleration_extruding`, `machine_max_acceleration_retracting`.  
`Advanced` [Variable](built_in_placeholders_variables): `machine_max_acceleration_travel`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--machine-max-acceleration-x=1` (same pattern for the other variables above).  
Safeguard maximum accelerations for all axes.
This will cap the acceleration set by the process if it exceeds these values.
