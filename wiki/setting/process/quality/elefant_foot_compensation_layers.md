# elefant_foot_compensation_layers

> Location: Process → Quality → Precision
> 本小节同时涵盖：`elefant_foot_compensation`（各另有独立文档）。

---

## Elephant foot compensation

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `elefant_foot_compensation`, `elefant_foot_compensation_layers`.  
[Type](../../../general_settings/option_type.md): `elefant_foot_compensation` (Float), `elefant_foot_compensation_layers` (Integer).  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--elefant-foot-compensation=1` (`elefant_foot_compensation` shown; other variables above follow their own type).  
This feature compensates for the "elephant foot" effect, which occurs when the first few layers of a print are wider than the rest due to:

- Weight of the material above them.
- Thermal expansion of the material.
- Bed temperature being too high.
- Inaccurate bed height/leveling.

![elephant-foot](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/elephant-foot.svg?raw=true)

To mitigate this effect, OrcaSlicer allows you to specify a positive distance by which the first layer is shrunk, decreasing linearly over the specified number of layers. This adjustment effectively reduces the width of the first few layers, helping to achieve a more accurate final print size.

The compensation is only applied when the object is printed directly on the build plate. It is skipped when a [raft](../../process/support/support_settings_raft.md) is used.

![elephant-foot-compensation](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/elephant-foot-compensation.png?raw=true)

The compensation works as follows:  
When $\mathrm{current\_layer} \le \mathrm{input\_compensation\_layers}$

$$
\mathrm{compensation} = \mathrm{input\_compensation\_distance} - \frac{\mathrm{input\_compensation\_distance}}{\mathrm{input\_compensation\_layers}} \times (\mathrm{current\_layer} - 1)
$$

According to the equation, we can establish the following rules:

- In the 1st layer, since it is layer `1 - 1 = 0`, compensation is 100%.
- The intermediate layers (between the first and input_compensation_layers) will have linear compensation.
- Layers above the specified amount will not be compensated.

Assuming the compensation value is 0.25 mm:

- Elephant Foot Compensation Layers = 1 :
    - 1st layer: `0.25mm` compensation (100%)
    - 2nd layer and beyond: No compensation (0 mm)
- Elephant Foot Compensation Layers = 2 :
    - 1st layer: `0.25mm` compensation (100%)
    - 2nd layer: `0.25 − (0.25 / 2) × (2 - 1) = 0.125mm` compensation (50%)
    - 3rd layer and beyond: No compensation (0 mm).
- Elephant Foot Compensation Layers = 5 :
    - 1st layer: `0.25mm` compensation (100%)
    - 2nd layer: `0.25 − (0.25 / 5) × (2 - 1) = 0.2mm` compensation (80%)
    - 3rd layer: `0.25 − (0.25 / 5) × (3 - 1) = 0.15mm` compensation (60%)
    - 4th layer: `0.25 − (0.25 / 5) × (4 - 1) = 0.1mm` compensation (40%)
    - 5th layer: `0.25 − (0.25 / 5) × (5 - 1) = 0.05mm` compensation (20%)
    - 6th layer and beyond: No compensation (0 mm).

> [!NOTE]
> This feature makes the part look like it has a smaller footprint on the build plate in the preview, but the final print (if calibrated correctly) will have the correct dimensions.  
> That's why the brim may look disconnected from the object when this feature is enabled. But in the final print, the brim will be correctly attached to the object.  
> If you use a high Elephant foot compensation value, you may want to enable the [Brim use EFC outline](../../process/others/others_settings_brim.md#brim-use-efc-outline) option to ensure proper brim attachment.
