# internal_solid_infill_speed

> Location: Process → Speed → Other layers speed

---

## Internal solid infill

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `internal_solid_infill_speed`.  
[Type](../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--internal-solid-infill-speed=1`.  
Speed of internal solid infill, which fills the interior of the model with solid layers.  
This is typically set faster than the [top surface speed](#top-surface) to optimize print time, while still ensuring adequate strength and layer adhesion. Adjusting this speed can help balance print quality and efficiency, especially for models requiring strong internal structures.  
Solid infill is also considered when [infill % is set to 100%](../../process/strength/strength_settings_infill.md#internal-solid-infill).
