# small_area_infill_flow_compensation_model

> 所在界面：工艺设置 → Quality → Walls and surfaces
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_wall_and_surfaces.md` 的「Small area flow compensation」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`small_area_infill_flow_compensation`（各另有独立文档）。

---

## Small area flow compensation

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `small_area_infill_flow_compensation`, `small_area_infill_flow_compensation_model`.  
[Type](option_type): `small_area_infill_flow_compensation` (Boolean), `small_area_infill_flow_compensation_model` (Text list).  
[CLI Example](cli_mode#setting-overrides): `--small-area-infill-flow-compensation=1` (`small_area_infill_flow_compensation` shown; other variables above follow their own type).  
Enables adaptive flow control for small infill areas.
This feature helps address extrusion problems that often occur in small regions of solid infill, such as the tops of narrow letters or fine features.  
In these cases, standard extrusion flow may be too much for the available space, leading to over-extrusion or poor surface quality.

![flow-compensation-model](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/flow-compensation-model.png?raw=true)

It works by dynamically adjusting the extrusion flow based on the length of the extrusion path, ensuring more precise material deposition in small spaces.

The compensation only applies to internal solid infill, top surfaces and first layer bottom surfaces, and only when that surface uses the [Rectilinear](strength_settings_patterns#rectilinear), [Aligned Rectilinear](strength_settings_patterns#aligned-rectilinear), [Monotonic](strength_settings_patterns#monotonic) or [Monotonic line](strength_settings_patterns#monotonic-line) pattern.

This is a native implementation of @Alexander-T-Moss's [Small Area Flow Compensation](https://github.com/Alexander-T-Moss/Small-Area-Flow-Comp).
