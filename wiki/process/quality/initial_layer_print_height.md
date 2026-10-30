# initial_layer_print_height

> Location: Process → Quality → Layer height
> 本小节同时涵盖：`layer_height`（各另有独立文档）。

---

# Layer Height

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `layer_height`, `initial_layer_print_height`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--layer-height=1` (same pattern for the other variables above).  
Layer height defines the vertical thickness of each printed layer, playing a crucial role in both print quality and printing speed.

> [!NOTE]
> You can use a variable layer height with the [Variable Layer Height](../../print_prepare/prepare_variable_layer_height.md) feature.

Using smaller layer heights increases print time but results in:

- Smoother surface finishes
- Less noticeable layer lines
- Enhanced detail on curves
- [Better performance on overhangs](#layer-height-overhangs-impacts)

![layer-height-spheres](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/layer-height-spheres.png?raw=true)

- [Quick Reference](#quick-reference)
- [Layer Height Guidelines](#layer-height-guidelines)
- [First Layer Height](#first-layer-height)
- [Layer Height Overhangs Impacts](#layer-height-overhangs-impacts)
