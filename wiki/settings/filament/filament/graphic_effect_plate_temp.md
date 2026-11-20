# graphic_effect_plate_temp

> Location: Filament → Filament → Bed temperature → Other layers
> Status: placeholder — to be completed.
> Visibility (preliminary, pending review): Shown only when the printer enables the corresponding bed type

---

[Mode](../../../general_settings/option_mode.md): —.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `graphic_effect_plate_temp`.  
[Type](../../../general_settings/option_type.md#list-types): `Integer list`.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[Unit](../../../general_settings/option_type.md#unit): `℃`.  
[Range](../../../general_settings/option_type.md#range): `0–300`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--graphic-effect-plate-temp=1`.  

Bed temperature for layers except the initial one. A value of 0 means the filament does not support printing on this plate.
