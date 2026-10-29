# bridge_density

> 所在界面：工艺设置 → Quality → Bridging
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_bridging.md` 的「Bridge density」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`internal_bridge_density`（各另有独立文档）。

---

## Bridge density

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `bridge_density`, `internal_bridge_density`.  
[Type](option_type#integer-float-percentage): `Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--bridge-density=20%` (same pattern for the other variables above).  
Controls the density (spacing) of external and internal bridge lines. Default is 100%.  
Theoretically, 100% means a solid bridge, but due to the tendency of bridge extrusions to sag, 100% may not be sufficient.

- Higher than 100% density (**Recommended**, max 125%):
    - Pros: Produces smoother bridge surfaces, as overlapping lines provide additional support during printing.
    - Cons: Can cause overextrusion, decreasing lower and upper surface quality.
- Lower than 100% density (min 10%):
    - Pros: Can create a string-like first layer. Faster and with better cooling, as there is more space for air to circulate around the extruded bridge.
    - Cons: May lead to sagging and poor surface finish.

The density changes the spacing between bridge lines, not the [flow ratio](#flow-ratio) of each line.
