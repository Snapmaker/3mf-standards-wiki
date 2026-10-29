# support_threshold_overlap

> 所在界面：工艺设置 → Support → Support
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_support.md` 的「Threshold overlap」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Threshold overlap

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `support_threshold_overlap`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--support-threshold-overlap=20%`.  
If [Threshold angle](#threshold-angle) is zero, support will be generated for overhangs whose overlap with the layer below is below the threshold. A percentage is relative to the outer wall line width.
The smaller this value is, the steeper the overhang that can be printed without support.  
Tree supports don't use this setting, so it is hidden for them.
