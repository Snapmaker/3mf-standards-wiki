# machine_max_jerk_x

> Location: Printer → Motion ability → Jerk limitation

---

## Jerk limitation

Safeguard maximum jerks for all axes.

> [!TIP]
> Check the [Cornering Calibration](../../../calibration/cornering_calib.md).

### Maximum Jerk

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `machine_max_jerk_x`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): — no static default.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--machine-max-jerk-x=1`.  
Maximum [jerk](../../process/speed/default_jerk.md) for each axis (M205 X, Y, Z, E, only apply if JD = 0 for Marlin 2 Firmware)

### Maximum Junction Deviation

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `machine_max_junction_deviation`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `0, 0`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` mm.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--machine-max-junction-deviation=1`.  
Maximum [junction deviation](../../printer/motion_ability/machine_max_junction_deviation.md) (M205 J, only apply if JD > 0 for Marlin Firmware. If your Marlin 2 printer uses Classic Jerk set this value to 0.)
