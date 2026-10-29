# draft_shield

> 所在界面：工艺设置 → Others → Skirt
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_skirt.md` 的「Shield」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Shield

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `draft_shield`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `disabled, enabled`.  
[CLI Example](cli_mode#setting-overrides): `--draft-shield=disabled`.  
When enabled, the skirt is printed as a draft shield: a taller wall surrounding the part to help protect prints (especially ABS/ASA) from drafts and sudden temperature changes.  
This is most useful for open-frame printers without an enclosure.

- Enabled: the shield is as tall as the tallest printed model on the bed.
- Disabled: the skirt uses the [Height](#height) value.

> [!NOTE]
> The skirt is printed at the [skirt distance](#distance) from the brim, or from the object if it has no brim, so the draft shield does not intersect brims.
