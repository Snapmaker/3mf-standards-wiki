# max_volumetric_extrusion_rate_slope_segment_length

> Location: Process → Speed → Advanced
> 本小节同时涵盖：`max_volumetric_extrusion_rate_slope`（各另有独立文档）。

---

# Speed Advanced - Extrusion Rate Smoothing

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `max_volumetric_extrusion_rate_slope`, `max_volumetric_extrusion_rate_slope_segment_length`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--max-volumetric-extrusion-rate-slope=1` (same pattern for the other variables above).  
Extrusion Rate Smoothing (ERS) (pressure equalizer in PrusaSlicer) aims to **limit the rate of extrusion volume change to be below a user-set threshold (the ERS value)**.  
It aims to assist the printer firmware's internal motion planner and pressure advance in achieving the desired nozzle flow and reducing deviations from the ideal flow.

This happens by reducing the stresses put on the extrusion system as well as reducing the absolute deviations from the ideal extrusion flow caused by pressure advance smooth time.

This feature is especially helpful when printing at high accelerations and large flow rates as the deviations are larger in these cases.

> [!NOTE]
> A value of 0 disables Extrusion rate smoothing. Any value greater than 0 turns off [Arc fitting](../../process/quality/quality_settings_precision.md#arc-fitting) and locks that option while smoothing is enabled.

![ers-intro](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/ERS/ers-intro.png?raw=true)

- [Theory](#theory)
    - [Acceleration vs. Extrusion rate smoothing](#acceleration-vs-extrusion-rate-smoothing)
    - [Pressure advance vs extrusion rate smoothing](#pressure-advance-vs-extrusion-rate-smoothing)
- [Finding the ideal Extrusion Rate smoothing value](#finding-the-ideal-extrusion-rate-smoothing-value)
- [A note for Bowden printers using Marlin without pressure advance](#a-note-for-bowden-printers-using-marlin-without-pressure-advance)
- [A note on ERS Segment length](#a-note-on-ers-segment-length)
- [Apply only on external features](#apply-only-on-external-features)
- [Limitations](#limitations)
- [Credits](#credits)
