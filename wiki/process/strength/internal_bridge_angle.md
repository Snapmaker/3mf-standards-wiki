# internal_bridge_angle

> Location: Process → Strength → Advanced
> 本小节同时涵盖：`bridge_angle`（各另有独立文档）。

---

## Bridge infill direction

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `bridge_angle`, `internal_bridge_angle`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--bridge-angle=1` (same pattern for the other variables above).  
If left to zero, the bridging angle will be calculated automatically for each specific bridge.  
Otherwise the provided angle will be used according to:

- The absolute coordinates
- The absolute coordinates + Model rotation: If [Align directions to model](#align-directions-to-model) is enabled
- The optimal automatic angle + this value: If [Relative Bridge Angle](#relative-bridge-angle) is enabled

> [!NOTE]
> Use 180° for zero absolute angle.
