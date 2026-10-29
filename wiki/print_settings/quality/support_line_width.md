# support_line_width

> 所在界面：工艺设置 → Quality → Line width
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_line_width.md` 的「Support」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Support

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `support_line_width`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--support-line-width=20%`.  
Typically set to **100%** to balance material usage and functionality. Reducing it too much can lead to weak support structures that may not hold up during printing or break easily during removal, leaving debris on the model.
