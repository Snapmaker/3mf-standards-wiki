# travel_short_distance_acceleration

> Location: Process → Speed → Acceleration → Short travel
> Status: placeholder — fork-added parameter, to be completed.

---

[Mode](../../../general_settings/option_mode.md): `Developer`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `travel_short_distance_acceleration`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `250`.  
[Unit](../../../general_settings/option_type.md#unit): `mm/s²`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--travel-short-distance-acceleration=1`.  

Acceleration used for short travel moves near external perimeters. Short travels are moves shorter than the 'Retraction minimum travel' distance.
Lower values (e.g., 250-500 mm/s²) reduce ringing artifacts on sharp corners without significantly impacting print time.
Set to 0 to disable (uses normal travel acceleration).

## Notes

Acceleration for **short travel moves** near outer walls. "Short" means a travel shorter than the filament's [Retraction minimum travel](../../filament/setting_overrides/filament_retraction_minimum_travel.md) (`filament_retraction_minimum_travel`) distance.

Lowering it (e.g. 250–500 mm/s²) reduces ringing at sharp corners with almost no impact on print time; 0 disables it and falls back to the regular [`travel_acceleration`](travel_acceleration.md).

<!-- TODO: interplay with input shaping -->
