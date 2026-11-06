# ironing_speed

> Location: Process → Speed → Other layers speed

---

## Ironing speed

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `ironing_speed`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[Default](../../../general_settings/option_type.md#default-value): `20`.  
[Range](../../../general_settings/option_type.md#range): `≥ 1` mm/s.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--ironing-speed=1`.  
[Ironing](../../process/support/support_ironing.md) and [Support Ironing](../../process/support/support_ironing.md) speed, typically slower than the top surface speed to ensure a smooth finish.  
Each filament can replace this speed with its own Ironing speed in its [setting overrides](../../process/quality/ironing_type.md).
