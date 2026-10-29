# fuzzy_skin_thickness

> 所在界面：工艺设置 → Others → Fuzzy Skin
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_fuzzy_skin.md` 的「Skin thickness」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Skin thickness

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `fuzzy_skin_thickness`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--fuzzy-skin-thickness=1`.  
Maximum lateral width (in mm) over which points can be displaced. This defines how far the wall can be jittered.  
Keep this below or near your outer wall line width and within nozzle/flow limits for reliable prints.
