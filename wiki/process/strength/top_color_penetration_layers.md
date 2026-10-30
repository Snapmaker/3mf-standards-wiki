# top_color_penetration_layers

> Location: Process → Strength → Top/bottom shells
> 本小节同时涵盖：`bottom_color_penetration_layers`（各另有独立文档）。

---

## Paint Penetration Layers

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `top_color_penetration_layers`, `bottom_color_penetration_layers`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--top-color-penetration-layers=1` (same pattern for the other variables above).  

> [!IMPORTANT]
> NEW FEATURE: **Paint penetration layers**  
> Available in: [Nightly builds](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/nightly-builds) or Releases greater than **2.4.2**.

When a top or bottom surface is painted with [Color Painting](../../print_prepare/prepare_color_painting.md), its color is also printed in the layers under a painted top surface and over a painted bottom surface, so the filament behind the paint doesn't show through. This is the number of layers that take the color, including the surface layer.  
Each layer further from the surface is colored about two line widths narrower than the one before, so the color tapers into the model instead of reaching its walls.

- **0:** uses the [Shell Layers](#shell-layers) count. This is the default, and how painted surfaces were always printed before this setting existed.
- **Lower values:** keep a thick shell for strength while printing fewer layers in the painted color, saving a filament change and its purge on each layer left out.
- **Higher values:** give a deeper, more saturated color, which helps with translucent or light filaments that let the layers behind them show through.

> [!WARNING]
> Keep the value within the shell, which is the larger of [Shell Layers](#shell-layers) and the layers needed to reach [Shell Thickness](#shell-thickness). A larger value also colors the [sparse infill](../../process/strength/strength_settings_infill.md) under or over the painted area, adding filament changes where they can't be seen.
