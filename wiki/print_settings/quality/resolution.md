# resolution

> 所在界面：工艺设置 → Quality → Precision
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_precision.md` 的「Resolution」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Resolution

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `resolution`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--resolution=1`.  
The G-code path is generated after simplifying the contour of models to avoid too many points and G-code lines.  
Smaller values mean higher resolution and more time to slice. If you are slicing big models on machines with low processing power, you may want to increase this value to speed up the slicing process.
