# cooling_perimeter_transition_distance

> Location: Filament → Cooling → Part cooling fan → Perimeter transition distance
> Status: placeholder — fork-added parameter, to be completed.
> Visibility: [`cooling_slowdown_logic`](cooling_slowdown_logic.md) is set to Consistent surface.

---

[Mode](../../../general_settings/option_mode.md): `Developer`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `cooling_perimeter_transition_distance`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[Default](../../../general_settings/option_type.md#default-value): `10.0`.  
[Unit](../../../general_settings/option_type.md#unit): `mm`.  
[Range](../../../general_settings/option_type.md#range): `0–50`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--cooling-perimeter-transition-distance=1`.  

Distance in millimeters before the end of slowed perimeters where the original print speed is gradually restored. This prevents visible speed transitions at the end of perimeters.
Only applies when 'Consistent surface' cooling logic is selected.

## Notes

How many millimeters before the end of a slowed-down perimeter the original speed is gradually restored, avoiding a visible speed-step mark at the end of the wall. Only effective when [`cooling_slowdown_logic`](cooling_slowdown_logic.md) = Consistent surface.

<!-- TODO: relation to outer-wall surface quality, value guidance -->
