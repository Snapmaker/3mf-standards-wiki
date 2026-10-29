# internal_solid_infill_acceleration

> 所在界面：工艺设置 → Speed → Acceleration
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_acceleration.md` 的「Internal solid infill」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Internal solid infill

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `internal_solid_infill_acceleration`.  
[Type](option_type#list-types): `Float or Percentage list`.  
[CLI Example](cli_mode#setting-overrides): `--internal-solid-infill-acceleration=20%`.  
Acceleration of [internal solid infill](speed_settings_other_layers_speed#internal-solid-infill). If the value is expressed as a percentage (e.g. 100%), it will be calculated based on the default acceleration.
