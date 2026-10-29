# sparse_infill_density

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_infill.md` 的「Sparse infill density」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Sparse infill density

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `sparse_infill_density`.  
[Type](option_type#integer-float-percentage): `Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--sparse-infill-density=20%`.  
Infill density determines the amount of material used to fill the interior of a 3D print. It is usually expressed as a percentage, with 100% being completely solid.

- Higher density increases
    - Strength
    - Material usage
    - Print time.

> [!NOTE]
> Density is usually calculated as a percentage of the total infill volume, not the total print volume.  
> Nevertheless, **not all patterns interpret density the same way**, so the actual material usage may vary.  
> You can see each pattern's material usage in the [Patterns section](strength_settings_patterns).
