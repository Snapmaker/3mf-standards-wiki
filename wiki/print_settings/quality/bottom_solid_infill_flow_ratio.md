# bottom_solid_infill_flow_ratio

> 所在界面：工艺设置 → Quality → Walls and surfaces
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_wall_and_surfaces.md` 的「Surface flow ratio」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`print_flow_ratio`、`top_solid_infill_flow_ratio`（各另有独立文档）。

---

## Surface flow ratio

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `print_flow_ratio`, `top_solid_infill_flow_ratio`, `bottom_solid_infill_flow_ratio`, `set_other_flow_ratios`, `first_layer_flow_ratio`, `outer_wall_flow_ratio`, `inner_wall_flow_ratio`, `overhang_flow_ratio`, `sparse_infill_flow_ratio`, `internal_solid_infill_flow_ratio`, `gap_fill_flow_ratio`, `support_flow_ratio`, `support_interface_flow_ratio`.  
[Type](option_type#integer-float-percentage): `Float` — every variable above except `set_other_flow_ratios`, which is a [Boolean](option_type#boolean) enable toggle for all the others (`--set-other-flow-ratios=1`).  
[CLI Example](cli_mode#setting-overrides): `--print-flow-ratio=1` (same pattern for the other Float variables above).  
The Flow ratio (`print_flow_ratio`) scales all extrusion flow of the object proportionally.

The top and bottom surface flow ratios affect the amount of material for [top or bottom solid infill](strength_settings_top_bottom_shells). You can decrease them slightly to get a smoother surface finish.  
The actual top or bottom surface flow used is calculated by multiplying this value by the [filament flow ratio](material_flow_ratio_and_pressure_advance#flow-ratio), and if set, the object's flow ratio.

Other flow ratios, such as ratios for the first layer (does not affect brims and skirts), outer and inner walls, overhang perimeters, sparse infill, internal solid infill, gap fill, support, and support interfaces, can also be adjusted after enabling the "Set other flow ratios" option.

> [!TIP]
> Before using a value other than 1, it is recommended to [calibrate the flow ratio](flow_ratio_calib) to ensure that the flow ratio is set correctly for your printer and filament.
