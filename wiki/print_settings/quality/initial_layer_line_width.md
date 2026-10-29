# initial_layer_line_width

> 所在界面：工艺设置 → Quality → Line width
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_line_width.md` 的「First Layer」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### First Layer

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `initial_layer_line_width`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--initial-layer-line-width=20%`.  
A wider first layer (with a higher [first layer height](quality_settings_layer_height#first-layer-height)) improves bed adhesion and compensates for uneven build surfaces.  
First layer line width also overrides [Brim's](others_settings_brim) and [Skirt's](others_settings_skirt) line width.
