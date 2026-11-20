# xy_contour_compensation

> Location: Process → Quality → Precision
> Also in this section: `xy_hole_compensation` (each documented on its own page).

---

## X-Y Compensation

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `xy_contour_compensation`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[Unit](../../../general_settings/option_type.md#unit): `mm`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--xy-contour-compensation=1`.  

Used to compensate the XY dimensions of the model.
With these options you can compensate material expansion or shrinkage, which can occur due to various factors such as the type of filament used, temperature fluctuations, or printer calibration issues.

> [!TIP]
> Follow the [Calibration Guide](../../../guides/calibration_guide.md) and [Filament Tolerance Calibration](../../../calibration/tolerance_calib.md) to determine the correct value for your printer and filament combination.
