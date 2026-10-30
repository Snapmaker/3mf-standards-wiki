# filament_stamping_distance

> Location: Filament → Multimaterial → Tool change parameters with single extruder MM printers

---

### Stamping distance

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `filament_stamping_distance`.  
[Type](../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--filament-stamping-distance=1`.  
Stamping distance measured from the center of the cooling tube.
If set to non-zero value, filament is moved toward the nozzle between the individual cooling moves ("stamping"). This option configures how long this movement should be before the filament is retracted again.
