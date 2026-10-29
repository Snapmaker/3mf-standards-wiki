# fuzzy_skin_noise_type

> 所在界面：工艺设置 → Others → Fuzzy Skin
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_fuzzy_skin.md` 的「Noise Type」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Noise Type

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `fuzzy_skin_noise_type`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `classic, perlin, billow, ridgedmulti, voronoi, ripple`.  
[CLI Example](cli_mode#setting-overrides): `--fuzzy-skin-noise-type=classic`.  
Select the noise algorithm used to generate the random offsets. Different noise types produce distinct visual textures.
