# infill_anchor_max

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_infill.md` 的「Anchor」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`infill_anchor`（各另有独立文档）。

---

## Anchor

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `infill_anchor_max`, `infill_anchor`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--infill-anchor-max=20%` (same pattern for the other variables above).  
Connect an infill line to an internal perimeter with a short segment of an additional perimeter. If expressed as a percentage (example: 15%), it is calculated over the infill extrusion width.
OrcaSlicer tries to connect two close infill lines to a short perimeter segment. If no such perimeter segment shorter than the Maximum length of the infill anchor is found, the infill line is connected to a perimeter segment at just one side and the length of the perimeter segment taken is limited to the Sparse infill anchor length, but no longer than the Maximum length of the infill anchor. If the Maximum length of the infill anchor is set to 0, the old algorithm for infill connection is used, which should create the same result as 1000 & 0.

When a line end cannot be connected to its neighbor, its anchor runs along the wall toward the nearest free line end, where the next infill path usually starts. Two line ends whose anchors would meet are connected instead. With [multiline](#fill-multiline) infill, an anchor stops short of the other lines of its group instead of printing over them.

Line ends left next to each other, about two line widths apart or closer, are joined with a short straight segment so they print as one path, also when the Maximum length of the infill anchor is `0`.

[Concentric](strength_settings_patterns#concentric) loops follow the outline of the infill area instead of ending at the walls, so there is nothing to anchor and both settings are hidden for that pattern.  
With the [Line](strength_settings_patterns#line) pattern both settings are disabled, and the Sparse infill anchor length is also disabled whenever the Maximum length of the infill anchor is `0`.

- **Anchor Off**

![InfillAnchorOff](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/InfillAnchorOff.png?raw=true)

- **Anchor On**

![InfillAnchorOn](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/InfillAnchorOn.png?raw=true)
