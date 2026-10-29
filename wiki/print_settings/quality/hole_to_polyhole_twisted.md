# hole_to_polyhole_twisted

> 所在界面：工艺设置 → Quality → Precision
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_precision.md` 的「Polyholes」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`hole_to_polyhole`、`hole_to_polyhole_threshold`（各另有独立文档）。

---

## Polyholes

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `hole_to_polyhole`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--hole-to-polyhole=1`.  
A polyhole is a technique used in FFF 3D printing to improve the accuracy of circular holes. Instead of modeling a perfect circle, the hole is represented as a polygon with a reduced number of flat sides. This simplification forces the slicer to treat each segment as a straight line, which prints more reliably. By carefully choosing the number of sides and ensuring the polygon sits on the outer boundary of the hole, you can produce openings that more closely match the intended diameter.

![PolyHoles](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/PolyHoles.png?raw=true)

- Original implementation: [SuperSlicer Polyholes](https://github.com/supermerill/SuperSlicer/wiki/Polyholes)
- Idea and mathematics: [Hydraraptor](https://hydraraptor.blogspot.com/2011/02/polyholes.html)
