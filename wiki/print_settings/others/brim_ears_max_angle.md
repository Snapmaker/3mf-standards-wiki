# brim_ears_max_angle

> 所在界面：工艺设置 → Others → Brim
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_brim.md` 的「Ear max angle」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

#### Ear max angle

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `brim_ears_max_angle`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--brim-ears-max-angle=1`.  
Angle threshold (degrees) used to decide where mouse ears may be placed:

- 0° — disabled; no mouse ears are generated.
- Between 0° and 180° — ears are created at features with local angles sharper (smaller) than the threshold.
- 180° — ears are allowed on almost any non-straight feature.
