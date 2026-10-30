# lateral_lattice_angle_1

> Location: Process → Strength → Infill
> 本小节同时涵盖：`lateral_lattice_angle_2`（各另有独立文档）。

---

## Lateral Lattice

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `lateral_lattice_angle_1`, `lateral_lattice_angle_2`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--lateral-lattice-angle-1=1` (same pattern for the other variables above).  
Low-strength pattern with good flexibility. You can adjust **Angle 1** and **Angle 2** to optimize the infill for your specific model. Each angle sets the tilt in the Z direction of one of the two sets of lattice elements. 0° is vertical.

- **Strength**
    - **Horizontal (X-Y):** Normal-Low ![level-to-better-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-3.svg?raw=true)
    - **Vertical (Z):** Low ![level-to-better-2](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-2.svg?raw=true)
- **Density Calculation:**  % of  total infill volume
    - **Material Usage:** Normal ![level-to-worse-4](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-4.svg?raw=true)
    - **Print Time:** Normal-Low ![level-to-worse-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-3.svg?raw=true)
        - **Material/Time (Higher better):** Normal-High ![level-to-better-5](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-5.svg?raw=true)
        - **Layer time Variability:** Unnoticeable
    - **Slicing Time:** Normal-Low ![level-to-worse-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-3.svg?raw=true)
    - **G-code Size:** Extra-Low ![level-to-worse-1](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-1.svg?raw=true)
- **Extra:**
    - **[Multiline](../../process/strength/strength_settings_infill.md#fill-multiline):** [Classic](../../process/strength/strength_settings_infill.md#classic-strategy)
        - **2 lines:** Print Time Low ![level-to-worse-2](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-2.svg?raw=true) (8% Faster over single line)
        - **3 lines:** Print Time Low ![level-to-worse-2](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-2.svg?raw=true) (10% Faster over single line)
    - **[Symmetric infill Y axis](../../process/strength/strength_settings_infill.md#symmetric-infill-y-axis):** No
    - **[Smooth Factor](../../process/strength/strength_settings_infill.md#sparse-infill-smooth-factor):** No
- **Applies to:**
    - **[Sparse Infill](../../process/strength/strength_settings_infill.md#sparse-infill-density)**

![infill-top-lateral-lattice](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/infill-top-lateral-lattice.png?raw=true)
