# min_skirt_length

> 所在界面：工艺设置 → Others → Skirt
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_skirt.md` 的「Minimum extrusion Length」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Minimum extrusion Length

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `min_skirt_length`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--min-skirt-length=1`.  
Minimum filament extrusion length in mm when printing the skirt. Zero means this feature is disabled.  
Using a non-zero value is useful if the printer is set up to print without a prime line.  
The final number of loops is not taken into account when arranging objects or validating the distance between them. Increase the number of loops in that case.
