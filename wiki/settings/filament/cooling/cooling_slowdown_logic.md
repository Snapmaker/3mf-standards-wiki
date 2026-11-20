# cooling_slowdown_logic

> Location: Filament → Cooling → Part cooling fan
> Status: placeholder — fork-added parameter, to be completed.
> Visibility: shown after [`slow_down_for_layer_cooling`](slow_down_for_layer_cooling.md) is checked.

## Basic information

- Label: Cooling slowdown logic
- Mode: Developer
- Type: Choice list (single choice: Uniform cooling / Consistent surface)
- Default: uniform_cooling

> Tooltip: Determines how the printer slows down when minimum layer time isn't reached.
> 'Uniform cooling' slows down all print features equally (current default behavior).
> 'Consistent surface' prioritizes slowing infill and internal perimeters first, preserving external perimeter speed for better surface finish on glossy filaments. This helps reduce VFA (Vertical Fine Artifacts) and maintains consistent surface shine.

## Notes

Determines the slowdown strategy when the minimum layer time is not met (ported from PrusaSlicer 2.9.3 to reduce VFA):

- **Uniform cooling** (default): all features slow down proportionally, i.e. the original behavior;
- **Consistent surface**: slows down infill and inner walls first, preserving outer-wall speed for a consistent surface finish; selecting it activates the companion parameter [`cooling_perimeter_transition_distance`](cooling_perimeter_transition_distance.md).

(To add: effect comparison of the two modes, suitable filaments)
