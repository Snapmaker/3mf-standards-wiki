# complete_print_exhaust_fan_speed

> Location: Filament → Cooling → Exhaust fan

---

#### Complete print

> [!WARNING] fork 未实现
> `activate_air_filtration_on_completion` 为上游 OrcaSlicer 参数，fork 未收录；本小节其余参数 fork 正常。

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `activate_air_filtration_on_completion`, `complete_print_exhaust_fan_speed`.  
[Type](../../../general_settings/option_type.md): `activate_air_filtration_on_completion` (Boolean list), `complete_print_exhaust_fan_speed` (Integer list).  
[Defaults](../../../general_settings/option_type.md#default-value): `activate_air_filtration_on_completion` (—), `complete_print_exhaust_fan_speed` (80).  
[Ranges](../../../general_settings/option_type.md#range): `complete_print_exhaust_fan_speed` (`0–100` %).  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--activate-air-filtration-on-completion=1` (`activate_air_filtration_on_completion` shown; other variables above follow their own type).  
Speed of exhaust fan after printing completes.
