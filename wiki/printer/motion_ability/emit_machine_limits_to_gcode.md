# emit_machine_limits_to_gcode

> Location: Printer → Motion ability → Advanced

---

## Emit limits to G-code

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `emit_machine_limits_to_gcode`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--emit-machine-limits-to-gcode=1`.  
If enabled, the machine limits will be emitted to G-code file.
This option will be ignored if the G-code flavor is set to Klipper.
