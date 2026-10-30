# bridge_density

> Location: Process → Quality → Bridging
> 本小节同时涵盖：`internal_bridge_density`（各另有独立文档）。

---

## Bridge density

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `bridge_density`, `internal_bridge_density`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Percentage`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--bridge-density=20%` (same pattern for the other variables above).  
Controls the density (spacing) of external and internal bridge lines. Default is 100%.  
Theoretically, 100% means a solid bridge, but due to the tendency of bridge extrusions to sag, 100% may not be sufficient.

- Higher than 100% density (**Recommended**, max 125%):
    - Pros: Produces smoother bridge surfaces, as overlapping lines provide additional support during printing.
    - Cons: Can cause overextrusion, decreasing lower and upper surface quality.
- Lower than 100% density (min 10%):
    - Pros: Can create a string-like first layer. Faster and with better cooling, as there is more space for air to circulate around the extruded bridge.
    - Cons: May lead to sagging and poor surface finish.

The density changes the spacing between bridge lines, not the [flow ratio](#flow-ratio) of each line.
