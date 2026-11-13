# infill_jerk

> Location: Process → Speed → Jerk(XY)

---

### Infill

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `infill_jerk`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `9`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` mm/s.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--infill-jerk=1`.  
Jerk for infill printing. This is usually set to a value higher than inner wall printing to improve speed.
