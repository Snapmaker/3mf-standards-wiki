# symmetric_infill_y_axis

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_patterns.md` 的「Zig Zag」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

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
    - **[Multiline](strength_settings_infill#fill-multiline):** No
    - **[Symmetric infill Y axis](strength_settings_infill#symmetric-infill-y-axis):** Yes
    - **[Smooth Factor](strength_settings_infill#sparse-infill-smooth-factor):** No
- **Applies to:**
    - **[Sparse Infill](strength_settings_infill#sparse-infill-density)**

![infill-top-zig-zag](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/infill-top-zig-zag.png?raw=true)
