# min_skirt_length

> Location: Process → Others → Skirt

---

## Minimum extrusion Length

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `min_skirt_length`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--min-skirt-length=1`.  
Minimum filament extrusion length in mm when printing the skirt. Zero means this feature is disabled.  
Using a non-zero value is useful if the printer is set up to print without a prime line.  
The final number of loops is not taken into account when arranging objects or validating the distance between them. Increase the number of loops in that case.
