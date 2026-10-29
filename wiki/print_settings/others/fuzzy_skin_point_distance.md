# fuzzy_skin_point_distance

> 所在界面：工艺设置 → Others → Fuzzy Skin
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_fuzzy_skin.md` 的「Point distance」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Point distance

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `fuzzy_skin_point_distance`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--fuzzy-skin-point-distance=1`.  
Average distance between random sample points along each line segment.  
Smaller values add more detail and increase computation; larger values produce coarser, faster results.
