# support_threshold_angle

> 所在界面：工艺设置 → Support → Support
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_support.md` 的「Threshold angle」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Threshold angle

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `support_threshold_angle`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--support-threshold-angle=1`.  
Support will be generated for overhangs whose slope angle is below the threshold. The smaller this value is, the steeper the overhang that can be printed without support.  
If set to `0`, normal supports use the [Threshold overlap](#threshold-overlap) instead, while tree supports use 30°.
