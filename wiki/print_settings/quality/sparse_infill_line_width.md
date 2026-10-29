# sparse_infill_line_width

> 所在界面：工艺设置 → Quality → Line width
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_line_width.md` 的「Sparse Infill」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Sparse Infill

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `sparse_infill_line_width`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--sparse-infill-line-width=20%`.  
Recommended to use a conservative value, typically around 115% to improve layer adhesion without getting near volumetric flow limitations.  
If you need stronger infill, it's recommended to use [infill line multiplier](strength_settings_infill#fill-multiline) when possible.
