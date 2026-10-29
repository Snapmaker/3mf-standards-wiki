# extra_solid_infills

> 所在界面：工艺设置 → Strength → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_infill.md` 的「Extra Solid Infill」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Extra Solid Infill

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `extra_solid_infills`.  
[Type](option_type#text): `Text`.  
[CLI Example](cli_mode#setting-overrides): `--extra-solid-infills=value`.  
Insert extra solid infills at specific layers to add strength at critical points in your print. This feature allows you to strategically reinforce your part without changing the overall sparse infill density.

![extra-solid-infill](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/fill/extra-solid-infill.gif?raw=true)

The pattern supports two formats:
