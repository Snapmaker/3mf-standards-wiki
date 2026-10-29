# change_extrusion_role_gcode

> 所在界面：打印机设置 → Machine G-code → Change extrusion role G-code
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/machine gcode/printer_machine_gcode.md` 的「Change extrusion role G-code」小节（2026-10-28），英文原文，待本地化校对。

---

## Change extrusion role G-code

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `change_extrusion_role_gcode`.  
[Type](option_type#text): `Text`.  
[CLI Example](cli_mode#setting-overrides): `--change-extrusion-role-gcode=value`.  
This G-code is inserted when the [extrusion role](built_in_placeholders_variables#extrusion-roles) is changed.
This is the Machine section of the feature "Change Extrusion Role G-code" that is also available in the [Material settings](material_advanced#change-extrusion-role-g-code) and [Process settings](others_settings_g_code_output#change-extrusion-role-g-code).

Example G-codes:

- Marlin g-code to set fan speed to 10% (S25 out of S255) for BridgeInfill role and 30% (S75 out of S255) for other roles:

  ```c++
  {if( extrusion_role == "BridgeInfill")}
  M106 S25
  {else}
  M106 S75
  {endif}
  ```
  
- Marlin G-code to set the fan speed to 0% for the ['Internal Sparse Infill' role](strength_settings_infill) and the first three layers, and to 30% `0.3*255` for the other roles. This achieves good layer adhesion while maintaining perimeter quality.:

  ```c++
  {if(extrusion_role)=="InternalInfill" || layer_num < 4 }
  M106 S0
  {else}
  M106 S{0.3*255}
  {endif}
  ```
  
- Marlin g-code to set pressure advance to 0 for ['Internal Sparse Infill' role](strength_settings_infill) and restore it to previous value for other roles:

  ```c++
  {if( extrusion_role == "InternalInfill")}
  M900 K0
  {else}
  M900 K{pressure_advance[0]}
  {endif}
  ```
