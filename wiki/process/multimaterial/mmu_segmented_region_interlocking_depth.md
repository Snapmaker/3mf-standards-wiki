# mmu_segmented_region_interlocking_depth

> Location: Process → Multimaterial → Advanced

---

## Interlocking depth of Segmented Region

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `mmu_segmented_region_interlocking_depth`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--mmu-segmented-region-interlocking-depth=1`.  
Interlocking depth of a segmented region. On every other layer, the painted region reaches only this deep into the model instead of the [Maximum Width of Segmented Region](#maximum-width-of-segmented-region), so consecutive layers interlock. Zero disables this feature. Hidden and ignored when [Interlocking Beam](#interlocking-beam) is enabled.
