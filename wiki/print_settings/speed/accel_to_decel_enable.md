# accel_to_decel_enable

> 所在界面：工艺设置 → Speed → Acceleration
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_acceleration.md` 的「Enable accel to decel」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅 Klipper 固件显示

---

## Enable accel to decel

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `accel_to_decel_enable`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--accel-to-decel-enable=1`.  
Adjusts Klipper's `max_accel_to_decel` automatically. Each time Orca sets the acceleration with `SET_VELOCITY_LIMIT ACCEL=`, it adds `ACCEL_TO_DECEL=` at the [accel to decel](#accel-to-decel) percentage of that acceleration. When disabled, `ACCEL_TO_DECEL` is not sent.  
This option is only shown when the [G-code flavor](printer_basic_information_advanced#g-code-flavor) is Klipper, and it is enabled by default.
