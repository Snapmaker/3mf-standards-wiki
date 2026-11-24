# seam_slope_entire_loop

> Location: Process → Quality → Seam → Scarf around entire wall
> Also in this section: `seam_slope_type`, `seam_slope_conditional`, `scarf_angle_threshold`, `scarf_overhang_threshold`, `scarf_joint_speed`, `seam_slope_start_height`, `seam_slope_min_length`, `seam_slope_steps`, `scarf_joint_flow_ratio`, `seam_slope_inner_walls` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `seam_slope_entire_loop`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `false`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--seam-slope-entire-loop=1`.  

The scarf extends to the entire length of the wall.

### Scarf joint seam

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `seam_slope_entire_loop`.  

Adjusts the extrusion flow rate at seam points to create a smooth overlap between the start and end of each loop, minimizing visible defects.

![scarf-joint-seam](../../../images/seam/scarf-joint-seam.png)

Advantages:

- Reduces visible z-seams
- Improves cosmetic quality of curved surfaces
- Can slightly improve part strength at seams by softening transitions

Disadvantages:

- May increase print time slightly
- Less effective on sharp corners and overhangs
- Requires tuning of parameters like length, speed, and flow for best results

Scarf joints are never applied on the first layer, in [spiral vase](../../process/others/spiral_mode.md) mode, or on belt printers.

> [!NOTE]
> Read more here: [Better Seams - An OrcaSlicer Guide](https://www.printables.com/model/783313-better-seams-an-orca-slicer-guide-to-using-scarf-s).
