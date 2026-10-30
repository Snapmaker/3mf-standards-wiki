# inner_wall_speed

> Location: Process → Speed → Other layers speed

---

## Inner wall

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `inner_wall_speed`.  
[Type](../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--inner-wall-speed=1`.  
Speed of the inner walls, which are printed faster than the outer wall to reduce print time. Their flow is still recommended to stay well below the [maximum volumetric speed](../../calibration/volumetric_speed_calib.md) to ensure good layer adhesion and reduce internal stresses in the material.
