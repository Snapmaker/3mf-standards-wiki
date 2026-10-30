# bottom_surface_pattern

> Location: Process → Strength → Top/bottom shells
> 本小节同时涵盖：`top_surface_pattern`（各另有独立文档）。

---

## Surface Pattern

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `top_surface_pattern`, `bottom_surface_pattern`.  
[Type](../../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../../general_settings/option_type.md#choice): `monotonic, monotonicline, rectilinear, alignedrectilinear, concentric, spiralinset, hilbertcurve, archimedeanchords, octagramspiral`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--top-surface-pattern=monotonic` (same pattern for the other variables above).  
This setting controls the pattern of the surfaces.  
If [Shell Layers](#shell-layers) is greater than 1, the surface pattern will be applied to the outermost shell layer only and the rest will use [Internal Solid Infill Pattern](../../process/strength/strength_settings_infill.md#internal-solid-infill).

> [!TIP]
> See [Infill Patterns Wiki List](../../process/strength/strength_settings_patterns.md) with **detailed specifications**, including their strengths and weaknesses.

The surface patterns are:

- **[Concentric](../../process/strength/strength_settings_patterns.md#concentric)**
- **[Rectilinear](../../process/strength/strength_settings_patterns.md#rectilinear)**
- **[Monotonic](../../process/strength/strength_settings_patterns.md#monotonic)**
- **[Monotonic line](../../process/strength/strength_settings_patterns.md#monotonic-line)**: usually recommended for top surfaces.
- **[Aligned Rectilinear](../../process/strength/strength_settings_patterns.md#aligned-rectilinear)**
- **[Spiral Inset](../../process/strength/strength_settings_patterns.md#spiral-inset)**
- **[Hilbert Curve](../../process/strength/strength_settings_patterns.md#hilbert-curve)**
- **[Archimedean Chords](../../process/strength/strength_settings_patterns.md#archimedean-chords)**
- **[Octagram Spiral](../../process/strength/strength_settings_patterns.md#octagram-spiral)**

> [!TIP]
> Enable [Align directions to model](../../process/strength/strength_settings_advanced.md#align-directions-to-model) to make the top/bottom surface fill direction follow the model's orientation on the build plate.
