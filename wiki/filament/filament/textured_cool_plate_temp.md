# textured_cool_plate_temp

> Location: Filament → Filament → Bed temperature
> 显隐条件（初步梳理，待校对）：仅当打印机启用对应床型时显示
> 本小节同时涵盖：`supertack_plate_temp_initial_layer`、`supertack_plate_temp`、`cool_plate_temp_initial_layer`、`cool_plate_temp`、`textured_cool_plate_temp_initial_layer`、`eng_plate_temp_initial_layer`、`eng_plate_temp`、`hot_plate_temp_initial_layer`、`hot_plate_temp`、`textured_plate_temp_initial_layer`、`textured_plate_temp`（各另有独立文档）。

---

## Bed

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `supertack_plate_temp_initial_layer`, `supertack_plate_temp`, `cool_plate_temp_initial_layer`, `cool_plate_temp`, `textured_cool_plate_temp_initial_layer`, `textured_cool_plate_temp`, `eng_plate_temp_initial_layer`, `eng_plate_temp`, `hot_plate_temp_initial_layer`, `hot_plate_temp`, `textured_plate_temp_initial_layer`, `textured_plate_temp`.  
[Type](../../general_settings/option_type.md#list-types): `Integer list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--supertack-plate-temp-initial-layer=1` (same pattern for the other variables above).  
Set the bed temperature for the selected material for First Layer and Other Layers for each Bed type if [Support multi bed types](../../printer/basic_information/printer_basic_information_printable_space.md#support-multi-bed-types) is enabled in printer settings.  
Using a higher temperature for the first layer can help improve adhesion to the build surface but be cautious of potential deformations like [elephant foot](../../process/quality/quality_settings_precision.md#elephant-foot-compensation).

Bed temperature plays a crucial role in ensuring proper filament adhesion to the build surface, which directly impacts both print success and quality.  
Most materials have a relatively broad optimal range for bed temperature (typically +/-5°C).  
In general, following the manufacturer’s recommendations, maintaining a clean bed (free from oils or fingerprints), ensuring a stable [chamber temperature](#print-chamber-temperature), and having a properly leveled bed will produce reliable results.

- If the bed temperature is too low, the filament may fail to adhere properly, leading to warping, weak layer bonding, or complete detachment. In severe cases, the printed part may dislodge entirely and stick to the nozzle or other printer components, potentially causing mechanical damage.
- If the bed temperature is too high, the lower layers can overheat and soften excessively, resulting in deformation such as [elephant foot](../../process/quality/quality_settings_precision.md#elephant-foot-compensation).

> [!TIP]
> As a general guideline, you can use the [glass transition temperature](https://en.wikipedia.org/wiki/Glass_transition) (Tg) of the material and subtract 5–10 °C to estimate a safe upper limit for bed temperature.  
> See [this article](https://magigoo.com/blog/prevent-warping-temperature-and-first-layer-adhesion-magigoo/) for a detailed explanation.

> [!NOTE]
> For challenging prints involving materials with **high shrinkage** (e.g., nylons or polycarbonate) or geometries prone to warping, dialed-in settings are critical.  
> In these cases, [chamber temperature](#print-chamber-temperature) becomes a **major factor** in preventing detachment and ensuring print success.
