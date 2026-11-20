# bridge_speed

> Location: Process → Speed → Overhang speed → External
> Status: placeholder — to be completed.

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `bridge_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `25`.  
[Unit](../../../general_settings/option_type.md#unit): `mm/s`.  
[Range](../../../general_settings/option_type.md#range): `≥ 1`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--bridge-speed=1`.  

Speed of the externally visible bridge extrusions.\n\nIn addition, if Slow down for curled perimeters is disabled or Classic overhang mode is enabled, it will be the print speed of overhang walls that are supported by less than 13%, whether they are part of a bridge or an overhang.
