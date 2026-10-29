# seam_slope_conditional

> 所在界面：工艺设置 → Quality → Seam
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_seam.md` 的「Scarf joint seam」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`seam_slope_type`、`scarf_angle_threshold`、`scarf_overhang_threshold`、`scarf_joint_speed`、`seam_slope_start_height`、`seam_slope_entire_loop`、`seam_slope_min_length`、`seam_slope_steps`、`scarf_joint_flow_ratio`、`seam_slope_inner_walls`（各另有独立文档）。

---

### Scarf joint seam

[Modes](option_mode):  
`Advanced` [Variables](built_in_placeholders_variables): `seam_slope_type`, `seam_slope_conditional`, `scarf_angle_threshold`, `scarf_overhang_threshold`, `scarf_joint_speed`, `seam_slope_start_height`, `seam_slope_entire_loop`, `seam_slope_min_length`, `seam_slope_steps`, `seam_slope_inner_walls`.  
`Expert` [Variable](built_in_placeholders_variables): `scarf_joint_flow_ratio`.  
Adjusts the extrusion flow rate at seam points to create a smooth overlap between the start and end of each loop, minimizing visible defects.

![scarf-joint-seam](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/seam/scarf-joint-seam.png?raw=true)

Advantages:

- Reduces visible z-seams
- Improves cosmetic quality of curved surfaces
- Can slightly improve part strength at seams by softening transitions

Disadvantages:

- May increase print time slightly
- Less effective on sharp corners and overhangs
- Requires tuning of parameters like length, speed, and flow for best results

Scarf joints are never applied on the first layer, in [spiral vase](others_settings_special_mode#spiral-vase) mode, or on [belt printers](belt_printing#features-that-are-not-available).

> [!NOTE]
> Read more here: [Better Seams - An OrcaSlicer Guide](https://www.printables.com/model/783313-better-seams-an-orca-slicer-guide-to-using-scarf-s).
