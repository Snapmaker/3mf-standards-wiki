# symmetric_infill_y_axis

> Location: Process → Strength → Infill

---

## Zig Zag

Similar to [rectilinear](#rectilinear), with a consistent pattern between layers.

- **Strength**
    - **Horizontal (X-Y):** Normal-Low ![level-to-better-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-3.svg?raw=true)
    - **Vertical (Z):** Low ![level-to-better-2](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-2.svg?raw=true)
- **Density Calculation:**  % of  total infill volume
    - **Material Usage:** Normal ![level-to-worse-4](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-4.svg?raw=true)
    - **Print Time:** Normal-Low ![level-to-worse-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-3.svg?raw=true)
        - **Material/Time (Higher better):** Normal-High ![level-to-better-5](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-5.svg?raw=true)
        - **Layer time Variability:** None
    - **Slicing Time:** Normal-Low ![level-to-worse-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-3.svg?raw=true)
    - **G-code Size:** Extra-Low ![level-to-worse-1](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-1.svg?raw=true)
- **Extra:**
    - **[Multiline](../../process/strength/strength_settings_infill.md#fill-multiline):** No
    - **[Symmetric infill Y axis](../../process/strength/strength_settings_infill.md#symmetric-infill-y-axis):** Yes
    - **[Smooth Factor](../../process/strength/strength_settings_infill.md#sparse-infill-smooth-factor):** No
- **Applies to:**
    - **[Sparse Infill](../../process/strength/strength_settings_infill.md#sparse-infill-density)**

![infill-top-zig-zag](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/infill-top-zig-zag.png?raw=true)
