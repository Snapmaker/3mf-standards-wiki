# brim_type

> 所在界面：工艺设置 → Others → Brim
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_brim.md` 的「Type」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Type

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `brim_type`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `auto_brim, brim_ears, painted, outer_only, inner_only, outer_and_inner, no_brim, leading_edge_only`.  
[CLI Example](cli_mode#setting-overrides): `--brim-type=auto_brim`.  
Controls how the brim is generated on a model's outer and/or inner sides.
