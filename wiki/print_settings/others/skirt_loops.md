# skirt_loops

> 所在界面：工艺设置 → Others → Skirt
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_skirt.md` 的「Loops」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Loops

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `skirt_loops`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--skirt-loops=1`.  
Number of skirt loops to print.  
Usually 2 loops are recommended, but more loops improve priming and give a larger buffer between the nozzle and the part, at the cost of extra filament and time.  
Set to 0 to disable the skirt.

![skirt](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/skirt/skirt.png?raw=true)
