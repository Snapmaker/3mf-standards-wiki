# small_area_infill_flow_compensation

> Location: Process → Quality → Walls and surfaces
> 本小节同时涵盖：`small_area_infill_flow_compensation_model`（各另有独立文档）。

---

## Small area flow compensation

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `small_area_infill_flow_compensation`, `small_area_infill_flow_compensation_model`.  
[Type](../../general_settings/option_type.md): `small_area_infill_flow_compensation` (Boolean), `small_area_infill_flow_compensation_model` (Text list).  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--small-area-infill-flow-compensation=1` (`small_area_infill_flow_compensation` shown; other variables above follow their own type).  
Enables adaptive flow control for small infill areas.
This feature helps address extrusion problems that often occur in small regions of solid infill, such as the tops of narrow letters or fine features.  
In these cases, standard extrusion flow may be too much for the available space, leading to over-extrusion or poor surface quality.

![flow-compensation-model](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/flow-compensation-model.png?raw=true)

It works by dynamically adjusting the extrusion flow based on the length of the extrusion path, ensuring more precise material deposition in small spaces.

The compensation only applies to internal solid infill, top surfaces and first layer bottom surfaces, and only when that surface uses the [Rectilinear](../../process/strength/strength_settings_patterns.md#rectilinear), [Aligned Rectilinear](../../process/strength/strength_settings_patterns.md#aligned-rectilinear), [Monotonic](../../process/strength/strength_settings_patterns.md#monotonic) or [Monotonic line](../../process/strength/strength_settings_patterns.md#monotonic-line) pattern.

This is a native implementation of @Alexander-T-Moss's [Small Area Flow Compensation](https://github.com/Alexander-T-Moss/Small-Area-Flow-Comp).
