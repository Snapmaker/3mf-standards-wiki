# travel_jerk

> Location: Process → Speed → Jerk(XY)

---

### Travel

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `travel_jerk`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `12`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` mm/s.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--travel-jerk=1`.  
Jerk for travel moves. This is usually set to a higher value than infill to reduce travel time.
