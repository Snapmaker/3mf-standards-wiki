# pressure_advance

> 所在界面：耗材设置 → Filament → Flow ratio and Pressure Advance
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_flow_ratio_and_pressure_advance.md` 的「Pressure Advance」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：需先启用 Enable pressure advance 后显示
> 本小节同时涵盖：`enable_pressure_advance`（各另有独立文档）。

---

## Pressure Advance

[Modes](option_mode):  
`Simple` [Variable](built_in_placeholders_variables): `enable_pressure_advance`.  
`Advanced` [Variable](built_in_placeholders_variables): `pressure_advance`.  
[Type](option_type): `enable_pressure_advance` (Boolean list), `pressure_advance` (Float list).  
[CLI Example](cli_mode#setting-overrides): `--enable-pressure-advance=1` (`enable_pressure_advance` shown; other variables above follow their own type).  
Pressure advance [Klipper](https://www.klipper3d.org/Pressure_Advance.html) and [RepRap](https://docs.duet3d.com/User_manual/Tuning/Pressure_advance) AKA [Linear advance (Marlin)](https://marlinfw.org/docs/features/lin_advance.html) is a feature that compensates for the lag in filament pressure within the nozzle during acceleration and deceleration. It helps improve print quality by reducing issues like blobs, oozing, and inconsistent extrusion, especially at corners or during fast movements.

> [!NOTE]
> Auto calibration result will be overwritten once enabled

> [!TIP]
> Check the [Pressure Advance Calibration guide](pressure_advance_calib).
