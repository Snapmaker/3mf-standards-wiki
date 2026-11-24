# accel_to_decel_enable

> Location: Process → Speed → Acceleration → Enable accel to decel
> Visibility (preliminary, pending review): Shown only with Klipper firmware

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `accel_to_decel_enable`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `true`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--accel-to-decel-enable=1`.  

Adjusts Klipper's `max_accel_to_decel` automatically. Each time Orca sets the acceleration with `SET_VELOCITY_LIMIT ACCEL=`, it adds `ACCEL_TO_DECEL=` at the [accel to decel](accel_to_decel_factor.md) percentage of that acceleration. When disabled, `ACCEL_TO_DECEL` is not sent.  
This option is only shown when the [G-code flavor](../../printer/basic_information/gcode_flavor.md) is Klipper, and it is enabled by default.
