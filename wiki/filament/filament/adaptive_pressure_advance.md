# adaptive_pressure_advance

> Location: Filament → Filament → Flow ratio and Pressure Advance

---

### Enable adaptive Pressure Advance (beta)

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `adaptive_pressure_advance`.  
[Type](../../general_settings/option_type.md#list-types): `Boolean list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--adaptive-pressure-advance=1`.  
With increasing print speeds (and hence increasing volumetric flow through the nozzle) and increasing accelerations, it has been observed that the effective PA value typically decreases. This means that a single PA value is not always 100% optimal for all features and a compromise value is usually used that does not cause too much bulging on features with lower flow speed and accelerations while also not causing gaps on faster features.

This feature aims to address this limitation by modeling the response of your printer's extrusion system depending on the volumetric flow speed and acceleration it is printing at. Internally, it generates a fitted model that can extrapolate the needed pressure advance for any given volumetric flow speed and acceleration, which is then emitted to the printer depending on the current print conditions.

When enabled, the pressure advance value above is overridden. However, a reasonable default value above is strongly recommended to act as a fallback and for when tool changing.

> [!TIP]
> Check the [Adaptive Pressure Advance Calibration guide](../../calibration/adaptive_pressure_advance_calib.md).
