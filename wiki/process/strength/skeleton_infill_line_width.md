# skeleton_infill_line_width

> Location: Process → Strength → Infill
> 本小节同时涵盖：`skin_infill_density`、`skeleton_infill_density`、`infill_lock_depth`、`skin_infill_depth`、`skin_infill_line_width`（各另有独立文档）。

---

## Locked Zag

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `skin_infill_density`, `skeleton_infill_density`, `infill_lock_depth`, `skin_infill_depth`, `skin_infill_line_width`, `skeleton_infill_line_width`.  
[Type](../../general_settings/option_type.md): `skin_infill_density` (Percentage), `skeleton_infill_density` (Percentage), `infill_lock_depth` (Float), `skin_infill_depth` (Float), `skin_infill_line_width` (Float or Percentage), `skeleton_infill_line_width` (Float or Percentage).  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--skin-infill-density=20%` (`skin_infill_density` shown; other variables above follow their own type).  
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
    - **[Multiline](../../process/strength/strength_settings_infill.md#fill-multiline):** No
    - **[Symmetric infill Y axis](../../process/strength/strength_settings_infill.md#symmetric-infill-y-axis):** Yes
    - **[Smooth Factor](../../process/strength/strength_settings_infill.md#sparse-infill-smooth-factor):** No
- **Applies to:**
    - **[Sparse Infill](../../process/strength/strength_settings_infill.md#sparse-infill-density)**

![infill-top-locked-zag](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/infill-top-locked-zag.png?raw=true)
