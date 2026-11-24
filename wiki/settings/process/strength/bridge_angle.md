# bridge_angle

> Location: Process → Strength → Advanced → Bridge infill direction
> Also in this section: `internal_bridge_angle` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `bridge_angle`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[Unit](../../../general_settings/option_type.md#unit): `°`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--bridge-angle=1`.  

If left to zero, the bridging angle will be calculated automatically for each specific bridge.  
Otherwise the provided angle will be used according to:

- The absolute coordinates
- The absolute coordinates + Model rotation: If [Align directions to model](align_infill_direction_to_model.md) is enabled
- The optimal automatic angle + this value: If Relative Bridge Angle is enabled

> [!NOTE]
> Use 180° for zero absolute angle.
