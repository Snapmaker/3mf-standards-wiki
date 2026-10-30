# support_bottom_z_distance

> Location: Process → Support → Advanced
> 本小节同时涵盖：`support_top_z_distance`（各另有独立文档）。

---

## Z distance

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `support_top_z_distance`, `support_bottom_z_distance`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--support-top-z-distance=1` (same pattern for the other variables above).  
The Z gap between the support and the object: **Top Z distance** is the gap between the top of the support and the overhang above it, and **Bottom Z distance** the gap between the object and a support standing on it. Both are rounded to a multiple of the layer height unless [Independent support layer height](#independent-support-layer-height) is enabled.

A Top Z distance of `0` is meant for soluble supports. In that case, Bottom Z distance is also ignored when there are bottom interface layers, and the support is printed in direct contact with the object.
