# pressure_advance

> Location: Filament → Filament → Flow ratio and Pressure Advance
> 显隐条件（初步梳理，待校对）：需先启用 Enable pressure advance 后显示
> 本小节同时涵盖：`enable_pressure_advance`（各另有独立文档）。

---

## Pressure Advance

[Modes](../../general_settings/option_mode.md):  
`Simple` [Variable](../../developer_reference/built_in_placeholders_variables.md): `enable_pressure_advance`.  
`Advanced` [Variable](../../developer_reference/built_in_placeholders_variables.md): `pressure_advance`.  
[Type](../../general_settings/option_type.md): `enable_pressure_advance` (Boolean list), `pressure_advance` (Float list).  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--enable-pressure-advance=1` (`enable_pressure_advance` shown; other variables above follow their own type).  
Pressure advance [Klipper](https://www.klipper3d.org/Pressure_Advance.html) and [RepRap](https://docs.duet3d.com/User_manual/Tuning/Pressure_advance) AKA [Linear advance (Marlin)](https://marlinfw.org/docs/features/lin_advance.html) is a feature that compensates for the lag in filament pressure within the nozzle during acceleration and deceleration. It helps improve print quality by reducing issues like blobs, oozing, and inconsistent extrusion, especially at corners or during fast movements.

> [!NOTE]
> Auto calibration result will be overwritten once enabled

> [!TIP]
> Check the [Pressure Advance Calibration guide](../../calibration/pressure_advance_calib.md).
