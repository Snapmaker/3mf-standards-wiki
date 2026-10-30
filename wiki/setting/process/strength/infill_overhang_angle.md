# infill_overhang_angle

> Location: Process → Strength → Infill

---

## Lateral Honeycomb

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `infill_overhang_angle`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--infill-overhang-angle=1`.  
Vertical honeycomb pattern with acceptable torsional stiffness, developed for low-density structures like wings. An improvement over [Lateral Lattice](#lateral-lattice), it offers the same performance at lower densities. This infill includes an **Infill overhang angle** parameter to improve the contact between layers and reduce the risk of delamination.

- **Strength**
    - **Horizontal (X-Y):** Normal-Low ![level-to-better-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-3.svg?raw=true)
    - **Vertical (Z):** Normal-Low ![level-to-better-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-3.svg?raw=true)
- **Density Calculation:**  % of  total infill volume
    - **Material Usage:** Normal ![level-to-worse-4](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-4.svg?raw=true)
    - **Print Time:** Normal-Low ![level-to-worse-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-3.svg?raw=true)
        - **Material/Time (Higher better):** Normal-High ![level-to-better-5](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-5.svg?raw=true)
        - **Layer time Variability:** Possibly Noticeable
    - **Slicing Time:** Normal-Low ![level-to-worse-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-3.svg?raw=true)
    - **G-code Size:** Extra-Low ![level-to-worse-1](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-1.svg?raw=true)
- **Extra:**
    - **[Multiline](../../process/strength/strength_settings_infill.md#fill-multiline):** [Classic](../../process/strength/strength_settings_infill.md#classic-strategy)
        - **2 lines:** Print Time Low ![level-to-worse-2](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-2.svg?raw=true) (7% Faster over single line)
        - **3 lines:** Print Time Low ![level-to-worse-2](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-2.svg?raw=true) (10% Faster over single line)
    - **[Symmetric infill Y axis](../../process/strength/strength_settings_infill.md#symmetric-infill-y-axis):** No
    - **[Smooth Factor](../../process/strength/strength_settings_infill.md#sparse-infill-smooth-factor):** No
- **Applies to:**
    - **[Sparse Infill](../../process/strength/strength_settings_infill.md#sparse-infill-density)**

![infill-top-lateral-honeycomb](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/infill-top-lateral-honeycomb.png?raw=true)
