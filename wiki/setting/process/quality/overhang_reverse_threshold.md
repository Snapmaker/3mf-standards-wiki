# overhang_reverse_threshold

> Location: Process → Quality → Overhangs

---

### Reverse threshold

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `overhang_reverse_threshold`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float or Percentage`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--overhang-reverse-threshold=20%`.  
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
