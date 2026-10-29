# enable_extra_bridge_layer

> 所在界面：工艺设置 → Quality → Bridging
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_bridging.md` 的「Extra bridge layers」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Extra bridge layers

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `enable_extra_bridge_layer`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `disabled, external_bridge_only, internal_bridge_only, apply_to_all`.  
[CLI Example](cli_mode#setting-overrides): `--enable-extra-bridge-layer=disabled`.  
This option enables the generation of an extra bridge layer over bridges.

Extra bridge layers help improve bridge appearance and reliability, as the solid infill is better supported. This is especially useful in fast printers, where the bridge and solid infill speeds vary greatly. The extra bridge layer results in reduced pillowing on top surfaces, as well as reduced separation of the external bridge layer from its surrounding perimeters.

It is generally recommended to set this to at least **External bridge only**, unless specific issues with the sliced model are found.

**Options:**

- **Disabled** - does not generate second bridge layers. This is the default and is set for compatibility purposes.
- **External bridge only** - generates second bridge layers for external-facing bridges only. Please note that small bridges that are shorter or narrower than the set number of perimeters will be skipped as they would not benefit from a second bridge layer. If generated, the second bridge layer will be extruded parallel to the first bridge layer to reinforce the bridge strength.
- **Internal bridge only** - generates second bridge layers for internal bridges over sparse infill only. Please note that the internal bridges count towards the top shell layer count of your model. The second internal bridge layer will be extruded as close to perpendicular to the first as possible. If multiple regions in the same island, with varying bridge angles are present, the last region of that island will be selected as the angle reference.
- **Apply to all** - generates second bridge layers for both internal and external-facing bridges.
