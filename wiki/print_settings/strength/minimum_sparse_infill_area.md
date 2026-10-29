# minimum_sparse_infill_area

> 所在界面：工艺设置 → Strength → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_advanced.md` 的「Minimum sparse infill threshold」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Minimum sparse infill threshold

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `minimum_sparse_infill_area`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--minimum-sparse-infill-area=1`.  
Sparse infill areas smaller than the threshold value (in mm²) are replaced by [internal solid infill](strength_settings_infill#internal-solid-infill).
This setting helps to ensure that small areas of sparse infill do not compromise the strength of the print. It is particularly useful for models with intricate designs or small features where sparse infill may not provide sufficient support.
