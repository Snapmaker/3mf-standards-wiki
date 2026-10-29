# internal_bridge_angle

> 所在界面：工艺设置 → Strength → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_advanced.md` 的「Bridge infill direction」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`bridge_angle`（各另有独立文档）。

---

## Bridge infill direction

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `bridge_angle`, `internal_bridge_angle`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--bridge-angle=1` (same pattern for the other variables above).  
If left to zero, the bridging angle will be calculated automatically for each specific bridge.  
Otherwise the provided angle will be used according to:

- The absolute coordinates
- The absolute coordinates + Model rotation: If [Align directions to model](#align-directions-to-model) is enabled
- The optimal automatic angle + this value: If [Relative Bridge Angle](#relative-bridge-angle) is enabled

> [!NOTE]
> Use 180° for zero absolute angle.
