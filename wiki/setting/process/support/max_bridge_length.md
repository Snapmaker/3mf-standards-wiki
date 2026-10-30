# max_bridge_length

> Location: Process → Support → Advanced

---

## Max bridge length

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `max_bridge_length`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--max-bridge-length=1`.  
The longest bridge that tree supports leave unsupported. It replaces [Don't support bridges](#dont-support-bridges) for every tree style, including Organic. Bridges up to this length that are anchored at both ends are printed without support, and longer ones are supported along their whole length. `0` supports all bridges, and a very large value leaves every bridge unsupported.

With the Tree Slim, Tree Strong and Tree Hybrid styles, the branch tips placed inside an overhang are also spaced at least half this length apart, so a value above twice [Branch Distance](../../process/support/support_settings_tree.md#branch-distance) spreads them further apart.
