# top_surface_pattern

> 所在界面：工艺设置 → Strength → Top/bottom shells
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_top_bottom_shells.md` 的「Surface Pattern」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`bottom_surface_pattern`（各另有独立文档）。

---

## Surface Pattern

[Mode](option_mode): `Simple`.  
[Variables](built_in_placeholders_variables): `top_surface_pattern`, `bottom_surface_pattern`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `monotonic, monotonicline, rectilinear, alignedrectilinear, concentric, spiralinset, hilbertcurve, archimedeanchords, octagramspiral`.  
[CLI Example](cli_mode#setting-overrides): `--top-surface-pattern=monotonic` (same pattern for the other variables above).  
This setting controls the pattern of the surfaces.  
If [Shell Layers](#shell-layers) is greater than 1, the surface pattern will be applied to the outermost shell layer only and the rest will use [Internal Solid Infill Pattern](strength_settings_infill#internal-solid-infill).

> [!TIP]
> See [Infill Patterns Wiki List](strength_settings_patterns) with **detailed specifications**, including their strengths and weaknesses.

The surface patterns are:

- **[Concentric](strength_settings_patterns#concentric)**
- **[Rectilinear](strength_settings_patterns#rectilinear)**
- **[Monotonic](strength_settings_patterns#monotonic)**
- **[Monotonic line](strength_settings_patterns#monotonic-line)**: usually recommended for top surfaces.
- **[Aligned Rectilinear](strength_settings_patterns#aligned-rectilinear)**
- **[Spiral Inset](strength_settings_patterns#spiral-inset)**
- **[Hilbert Curve](strength_settings_patterns#hilbert-curve)**
- **[Archimedean Chords](strength_settings_patterns#archimedean-chords)**
- **[Octagram Spiral](strength_settings_patterns#octagram-spiral)**

> [!TIP]
> Enable [Align directions to model](strength_settings_advanced#align-directions-to-model) to make the top/bottom surface fill direction follow the model's orientation on the build plate.
