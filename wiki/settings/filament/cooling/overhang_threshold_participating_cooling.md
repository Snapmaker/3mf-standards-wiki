# overhang_threshold_participating_cooling

> Location: Filament → Cooling → Part cooling fan → Overhang threshold for participating cooling
> Status: placeholder — fork-added parameter, to be completed.

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `overhang_threshold_participating_cooling`.  
[Type](../../../general_settings/option_type.md#list-types): `Choice list (six levels: none / 1_4 / 2_4 / 3_4 / 4_4 / bridge; the UI shows 0% / 10% / 25% / 50% / 75% / 100%)`.  
[Default](../../../general_settings/option_type.md#default-value): `95%`.  
[Options](../../../general_settings/option_type.md#choice): `0%, 10%, 25%, 50%, 75%, 100%`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--overhang-threshold-participating-cooling=value`.  

Decide which overhang part join the cooling function to slow down the speed. Expressed as percentage which indicates how much width of the line is without support from the lower layer. 100% means forcing cooling for all outer wall no matter how much overhang degree.

## Notes

Determines how much of an **outer wall** must be overhanging to join the slow-down-for-cooling behavior: the percentage is the unsupported share of the line width. 100% means all outer walls join the slowdown regardless of overhang angle.

Sits next to [`overhang_fan_threshold`](overhang_fan_threshold.md) (the fan speed-up trigger threshold) but governs the **slowdown** side.

> [!NOTE]
> The bridge enum level is serialized as 95%; the UI dropdown shows it as the 100% level.

<!-- TODO: interaction details with slow_down_for_layer_cooling -->
