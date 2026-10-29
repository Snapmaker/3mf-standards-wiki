# filter_out_gap_fill

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_infill.md` 的「Filter out tiny gaps」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Filter out tiny gaps

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `filter_out_gap_fill`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--filter-out-gap-fill=1`.  
Don't print gap fill with a length smaller than the specified threshold (in mm).  
This setting applies to top, bottom and solid infill and, if using the [classic perimeter generator](quality_settings_wall_generator#classic), to wall gap fill.
