# extra_perimeters_on_overhangs

> 所在界面：工艺设置 → Quality → Overhangs
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_overhangs.md` 的「Extra perimeters on overhangs」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Extra perimeters on overhangs

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `extra_perimeters_on_overhangs`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--extra-perimeters-on-overhangs=1`.  
Create additional perimeter (overhang wall) paths over steep overhangs and areas where bridges cannot be anchored.

This option only works when [Detect overhang walls](#detect-overhang-wall) is enabled, even though it stays visible and editable when that option is off.

![extra-perimeters-on-overhangs](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/overhangs/extra-perimeters-on-overhangs.png?raw=true)
