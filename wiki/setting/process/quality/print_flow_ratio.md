# print_flow_ratio

> Location: Process → Quality → Walls and surfaces
> 本小节同时涵盖：`top_solid_infill_flow_ratio`、`bottom_solid_infill_flow_ratio`（各另有独立文档）。

---

## Surface flow ratio

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `print_flow_ratio`, `top_solid_infill_flow_ratio`, `bottom_solid_infill_flow_ratio`, `set_other_flow_ratios`, `first_layer_flow_ratio`, `outer_wall_flow_ratio`, `inner_wall_flow_ratio`, `overhang_flow_ratio`, `sparse_infill_flow_ratio`, `internal_solid_infill_flow_ratio`, `gap_fill_flow_ratio`, `support_flow_ratio`, `support_interface_flow_ratio`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float` — every variable above except `set_other_flow_ratios`, which is a [Boolean](../../../general_settings/option_type.md#boolean) enable toggle for all the others (`--set-other-flow-ratios=1`).  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--print-flow-ratio=1` (same pattern for the other Float variables above).  
The Flow ratio (`print_flow_ratio`) scales all extrusion flow of the object proportionally.

The top and bottom surface flow ratios affect the amount of material for [top or bottom solid infill](../../process/strength/strength_settings_top_bottom_shells.md). You can decrease them slightly to get a smoother surface finish.  
The actual top or bottom surface flow used is calculated by multiplying this value by the [filament flow ratio](../../filament/filament/material_flow_ratio_and_pressure_advance.md#flow-ratio), and if set, the object's flow ratio.

Other flow ratios, such as ratios for the first layer (does not affect brims and skirts), outer and inner walls, overhang perimeters, sparse infill, internal solid infill, gap fill, support, and support interfaces, can also be adjusted after enabling the "Set other flow ratios" option.

> [!TIP]
> Before using a value other than 1, it is recommended to [calibrate the flow ratio](../../../calibration/flow_ratio_calib.md) to ensure that the flow ratio is set correctly for your printer and filament.
