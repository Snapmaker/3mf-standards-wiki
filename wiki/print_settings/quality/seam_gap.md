# seam_gap

> 所在界面：工艺设置 → Quality → Seam
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_seam.md` 的「Seam gap」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Seam gap

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `seam_gap`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--seam-gap=20%`.  
Controls the gap in mm or as a percentage of the nozzle size between the two ends of a loop starting and ending with a seam.

- A larger gap will reduce the bulging seen at the seam.
- A smaller gap reduces the visual appearance of a seam.

For a well-tuned printer with [pressure advance](pressure_advance_calib) and [filament retraction](retraction_calib), a value of **0-15%** is typically optimal.

![seam-gap](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/seam/seam-gap.gif?raw=true)
