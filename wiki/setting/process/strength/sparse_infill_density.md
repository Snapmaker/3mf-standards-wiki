# sparse_infill_density

> Location: Process → Strength → Infill

---

## Sparse infill density

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `sparse_infill_density`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Percentage`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--sparse-infill-density=20%`.  
Infill density determines the amount of material used to fill the interior of a 3D print. It is usually expressed as a percentage, with 100% being completely solid.

- Higher density increases
    - Strength
    - Material usage
    - Print time.

> [!NOTE]
> Density is usually calculated as a percentage of the total infill volume, not the total print volume.  
> Nevertheless, **not all patterns interpret density the same way**, so the actual material usage may vary.  
> You can see each pattern's material usage in the [Patterns section](../../process/strength/strength_settings_patterns.md).
