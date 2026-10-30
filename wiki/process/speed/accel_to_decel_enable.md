# accel_to_decel_enable

> Location: Process → Speed → Acceleration
> 显隐条件（初步梳理，待校对）：仅 Klipper 固件显示

---

## Enable accel to decel

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `accel_to_decel_enable`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--accel-to-decel-enable=1`.  
Adjusts Klipper's `max_accel_to_decel` automatically. Each time Orca sets the acceleration with `SET_VELOCITY_LIMIT ACCEL=`, it adds `ACCEL_TO_DECEL=` at the [accel to decel](#accel-to-decel) percentage of that acceleration. When disabled, `ACCEL_TO_DECEL` is not sent.  
This option is only shown when the [G-code flavor](../../printer/basic_information/printer_basic_information_advanced.md#g-code-flavor) is Klipper, and it is enabled by default.
