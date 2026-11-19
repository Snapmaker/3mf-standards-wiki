# graphic_effect_plate_temp_initial_layer

> Location: Filament → Filament → Bed temperature
> Visibility (preliminary, pending review): Shown only when the printer enables the corresponding bed type
> G-code embedded name: `first_layer_bed_temperature` (aggregated value, not read from this key directly: uses the initial-layer bed temperature of the active bed type, taking the maximum across slots so mixed-material printing runs the highest bed temperature).
> Also in this section: `supertack_plate_temp_initial_layer`, `supertack_plate_temp`, `cool_plate_temp_initial_layer`, `cool_plate_temp`, `textured_cool_plate_temp_initial_layer`, `textured_cool_plate_temp`, `eng_plate_temp_initial_layer`, `eng_plate_temp`, `hot_plate_temp_initial_layer`, `hot_plate_temp`, `textured_plate_temp_initial_layer`, `textured_plate_temp`, `graphic_effect_plate_temp` (each documented on its own page).

---

## Bed

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `graphic_effect_plate_temp_initial_layer`.  
[Type](../../../general_settings/option_type.md#list-types): `Integer list`.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[Range](../../../general_settings/option_type.md#range): `0–300` ℃.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--graphic-effect-plate-temp-initial-layer=1`.  
Set the bed temperature for the selected material for First Layer and Other Layers for each Bed type if [Support multi bed types](../../printer/basic_information/support_multi_bed_types.md) is enabled in printer settings.  
Using a higher temperature for the first layer can help improve adhesion to the build surface but be cautious of potential deformations like [elephant foot](../../process/quality/elefant_foot_compensation.md).
