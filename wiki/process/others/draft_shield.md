# draft_shield

> Location: Process → Others → Skirt

---

## Shield

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `draft_shield`.  
[Type](../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../general_settings/option_type.md#choice): `disabled, enabled`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--draft-shield=disabled`.  
When enabled, the skirt is printed as a draft shield: a taller wall surrounding the part to help protect prints (especially ABS/ASA) from drafts and sudden temperature changes.  
This is most useful for open-frame printers without an enclosure.

- Enabled: the shield is as tall as the tallest printed model on the bed.
- Disabled: the skirt uses the [Height](#height) value.

> [!NOTE]
> The skirt is printed at the [skirt distance](#distance) from the brim, or from the object if it has no brim, so the draft shield does not intersect brims.
