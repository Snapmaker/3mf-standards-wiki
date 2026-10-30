# filament_flow_ratio

> Location: Filament → Filament → Flow ratio and Pressure Advance

---

## Flow Ratio

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_flow_ratio`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-flow-ratio=1`.  
The material may have volumetric change after switching between molten and crystalline states. This setting changes all extrusion flow of this filament in G-code proportionally.  
The recommended value range is between 0.95 and 1.05. You may be able to tune this value to get a nice flat surface if there is slight overflow or underflow.  
The final object flow ratio is this value multiplied by the [filament flow ratio](../../filament/filament/material_flow_ratio_and_pressure_advance.md#flow-ratio).

> [!TIP]
> Check the [Flow Ratio Calibration guide](../../../calibration/flow_ratio_calib.md).
