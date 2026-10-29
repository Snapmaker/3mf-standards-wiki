# xy_hole_compensation

> 所在界面：工艺设置 → Quality → Precision
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_precision.md` 的「X-Y Compensation」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`xy_contour_compensation`（各另有独立文档）。

---

## X-Y Compensation

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `xy_hole_compensation`, `xy_contour_compensation`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--xy-hole-compensation=1` (same pattern for the other variables above).  
Used to compensate the XY dimensions of the model.
With these options you can compensate material expansion or shrinkage, which can occur due to various factors such as the type of filament used, temperature fluctuations, or printer calibration issues.

> [!TIP]
> Follow the [Calibration Guide](calibration_guide) and [Filament Tolerance Calibration](tolerance_calib) to determine the correct value for your printer and filament combination.
