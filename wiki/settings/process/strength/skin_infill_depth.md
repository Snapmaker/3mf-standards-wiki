# skin_infill_depth

> Location: Process → Strength → Infill
> Also in this section: `skin_infill_density`, `skeleton_infill_density`, `infill_lock_depth`, `skin_infill_line_width`, `skeleton_infill_line_width` (each documented on its own page).

---

## Locked Zag

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `skin_infill_depth`.  
[Type](../../../general_settings/option_type.md): Float.  
[Default](../../../general_settings/option_type.md#default-value): `2.0`.  
[Range](../../../general_settings/option_type.md#range): `0–100` mm.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--skin-infill-depth=1`.  
Version of [Zig Zag](#zig-zag) that adds extra skin.
When using this fill, you can individually modify the density of the skeleton and skin, as well as the size of the skin and how much interconnection there is between the skin and the skeleton (a lock depth of 50% of the skin depth is recommended).  
**Skin line width** and **Skeleton line width** set the line width of the skin and skeleton paths. If expressed as a %, they are computed over the nozzle diameter.  
The **Infill shift step** of [Cross Zag](#cross-zag) also applies to Locked Zag, but it only shifts the skin. The skeleton is not shifted.

- **Strength**
    - **Horizontal (X-Y):** Normal-Low ![level-to-better-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-3.svg?raw=true)
    - **Vertical (Z):** Normal-Low ![level-to-better-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-3.svg?raw=true)
- **Density Calculation:** Similar to [Zig Zag](#zig-zag).
Skeleton density * (Infill area - Skin area + Lock depth area) + (Skin density * Skin area).
    - **Material Usage:** Ultra-High ![level-to-worse-8](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-8.svg?raw=true)
    - **Print Time:** Extra-High ![level-to-worse-7](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-7.svg?raw=true)
        - **Material/Time (Higher better):** Normal ![level-to-better-4](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-4.svg?raw=true)
        - **Layer time Variability:** None
    - **Slicing Time:** Normal ![level-to-worse-4](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-4.svg?raw=true)
    - **G-code Size:** Normal-High ![level-to-worse-5](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-5.svg?raw=true)
- **Extra:**
    - **[Multiline](../../process/strength/fill_multiline.md):** No
    - **[Symmetric infill Y axis](../../process/strength/symmetric_infill_y_axis.md):** Yes
    - **[Smooth Factor](../../process/strength/sparse_infill_pattern.md):** No
- **Applies to:**
    - **[Sparse Infill](../../process/strength/sparse_infill_density.md)**

![infill-top-locked-zag](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/infill-top-locked-zag.png?raw=true)
