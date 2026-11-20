# overhang_threshold_participating_cooling

> Location: Filament → Cooling → Part cooling fan
> Status: placeholder — fork-added parameter, to be completed.

## Basic information

- Label: Overhang threshold for participating cooling
- Type: Choice list (six levels: none / 1_4 / 2_4 / 3_4 / 4_4 / bridge; the UI shows 0% / 10% / 25% / 50% / 75% / 100%)
- Default: 95% (bridge level)
- Mode: Advanced

> Tooltip (original): Decide which overhang part join the cooling function to slow down the speed. Expressed as percentage which indicates how much width of the line is without support from the lower layer. 100% means forcing cooling for all outer wall no matter how much overhang degree.

## Notes

Determines how much of an **outer wall** must be overhanging to join the slow-down-for-cooling behavior: the percentage is the unsupported share of the line width. 100% means all outer walls join the slowdown regardless of overhang angle.

Sits next to [`overhang_fan_threshold`](overhang_fan_threshold.md) (the fan speed-up trigger threshold) but governs the **slowdown** side.

> [!NOTE]
> The bridge enum level is serialized as 95%; the UI dropdown shows it as the 100% level.

(To add: interaction details with slow_down_for_layer_cooling)
