# change_extrusion_role_gcode

> Location: Printer → Machine G-code → Change extrusion role G-code

---

## Change extrusion role G-code

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `change_extrusion_role_gcode`.  
[Type](../../general_settings/option_type.md#text): `Text`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--change-extrusion-role-gcode=value`.  
This G-code is inserted when the [extrusion role](../../developer_reference/built_in_placeholders_variables.md#extrusion-roles) is changed.
This is the Machine section of the feature "Change Extrusion Role G-code" that is also available in the [Material settings](../../filament/advanced/material_advanced.md#change-extrusion-role-g-code) and [Process settings](../../process/others/others_settings_g_code_output.md#change-extrusion-role-g-code).

Example G-codes:

- Marlin g-code to set fan speed to 10% (S25 out of S255) for BridgeInfill role and 30% (S75 out of S255) for other roles:

  ```c++
  {if( extrusion_role == "BridgeInfill")}
  M106 S25
  {else}
  M106 S75
  {endif}
  ```
  
- Marlin G-code to set the fan speed to 0% for the ['Internal Sparse Infill' role](../../process/strength/strength_settings_infill.md) and the first three layers, and to 30% `0.3*255` for the other roles. This achieves good layer adhesion while maintaining perimeter quality.:

  ```c++
  {if(extrusion_role)=="InternalInfill" || layer_num < 4 }
  M106 S0
  {else}
  M106 S{0.3*255}
  {endif}
  ```
  
- Marlin g-code to set pressure advance to 0 for ['Internal Sparse Infill' role](../../process/strength/strength_settings_infill.md) and restore it to previous value for other roles:

  ```c++
  {if( extrusion_role == "InternalInfill")}
  M900 K0
  {else}
  M900 K{pressure_advance[0]}
  {endif}
  ```
