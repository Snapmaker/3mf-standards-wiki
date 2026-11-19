# symmetric_infill_y_axis

> Location: Process → Strength → Infill

---

## Zig Zag

Similar to [rectilinear](#rectilinear), with a consistent pattern between layers.

- **Strength**
    - **Horizontal (X-Y):** Normal-Low ![level-to-better-3](../../../images/misc/level-to-better-3.svg)
    - **Vertical (Z):** Low ![level-to-better-2](../../../images/misc/level-to-better-2.svg)
- **Density Calculation:**  % of  total infill volume
    - **Material Usage:** Normal ![level-to-worse-4](../../../images/misc/level-to-worse-4.svg)
    - **Print Time:** Normal-Low ![level-to-worse-3](../../../images/misc/level-to-worse-3.svg)
        - **Material/Time (Higher better):** Normal-High ![level-to-better-5](../../../images/misc/level-to-better-5.svg)
        - **Layer time Variability:** None
    - **Slicing Time:** Normal-Low ![level-to-worse-3](../../../images/misc/level-to-worse-3.svg)
    - **G-code Size:** Extra-Low ![level-to-worse-1](../../../images/misc/level-to-worse-1.svg)
- **Extra:**
    - **[Multiline](../../process/strength/fill_multiline.md):** No
    - **[Symmetric infill Y axis](../../process/strength/symmetric_infill_y_axis.md):** Yes
    - **[Smooth Factor](../../process/strength/sparse_infill_pattern.md):** No
- **Applies to:**
    - **[Sparse Infill](../../process/strength/sparse_infill_density.md)**

![infill-top-zig-zag](../../../images/fill/infill-top-zig-zag.png)
