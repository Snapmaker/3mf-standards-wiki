# seam_gap

> Location: Process → Quality → Seam

---

### Seam gap

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `seam_gap`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float or Percentage`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--seam-gap=20%`.  
Controls the gap in mm or as a percentage of the nozzle size between the two ends of a loop starting and ending with a seam.

- A larger gap will reduce the bulging seen at the seam.
- A smaller gap reduces the visual appearance of a seam.

For a well-tuned printer with [pressure advance](../../../calibration/pressure_advance_calib.md) and [filament retraction](../../../calibration/retraction_calib.md), a value of **0-15%** is typically optimal.

![seam-gap](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/seam/seam-gap.gif?raw=true)
