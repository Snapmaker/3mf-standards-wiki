# fill_multiline

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_infill.md` 的「Fill Multiline」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Fill Multiline

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `fill_multiline`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--fill-multiline=1`.  
This setting allows the selected [infill pattern](#sparse-infill-pattern) to be generated using up to 10 parallel extrusion lines per path, while preserving both the defined [infill density](#sparse-infill-density) and the overall material usage.

To check which patterns support multiline infill, see the Patterns Quick Reference table in the [Infill Patterns Wiki List](strength_settings_patterns_quick_reference) or each pattern's specifics in the [Patterns section](strength_settings_patterns).

![multiline-infill](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/multiline-infill.png?raw=true)

> [!NOTE]
> Orca's approach is different from other slicers that simply multiply the number of lines and material usage, generating a denser infill than expected.  
> Orca Slicer keeps the cross-section constant for the set density.
>
>| Infill   Density % | Infill Lines | Orca Density | Other Slicers Density |
>|--------------------|--------------|--------------|-----------------------|
>| 10%                | 2            | 10%          | 20%                   |
>| 25%                | 2            | 25%          | 50%                   |
>| 40%                | 2            | 40%          | 80%                   |
>| 10%                | 3            | 10%          | 30%                   |
>| 25%                | 3            | 25%          | 75%                   |
>| 40%                | 3            | 40%          | 100%                  |
>| 10%                | 5            | 10%          | 50%                   |
>| 25%                | 5            | 25%          | 100%                  |
>| 40%                | 5            | 40%          | 100%                  |
