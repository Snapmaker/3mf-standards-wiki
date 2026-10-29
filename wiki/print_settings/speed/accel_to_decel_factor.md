# accel_to_decel_factor

> 所在界面：工艺设置 → Speed → Acceleration
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_acceleration.md` 的「Accel to decel」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅 Klipper 固件显示

---

### Accel to decel

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `accel_to_decel_factor`.  
[Type](option_type#integer-float-percentage): `Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--accel-to-decel-factor=20%`.  
Percentage of the acceleration that Klipper's `max_accel_to_decel` is set to, from 1% to 100% (default 50%).  
For example, at 5000 mm/s² and 50%, Orca sends `SET_VELOCITY_LIMIT ACCEL=5000 ACCEL_TO_DECEL=2500`.  
It can only be edited when [Enable accel to decel](#enable-accel-to-decel) is checked.
