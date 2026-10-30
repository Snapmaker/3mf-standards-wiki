# minimum_sparse_infill_area

> Location: Process → Strength → Advanced

---

## Minimum sparse infill threshold

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `minimum_sparse_infill_area`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--minimum-sparse-infill-area=1`.  
Sparse infill areas smaller than the threshold value (in mm²) are replaced by [internal solid infill](../../process/strength/strength_settings_infill.md#internal-solid-infill).
This setting helps to ensure that small areas of sparse infill do not compromise the strength of the print. It is particularly useful for models with intricate designs or small features where sparse infill may not provide sufficient support.
