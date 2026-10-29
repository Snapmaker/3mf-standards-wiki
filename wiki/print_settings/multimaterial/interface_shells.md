# interface_shells

> 所在界面：工艺设置 → Multimaterial → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_advanced.md` 的「Interface Shells」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Interface Shells

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `interface_shells`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--interface-shells=1`.  
Forces the generation of solid shells between adjacent materials/volumes. Useful for multi-extruder prints with translucent materials or manual soluble support material.
