# filament_flow_ratio

> 所在界面：耗材设置 → Filament → Flow ratio and Pressure Advance
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_flow_ratio_and_pressure_advance.md` 的「Flow Ratio」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Flow Ratio

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filament_flow_ratio`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--filament-flow-ratio=1`.  
The material may have volumetric change after switching between molten and crystalline states. This setting changes all extrusion flow of this filament in G-code proportionally.  
The recommended value range is between 0.95 and 1.05. You may be able to tune this value to get a nice flat surface if there is slight overflow or underflow.  
The final object flow ratio is this value multiplied by the [filament flow ratio](material_flow_ratio_and_pressure_advance#flow-ratio).

> [!TIP]
> Check the [Flow Ratio Calibration guide](flow_ratio_calib).
