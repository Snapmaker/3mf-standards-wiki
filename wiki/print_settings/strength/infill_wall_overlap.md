# infill_wall_overlap

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_infill.md` 的「Infill Wall Overlap」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Infill Wall Overlap

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `infill_wall_overlap`.  
[Type](option_type#integer-float-percentage): `Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--infill-wall-overlap=20%`.  
Infill area is enlarged slightly to overlap with wall for better bonding. The percentage value is approximately relative to the inner wall line width. More precisely, it is relative to half the inner wall line spacing plus half the internal solid infill line spacing with the [Classic](quality_settings_wall_generator#classic) wall generator, and to the inner wall line spacing with [Arachne](quality_settings_wall_generator#arachne) (the outer wall line spacing in both cases where only one wall is printed). Set this value to ~10-15% to minimize potential over-extrusion and accumulation of material resulting in rough surfaces.

- **Infill Wall Overlap Off**

![InfillWallOverlapOff](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/InfillWallOverlapOff.svg?raw=true)

- **Infill Wall Overlap On**

![InfillWallOverlapOn](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/InfillWallOverlapOn.svg?raw=true)
