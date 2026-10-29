# mmu_segmented_region_max_width

> 所在界面：工艺设置 → Multimaterial → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_advanced.md` 的「Maximum Width of Segmented Region」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Maximum Width of Segmented Region

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `mmu_segmented_region_max_width`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--mmu-segmented-region-max-width=1`.  
Maximum width of a segmented region. Zero disables this feature. Ignored when [Interlocking Beam](#interlocking-beam) is enabled.
