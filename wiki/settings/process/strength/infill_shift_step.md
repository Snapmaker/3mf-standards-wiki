# infill_shift_step

> Location: Process → Strength → Infill

---

## Cross Hatch

Similar to [Gyroid](#gyroid) but with linear patterns, creating weak points at internal corners.
Easier to slice but consider using [TPMS-D](#tpms-d) or [Gyroid](#gyroid) for better strength and flexibility.

- **Strength**
    - **Horizontal (X-Y):** Normal-High ![level-to-better-5](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-5.svg?raw=true)
    - **Vertical (Z):** Normal-High ![level-to-better-5](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-5.svg?raw=true)
- **Density Calculation:**  % of  total infill volume
    - **Material Usage:** Normal ![level-to-worse-4](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-4.svg?raw=true)
    - **Print Time:** Normal-High ![level-to-worse-5](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-5.svg?raw=true)
        - **Material/Time (Higher better):** Normal-Low ![level-to-better-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-better-3.svg?raw=true)
        - **Layer time Variability:** Likely Noticeable
    - **Slicing Time:** Normal ![level-to-worse-4](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-4.svg?raw=true)
    - **G-code Size:** Normal ![level-to-worse-4](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-4.svg?raw=true)
- **Extra:**
    - **[Multiline](../../process/strength/fill_multiline.md):** [Classic](../../process/strength/sparse_infill_pattern.md)
        - **2 lines:** Print Time Normal ![level-to-worse-4](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-4.svg?raw=true) (12% Faster over single line)
        - **3 lines:** Print Time Normal-Low ![level-to-worse-3](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/misc/level-to-worse-3.svg?raw=true) (18% Faster over single line)
    - **[Symmetric infill Y axis](../../process/strength/symmetric_infill_y_axis.md):** No
    - **[Smooth Factor](../../process/strength/sparse_infill_pattern.md):** Yes
- **Applies to:**
    - **[Sparse Infill](../../process/strength/sparse_infill_density.md)**

![infill-top-cross-hatch](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/infill-top-cross-hatch.png?raw=true)
