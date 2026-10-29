# lateral_lattice_angle_1

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_patterns.md` 的「Lateral Lattice」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`lateral_lattice_angle_2`（各另有独立文档）。

---

## Lateral Lattice

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `lateral_lattice_angle_1`, `lateral_lattice_angle_2`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--lateral-lattice-angle-1=1` (same pattern for the other variables above).  
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
    - **[Multiline](strength_settings_infill#fill-multiline):** [Classic](strength_settings_infill#classic-strategy)
        - **2 lines:** Print Time Low ![level-to-worse-2](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-2.svg?raw=true) (8% Faster over single line)
        - **3 lines:** Print Time Low ![level-to-worse-2](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-2.svg?raw=true) (10% Faster over single line)
    - **[Symmetric infill Y axis](strength_settings_infill#symmetric-infill-y-axis):** No
    - **[Smooth Factor](strength_settings_infill#sparse-infill-smooth-factor):** No
- **Applies to:**
    - **[Sparse Infill](strength_settings_infill#sparse-infill-density)**

![infill-top-lateral-lattice](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/infill-top-lateral-lattice.png?raw=true)
