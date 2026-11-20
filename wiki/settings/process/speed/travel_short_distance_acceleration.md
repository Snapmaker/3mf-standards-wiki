# travel_short_distance_acceleration

> Location: Process → Speed → Acceleration
> Status: placeholder — fork-added parameter, to be completed.

## Basic information

- Label: Short travel
- Mode: Developer
- Type: Float list, unit mm/s², min 0
- Default: 250

> Tooltip (original): Acceleration used for short travel moves near external perimeters. Short travels are moves shorter than the 'Retraction minimum travel' distance.
> Lower values (e.g., 250-500 mm/s²) reduce ringing artifacts on sharp corners without significantly impacting print time.
> Set to 0 to disable (uses normal travel acceleration).

## Notes

Acceleration for **short travel moves** near outer walls. "Short" means a travel shorter than the filament's [Retraction minimum travel](../../filament/setting_overrides/filament_retraction_minimum_travel.md) (`filament_retraction_minimum_travel`) distance.

Lowering it (e.g. 250–500 mm/s²) reduces ringing at sharp corners with almost no impact on print time; 0 disables it and falls back to the regular [`travel_acceleration`](travel_acceleration.md).

(To add: interplay with input shaping)
