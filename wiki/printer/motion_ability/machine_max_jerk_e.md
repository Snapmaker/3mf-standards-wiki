# machine_max_jerk_e

> Location: Printer → Motion ability → Jerk limitation

---

## Jerk limitation

Safeguard maximum jerks for all axes.

> [!TIP]
> Check the [Cornering Calibration](../../calibration/cornering_calib.md).

### Maximum Jerk

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `machine_max_jerk_x`, `machine_max_jerk_y`, `machine_max_jerk_z`, `machine_max_jerk_e`.  
[Type](../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--machine-max-jerk-x=1` (same pattern for the other variables above).  
Maximum [jerk](../../process/speed/speed_settings_jerk_xy.md) for each axis (M205 X, Y, Z, E, only apply if JD = 0 for Marlin 2 Firmware)

### Maximum Junction Deviation

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `machine_max_junction_deviation`.  
[Type](../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--machine-max-junction-deviation=1`.  
Maximum [junction deviation](../../process/speed/speed_settings_jerk_xy.md#junction-deviation) (M205 J, only apply if JD > 0 for Marlin Firmware. If your Marlin 2 printer uses Classic Jerk set this value to 0.)
