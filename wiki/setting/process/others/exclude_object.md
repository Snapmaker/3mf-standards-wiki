# exclude_object

> Location: Process → Others → G-code output

---

## Exclude Objects

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `exclude_object`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--exclude-object=1`.  
Add commands to the G-code that define each object and mark where it starts and ends, so the printer firmware can skip (cancel) individual objects during the print: `EXCLUDE_OBJECT_DEFINE`, `EXCLUDE_OBJECT_START` and `EXCLUDE_OBJECT_END` for Klipper, and `M486` for Marlin and RepRapFirmware.
