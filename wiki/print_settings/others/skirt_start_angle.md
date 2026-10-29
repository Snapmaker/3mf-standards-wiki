# skirt_start_angle

> 所在界面：工艺设置 → Others → Skirt
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_skirt.md` 的「Start point」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Start point

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `skirt_start_angle`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--skirt-start-angle=1`.  
Start angle for the skirt relative to the object center. 0° is the right-most position (along the +X axis), angles increase counter-clockwise.  
Use this to control where the skirt begins to better align with part features or prime locations.
