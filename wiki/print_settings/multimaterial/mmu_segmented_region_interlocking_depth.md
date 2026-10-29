# mmu_segmented_region_interlocking_depth

> 所在界面：工艺设置 → Multimaterial → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_advanced.md` 的「Interlocking depth of Segmented Region」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Interlocking depth of Segmented Region

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `mmu_segmented_region_interlocking_depth`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--mmu-segmented-region-interlocking-depth=1`.  
Interlocking depth of a segmented region. On every other layer, the painted region reaches only this deep into the model instead of the [Maximum Width of Segmented Region](#maximum-width-of-segmented-region), so consecutive layers interlock. Zero disables this feature. Hidden and ignored when [Interlocking Beam](#interlocking-beam) is enabled.
