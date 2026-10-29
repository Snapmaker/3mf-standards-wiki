# brim_ears_detection_length

> 所在界面：工艺设置 → Others → Brim
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_brim.md` 的「Ear detection radius」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

#### Ear detection radius

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `brim_ears_detection_length`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--brim-ears-detection-length=1`.  
The geometry is decimated before sharp angles are detected.  
This parameter sets the minimum deviation length used for the decimation.  
Set to 0 to disable.
