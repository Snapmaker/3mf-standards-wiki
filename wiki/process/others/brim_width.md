# brim_width

> Location: Process → Others → Brim

---

## Width

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `brim_width`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--brim-width=1`.  
Distance between the model and the outermost brim line.  
Increasing this value widens the brim, which can improve adhesion but increases material usage.

On a [belt printer](#brim-on-belt-printers), the width is measured on the belt surface and applies to every brim type.

When **Brim type** is set to **Mouse ear**, this setting is labeled **Brim ear radius** *(Nightly builds and releases greater than 2.4.2)*. Its value sets the radius of each automatically generated ear. When **Brim type** is set to **Painted**, the size of brim ears is controlled in the [Brim ears Painting tool](../../print_prepare/prepare_brim_ears_painting.md).
