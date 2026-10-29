# max_bridge_length

> 所在界面：工艺设置 → Support → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_advanced.md` 的「Max bridge length」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Max bridge length

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `max_bridge_length`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--max-bridge-length=1`.  
The longest bridge that tree supports leave unsupported. It replaces [Don't support bridges](#dont-support-bridges) for every tree style, including Organic. Bridges up to this length that are anchored at both ends are printed without support, and longer ones are supported along their whole length. `0` supports all bridges, and a very large value leaves every bridge unsupported.

With the Tree Slim, Tree Strong and Tree Hybrid styles, the branch tips placed inside an overhang are also spaced at least half this length apart, so a value above twice [Branch Distance](support_settings_tree#branch-distance) spreads them further apart.
