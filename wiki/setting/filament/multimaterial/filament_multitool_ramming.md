# filament_multitool_ramming

> Location: Filament → Multimaterial → Tool change parameters with multi extruder MM printers

---

## Tool change parameters with multi extruder

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `filament_multitool_ramming`.  
[Type](../../../general_settings/option_type.md#list-types): `Boolean list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--filament-multitool-ramming=1`.  
These options apply to printers that use multiple independent extruders or hotends (multi-tool setups). When enabled, ramming and related parameters define a small, controlled extrusion on the wipe tower immediately before a tool change to ensure the outgoing tool is cleared and the incoming tool begins with consistent filament at the nozzle. Use these settings to tune multi-tool handoffs and avoid color or material mixing.
