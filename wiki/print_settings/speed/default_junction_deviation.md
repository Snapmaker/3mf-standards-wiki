# default_junction_deviation

> 所在界面：工艺设置 → Speed → Jerk(XY)
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_jerk_xy.md` 的「Junction Deviation」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅 Marlin 类固件（Jerk 限制组）显示

---

### Junction Deviation

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `default_junction_deviation`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--default-junction-deviation=1`.  
Alternative to Jerk, Junction Deviation is the default method for controlling cornering speed in Marlin 2 printers.  
Instead of setting a cornering speed for each line type, it calculates the cornering speed from [each line's acceleration](speed_settings_acceleration) and the corner angle. A Junction Deviation equivalent to a given jerk value can be estimated with the formula:

$$
JD = 0.4 \cdot \frac{\text{Jerk}^2}{\text{Accel.}}
$$

Higher values result in faster and more aggressive cornering speeds, while lower values produce smoother, more controlled cornering.

> [!NOTE]
> Classic Jerk can still be used in Marlin 2, but it is deprecated in favor of Junction Deviation.  
> If your printer uses Classic Jerk, set [Maximum Junction Deviation](printer_motion_ability#maximum-junction-deviation) to `0` in the printer settings to enable the Jerk settings.

This value is limited by [Printer settings > Motion ability > Maximum Junction Deviation](printer_motion_ability#maximum-junction-deviation).
