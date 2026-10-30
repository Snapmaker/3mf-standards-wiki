# internal_bridge_flow

> Location: Process → Quality → Bridging
> 本小节同时涵盖：`bridge_flow`（各另有独立文档）。

---

## Flow ratio

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `bridge_flow`, `internal_bridge_flow`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--bridge-flow=1` (same pattern for the other variables above).  
This value governs the thickness of the bridge layer.

For external bridges, when material tends to sag, reducing the flow ratio can help improve appearance.  
For internal bridges, increasing the flow ratio can enhance strength and upper layer quality.

- Values above 1.0: Increase the amount of material while maintaining line spacing. This can improve line contact and strength.
- Values below 1.0: Reduce the amount of material while adjusting line spacing to maintain contact. This can reduce sagging.

The actual bridge flow used is calculated by multiplying this value with the [filament flow ratio](../../filament/filament/material_flow_ratio_and_pressure_advance.md#flow-ratio), and if set, the object's flow ratio.  
For internal bridges, the internal bridge flow ratio is also multiplied by the bridge flow ratio.
