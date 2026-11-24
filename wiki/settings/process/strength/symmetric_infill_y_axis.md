# symmetric_infill_y_axis

> Location: Process → Strength → Infill → Symmetric infill Y axis

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `symmetric_infill_y_axis`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `false`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--symmetric-infill-y-axis=1`.  

If the model has two parts that are symmetric about the Y axis, and you want these parts to have symmetric textures, please click this option on one of the parts.

## Zig Zag

Similar to rectilinear, with a consistent pattern between layers.

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
