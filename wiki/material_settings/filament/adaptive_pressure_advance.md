# adaptive_pressure_advance

> 所在界面：耗材设置 → Filament → Flow ratio and Pressure Advance
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_flow_ratio_and_pressure_advance.md` 的「Enable adaptive Pressure Advance (beta)」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Enable adaptive Pressure Advance (beta)

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `adaptive_pressure_advance`.  
[Type](option_type#list-types): `Boolean list`.  
[CLI Example](cli_mode#setting-overrides): `--adaptive-pressure-advance=1`.  
With increasing print speeds (and hence increasing volumetric flow through the nozzle) and increasing accelerations, it has been observed that the effective PA value typically decreases. This means that a single PA value is not always 100% optimal for all features and a compromise value is usually used that does not cause too much bulging on features with lower flow speed and accelerations while also not causing gaps on faster features.

This feature aims to address this limitation by modeling the response of your printer's extrusion system depending on the volumetric flow speed and acceleration it is printing at. Internally, it generates a fitted model that can extrapolate the needed pressure advance for any given volumetric flow speed and acceleration, which is then emitted to the printer depending on the current print conditions.

When enabled, the pressure advance value above is overridden. However, a reasonable default value above is strongly recommended to act as a fallback and for when tool changing.

> [!TIP]
> Check the [Adaptive Pressure Advance Calibration guide](adaptive_pressure_advance_calib).
