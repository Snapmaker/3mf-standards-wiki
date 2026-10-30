# enable_extra_bridge_layer

> Location: Process → Quality → Bridging

---

## Extra bridge layers

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `enable_extra_bridge_layer`.  
[Type](../../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../../general_settings/option_type.md#choice): `disabled, external_bridge_only, internal_bridge_only, apply_to_all`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--enable-extra-bridge-layer=disabled`.  
This option enables the generation of an extra bridge layer over bridges.

Extra bridge layers help improve bridge appearance and reliability, as the solid infill is better supported. This is especially useful in fast printers, where the bridge and solid infill speeds vary greatly. The extra bridge layer results in reduced pillowing on top surfaces, as well as reduced separation of the external bridge layer from its surrounding perimeters.

It is generally recommended to set this to at least **External bridge only**, unless specific issues with the sliced model are found.

**Options:**

- **Disabled** - does not generate second bridge layers. This is the default and is set for compatibility purposes.
- **External bridge only** - generates second bridge layers for external-facing bridges only. Please note that small bridges that are shorter or narrower than the set number of perimeters will be skipped as they would not benefit from a second bridge layer. If generated, the second bridge layer will be extruded parallel to the first bridge layer to reinforce the bridge strength.
- **Internal bridge only** - generates second bridge layers for internal bridges over sparse infill only. Please note that the internal bridges count towards the top shell layer count of your model. The second internal bridge layer will be extruded as close to perpendicular to the first as possible. If multiple regions in the same island, with varying bridge angles are present, the last region of that island will be selected as the angle reference.
- **Apply to all** - generates second bridge layers for both internal and external-facing bridges.
