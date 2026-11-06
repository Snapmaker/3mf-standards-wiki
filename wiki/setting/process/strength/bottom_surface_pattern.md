# bottom_surface_pattern

> Location: Process → Strength → Top/bottom shells
> 本小节同时涵盖：`top_surface_pattern`（各另有独立文档）。

---

## Surface Pattern

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `top_surface_pattern`, `bottom_surface_pattern`.  
[Type](../../../general_settings/option_type.md#choice): `Choice`.  
[Defaults](../../../general_settings/option_type.md#default-value): `top_surface_pattern` (ipMonotonicLine), `bottom_surface_pattern` (ipMonotonic).  
[Options](../../../general_settings/option_type.md#choice): `monotonic, monotonicline, rectilinear, alignedrectilinear, concentric, spiralinset, hilbertcurve, archimedeanchords, octagramspiral`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--top-surface-pattern=monotonic` (same pattern for the other variables above).  
This setting controls the pattern of the surfaces.  
If [Shell Layers](#shell-layers) is greater than 1, the surface pattern will be applied to the outermost shell layer only and the rest will use [Internal Solid Infill Pattern](../../process/strength/internal_solid_infill_pattern.md).

> [!TIP]
> See [Infill Patterns Wiki List](../../process/strength/sparse_infill_pattern.md) with **detailed specifications**, including their strengths and weaknesses.

The surface patterns are:

- **[Concentric](../../process/strength/sparse_infill_pattern.md)**
- **[Rectilinear](../../process/strength/sparse_infill_pattern.md)**
- **[Monotonic](../../process/strength/sparse_infill_pattern.md)**
- **[Monotonic line](../../process/strength/sparse_infill_pattern.md)**: usually recommended for top surfaces.
- **[Aligned Rectilinear](../../process/strength/sparse_infill_pattern.md)**
- **[Spiral Inset](../../process/strength/sparse_infill_pattern.md)**
- **[Hilbert Curve](../../process/strength/sparse_infill_pattern.md)**
- **[Archimedean Chords](../../process/strength/sparse_infill_pattern.md)**
- **[Octagram Spiral](../../process/strength/sparse_infill_pattern.md)**

> [!TIP]
> Enable [Align directions to model](../../process/strength/align_infill_direction_to_model.md) to make the top/bottom surface fill direction follow the model's orientation on the build plate.
