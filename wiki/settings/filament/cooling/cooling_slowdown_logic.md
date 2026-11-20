# cooling_slowdown_logic

> Location: Filament → Cooling → Part cooling fan → Cooling slowdown logic
> Status: placeholder — fork-added parameter, to be completed.
> Visibility: shown after [`slow_down_for_layer_cooling`](slow_down_for_layer_cooling.md) is checked.

---

[Mode](../../../general_settings/option_mode.md): `Developer`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `cooling_slowdown_logic`.  
[Type](../../../general_settings/option_type.md#list-types): `Choice list (single choice: Uniform cooling / Consistent surface)`.  
[Default](../../../general_settings/option_type.md#default-value): `uniform_cooling`.  
[Options](../../../general_settings/option_type.md#choice): `uniform_cooling, consistent_surface`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--cooling-slowdown-logic=value`.  

Determines how the printer slows down when minimum layer time isn't reached.
'Uniform cooling' slows down all print features equally (current default behavior).
'Consistent surface' prioritizes slowing infill and internal perimeters first, preserving external perimeter speed for better surface finish on glossy filaments. This helps reduce VFA (Vertical Fine Artifacts) and maintains consistent surface shine.

## Notes

Determines the slowdown strategy when the minimum layer time is not met (ported from PrusaSlicer 2.9.3 to reduce VFA):

- **Uniform cooling** (default): all features slow down proportionally, i.e. the original behavior;
- **Consistent surface**: slows down infill and inner walls first, preserving outer-wall speed for a consistent surface finish; selecting it activates the companion parameter [`cooling_perimeter_transition_distance`](cooling_perimeter_transition_distance.md).

<!-- TODO: effect comparison of the two modes, suitable filaments -->
