# single_loop_draft_shield

> 所在界面：工艺设置 → Others → Skirt
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_skirt.md` 的「Single loop after first layer」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Single loop after first layer

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `single_loop_draft_shield`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--single-loop-draft-shield=1`.  
When enabled, limits the skirt or draft shield to a single wall after the first layer (i.e. only one loop is printed on subsequent layers). This reduces filament and print time but makes the shield less robust and more prone to warping or cracking.
