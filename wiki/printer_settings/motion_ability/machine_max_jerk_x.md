# machine_max_jerk_x

> 所在界面：打印机设置 → Motion ability → Jerk limitation
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/motion ability/printer_motion_ability.md` 的「Jerk limitation」小节（2026-10-28），英文原文，待本地化校对。

---

## Jerk limitation

Safeguard maximum jerks for all axes.

> [!TIP]
> Check the [Cornering Calibration](cornering_calib).

### Maximum Jerk

[Mode](option_mode): `Simple`.  
[Variables](built_in_placeholders_variables): `machine_max_jerk_x`, `machine_max_jerk_y`, `machine_max_jerk_z`, `machine_max_jerk_e`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--machine-max-jerk-x=1` (same pattern for the other variables above).  
Maximum [jerk](speed_settings_jerk_xy) for each axis (M205 X, Y, Z, E, only apply if JD = 0 for Marlin 2 Firmware)

### Maximum Junction Deviation

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `machine_max_junction_deviation`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--machine-max-junction-deviation=1`.  
Maximum [junction deviation](speed_settings_jerk_xy#junction-deviation) (M205 J, only apply if JD > 0 for Marlin Firmware. If your Marlin 2 printer uses Classic Jerk set this value to 0.)
