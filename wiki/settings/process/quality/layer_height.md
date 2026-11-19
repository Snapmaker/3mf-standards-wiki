# layer_height

> Location: Process → Quality → Layer height
> 本小节同时涵盖：`initial_layer_print_height`（各另有独立文档）。

---

# Layer Height

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `layer_height`, `initial_layer_print_height`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[Defaults](../../../general_settings/option_type.md#default-value): `layer_height` (0.2), `initial_layer_print_height` (0.2).  
[Ranges](../../../general_settings/option_type.md#range): `layer_height` (`≥ 0` mm), `initial_layer_print_height` (`≥ 0` mm).  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--layer-height=1` (same pattern for the other variables above).  
Layer height defines the vertical thickness of each printed layer, playing a crucial role in both print quality and printing speed.

> [!NOTE]
> You can use a variable layer height with the [Variable Layer Height](../../../print_prepare/prepare_variable_layer_height.md) feature.

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

## Quick Reference

| Nozzle Size | Min | Max | First Layer Height |
| --- | --- | --- | --- |
| 0.2mm | 0.04mm | 0.16mm | 0.12mm |
| 0.4mm | 0.08mm | 0.32mm | 0.25mm |
| 0.6mm | 0.12mm | 0.48mm | 0.35mm |
| 0.8mm | 0.16mm | 0.64mm | 0.45mm |

> [!NOTE]
> 表仅列 U1 机型可用喷嘴尺寸（0.2 / 0.4 / 0.6 / 0.8 mm）。

## Layer Height Guidelines

Usually, the optimal range for layer height is between 20% and 80% of the nozzle diameter.

- **Below 20%:** Flow inconsistencies and "fish scale" patterns may occur, especially at high speeds.
- **Over 80%:** Increased risk of layer adhesion issues and reduced print quality.

## First Layer Height

Controls the thickness of the initial layer.  
A thicker first layer improves bed adhesion and compensates for build surface imperfections.

**Recommended:** 0.25mm for 0.4mm nozzle (62.5% of nozzle diameter)  
**Maximum:** 65% of nozzle diameter

## Layer Height Overhangs Impacts

Layer height directly affects overhang angle capability and quality.

![layer-height](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/layer-height.svg?raw=true)

**Smaller layer heights** enable steeper overhangs by reducing the unsupported distance between layers, while **larger layer heights** increase this gap, leading to more sagging and requiring support material at shallower angles.
