# cooling_perimeter_transition_distance

> Location: Filament → Cooling → Part cooling fan
> Status: placeholder — fork-added parameter, to be completed.
> Visibility: [`cooling_slowdown_logic`](cooling_slowdown_logic.md) is set to Consistent surface.

## Basic information

- Label: Perimeter transition distance
- Type: Float list, unit mm, range 0–50
- Default: 10.0
- Mode: Developer

> Tooltip (original): Distance in millimeters before the end of slowed perimeters where the original print speed is gradually restored. This prevents visible speed transitions at the end of perimeters.
> Only applies when 'Consistent surface' cooling logic is selected.

## Notes

How many millimeters before the end of a slowed-down perimeter the original speed is gradually restored, avoiding a visible speed-step mark at the end of the wall. Only effective when [`cooling_slowdown_logic`](cooling_slowdown_logic.md) = Consistent surface.

(To add: relation to outer-wall surface quality, value guidance)
