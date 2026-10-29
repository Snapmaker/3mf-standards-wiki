# interlocking_beam

> 所在界面：工艺设置 → Multimaterial → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_advanced.md` 的「Interlocking Beam」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Interlocking Beam

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `interlocking_beam`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--interlocking-beam=1`.  
Generates an interlocking beam structure at the locations where different filaments touch. This improves the adhesion between filaments, especially for models printed in different materials.
