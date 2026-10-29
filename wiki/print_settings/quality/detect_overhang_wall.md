# detect_overhang_wall

> 所在界面：工艺设置 → Quality → Overhangs
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_overhangs.md` 的「Detect overhang wall」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Detect overhang wall

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `detect_overhang_wall`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--detect-overhang-wall=1`.  
Detects the overhang percentage relative to the line width and uses a different speed to print.
Walls with 100% overhang are printed with the bridge settings.

![overhang](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/overhangs/overhang.png?raw=true)
