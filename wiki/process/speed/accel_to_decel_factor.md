# accel_to_decel_factor

> Location: Process → Speed → Acceleration
> 显隐条件（初步梳理，待校对）：仅 Klipper 固件显示

---

### Accel to decel

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `accel_to_decel_factor`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Percentage`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--accel-to-decel-factor=20%`.  
Percentage of the acceleration that Klipper's `max_accel_to_decel` is set to, from 1% to 100% (default 50%).  
For example, at 5000 mm/s² and 50%, Orca sends `SET_VELOCITY_LIMIT ACCEL=5000 ACCEL_TO_DECEL=2500`.  
It can only be edited when [Enable accel to decel](#enable-accel-to-decel) is checked.
