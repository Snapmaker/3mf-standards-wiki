# overhang_reverse_threshold

> 所在界面：工艺设置 → Quality → Overhangs
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_overhangs.md` 的「Reverse threshold」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Reverse threshold

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `overhang_reverse_threshold`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--overhang-reverse-threshold=20%`.  
You can set a threshold for the overhang reversal to be considered useful.
Can be set as:

- **0**: Disables the threshold, meaning that all walls will be reversed on even layers.
- **mm**: A fixed distance in millimeters.
- **%**: A percentage of the perimeter width.

When using this setting, the walls will make the reversal texture in the layers where the overhang is above the threshold, and the rest of the walls will be printed in the normal direction.
This could result in uneven texture, sometimes considered worse than the full reversal texture, so it is recommended to use this setting only if you are sure that the overhang reversal will not be useful for your model.

> [!NOTE]
> Only available when:
>
> - [Detect overhang wall](#detect-overhang-wall) is enabled
> - [Reverse on even](#reverse-on-even) is enabled
> - [Reverse internal only](#reverse-internal-only) is disabled
>
> If those conditions are not met, this setting will be hidden.
