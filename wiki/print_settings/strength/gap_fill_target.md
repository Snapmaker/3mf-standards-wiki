# gap_fill_target

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_infill.md` 的「Apply gap fill」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Apply gap fill

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `gap_fill_target`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `everywhere, topbottom, nowhere`.  
[CLI Example](cli_mode#setting-overrides): `--gap-fill-target=everywhere`.  
Enables gap fill for the selected solid surfaces.  
The minimum gap length that will be filled can be controlled with the [Filter out tiny gaps](#filter-out-tiny-gaps) option.

1. **Everywhere:** Applies gap fill to top, bottom and internal solid surfaces for maximum strength.
2. **Top and bottom surfaces:** Applies gap fill to top and bottom surfaces only, balancing print speed, reducing potential over-extrusion in the solid infill and making sure the top and bottom surfaces have no pinhole gaps.
3. **Nowhere:** Disables gap fill for all solid infill areas.

Note that if using the [classic perimeter generator](quality_settings_wall_generator#classic), gap fill may also be generated between perimeters, if a full width line cannot fit between them.
That perimeter gap fill is not controlled by this setting.

If you would like all gap fill, including the classic perimeter generated one, removed, set the Filter out tiny gaps value to a large number, like 999999.

However, this is not advised, as gap fill between perimeters contributes to the model's strength. For models where excessive gap fill is generated between perimeters, a better option would be to switch to the [Arachne wall generator](quality_settings_wall_generator#arachne) and use this option to control whether the cosmetic top and bottom surface gap fill is generated.
