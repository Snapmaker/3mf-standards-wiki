# ironing_speed

> 所在界面：工艺设置 → Speed → Other layers speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_other_layers_speed.md` 的「Ironing speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Ironing speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `ironing_speed`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--ironing-speed=1`.  
[Ironing](quality_settings_ironing) and [Support Ironing](support_settings_ironing) speed, typically slower than the top surface speed to ensure a smooth finish.  
Each filament can replace this speed with its own Ironing speed in its [setting overrides](material_setting_overrides#ironing).
