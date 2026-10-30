# default_junction_deviation

> Location: Process → Speed → Jerk(XY)
> 显隐条件（初步梳理，待校对）：仅 Marlin 类固件（Jerk 限制组）显示

---

### Junction Deviation

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `default_junction_deviation`.  
[Type](../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--default-junction-deviation=1`.  
Alternative to Jerk, Junction Deviation is the default method for controlling cornering speed in Marlin 2 printers.  
Instead of setting a cornering speed for each line type, it calculates the cornering speed from [each line's acceleration](../../process/speed/speed_settings_acceleration.md) and the corner angle. A Junction Deviation equivalent to a given jerk value can be estimated with the formula:

$$
JD = 0.4 \cdot \frac{\text{Jerk}^2}{\text{Accel.}}
$$

Higher values result in faster and more aggressive cornering speeds, while lower values produce smoother, more controlled cornering.

> [!NOTE]
> Classic Jerk can still be used in Marlin 2, but it is deprecated in favor of Junction Deviation.  
> If your printer uses Classic Jerk, set [Maximum Junction Deviation](../../printer/motion_ability/printer_motion_ability.md#maximum-junction-deviation) to `0` in the printer settings to enable the Jerk settings.

This value is limited by [Printer settings > Motion ability > Maximum Junction Deviation](../../printer/motion_ability/printer_motion_ability.md#maximum-junction-deviation).
