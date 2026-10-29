# fuzzy_skin_persistence

> 所在界面：工艺设置 → Others → Fuzzy Skin
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_fuzzy_skin.md` 的「Skin Noise Persistence」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Skin Noise Persistence

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `fuzzy_skin_persistence`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--fuzzy-skin-persistence=1`.  
Controls how amplitude decays across octaves. Lower persistence results in smoother noise; higher persistence keeps finer-scale detail stronger.
