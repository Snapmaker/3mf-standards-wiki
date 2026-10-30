# xy_contour_compensation

> Location: Process → Quality → Precision
> 本小节同时涵盖：`xy_hole_compensation`（各另有独立文档）。

---

## X-Y Compensation

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `xy_hole_compensation`, `xy_contour_compensation`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--xy-hole-compensation=1` (same pattern for the other variables above).  
Used to compensate the XY dimensions of the model.
With these options you can compensate material expansion or shrinkage, which can occur due to various factors such as the type of filament used, temperature fluctuations, or printer calibration issues.

> [!TIP]
> Follow the [Calibration Guide](../../guides/calibration_guide.md) and [Filament Tolerance Calibration](../../calibration/tolerance_calib.md) to determine the correct value for your printer and filament combination.
