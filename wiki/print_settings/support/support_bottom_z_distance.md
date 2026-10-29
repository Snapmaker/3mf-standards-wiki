# support_bottom_z_distance

> 所在界面：工艺设置 → Support → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_advanced.md` 的「Z distance」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`support_top_z_distance`（各另有独立文档）。

---

## Z distance

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `support_top_z_distance`, `support_bottom_z_distance`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--support-top-z-distance=1` (same pattern for the other variables above).  
The Z gap between the support and the object: **Top Z distance** is the gap between the top of the support and the overhang above it, and **Bottom Z distance** the gap between the object and a support standing on it. Both are rounded to a multiple of the layer height unless [Independent support layer height](#independent-support-layer-height) is enabled.

A Top Z distance of `0` is meant for soluble supports. In that case, Bottom Z distance is also ignored when there are bottom interface layers, and the support is printed in direct contact with the object.
