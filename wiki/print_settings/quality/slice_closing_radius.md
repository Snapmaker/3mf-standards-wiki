# slice_closing_radius

> 所在界面：工艺设置 → Quality → Precision
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_precision.md` 的「Slice gap closing radius」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Slice gap closing radius

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `slice_closing_radius`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--slice-closing-radius=1`.  
Cracks smaller than 2x the gap closing radius are filled during the triangle mesh slicing.  
The gap closing operation may reduce the final print resolution, therefore it is advisable to keep the value reasonably low.
