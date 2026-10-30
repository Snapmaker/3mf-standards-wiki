# fan_kickstart

> Location: Printer → Basic information → Cooling Fan

---

## Fan kick-start time

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `fan_kickstart`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--fan-kickstart=1`.  
Emit a max fan speed command for this amount of seconds before reducing to target speed to kick-start the cooling fan.
This is useful for fans where a low PWM/power may be insufficient to get the fan started spinning from a stop, or to get the fan up to speed faster.
Set to 0 to deactivate.
