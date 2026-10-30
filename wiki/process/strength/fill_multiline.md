# fill_multiline

> Location: Process → Strength → Infill

---

## Fill Multiline

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `fill_multiline`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--fill-multiline=1`.  
This setting allows the selected [infill pattern](#sparse-infill-pattern) to be generated using up to 10 parallel extrusion lines per path, while preserving both the defined [infill density](#sparse-infill-density) and the overall material usage.

To check which patterns support multiline infill, see the Patterns Quick Reference table in the [Infill Patterns Wiki List](../../process/strength/strength_settings_patterns_quick_reference.md) or each pattern's specifics in the [Patterns section](../../process/strength/strength_settings_patterns.md).

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
