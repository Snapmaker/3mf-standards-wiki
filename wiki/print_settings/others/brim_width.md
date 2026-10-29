# brim_width

> 所在界面：工艺设置 → Others → Brim
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_brim.md` 的「Width」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Width

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `brim_width`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--brim-width=1`.  
Distance between the model and the outermost brim line.  
Increasing this value widens the brim, which can improve adhesion but increases material usage.

On a [belt printer](#brim-on-belt-printers), the width is measured on the belt surface and applies to every brim type.

When **Brim type** is set to **Mouse ear**, this setting is labeled **Brim ear radius** *(Nightly builds and releases greater than 2.4.2)*. Its value sets the radius of each automatically generated ear. When **Brim type** is set to **Painted**, the size of brim ears is controlled in the [Brim ears Painting tool](prepare_brim_ears_painting).
