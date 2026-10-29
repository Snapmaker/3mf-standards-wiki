# bridge_flow

> 所在界面：工艺设置 → Quality → Bridging
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_bridging.md` 的「Flow ratio」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`internal_bridge_flow`（各另有独立文档）。

---

## Flow ratio

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `bridge_flow`, `internal_bridge_flow`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--bridge-flow=1` (same pattern for the other variables above).  
This value governs the thickness of the bridge layer.

For external bridges, when material tends to sag, reducing the flow ratio can help improve appearance.  
For internal bridges, increasing the flow ratio can enhance strength and upper layer quality.

- Values above 1.0: Increase the amount of material while maintaining line spacing. This can improve line contact and strength.
- Values below 1.0: Reduce the amount of material while adjusting line spacing to maintain contact. This can reduce sagging.

The actual bridge flow used is calculated by multiplying this value with the [filament flow ratio](material_flow_ratio_and_pressure_advance#flow-ratio), and if set, the object's flow ratio.  
For internal bridges, the internal bridge flow ratio is also multiplied by the bridge flow ratio.
