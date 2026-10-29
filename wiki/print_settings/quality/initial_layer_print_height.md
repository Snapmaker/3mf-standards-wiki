# initial_layer_print_height

> 所在界面：工艺设置 → Quality → Layer height
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_layer_height.md` 的「Layer Height」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`layer_height`（各另有独立文档）。

---

# Layer Height

[Mode](option_mode): `Simple`.  
[Variables](built_in_placeholders_variables): `layer_height`, `initial_layer_print_height`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--layer-height=1` (same pattern for the other variables above).  
Layer height defines the vertical thickness of each printed layer, playing a crucial role in both print quality and printing speed.

> [!NOTE]
> You can use a variable layer height with the [Variable Layer Height](prepare_variable_layer_height) feature.

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
