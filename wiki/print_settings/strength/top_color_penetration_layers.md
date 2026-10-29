# top_color_penetration_layers

> 所在界面：工艺设置 → Strength → Top/bottom shells
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_top_bottom_shells.md` 的「Paint Penetration Layers」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`bottom_color_penetration_layers`（各另有独立文档）。

---

## Paint Penetration Layers

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `top_color_penetration_layers`, `bottom_color_penetration_layers`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--top-color-penetration-layers=1` (same pattern for the other variables above).  

> [!IMPORTANT]
> NEW FEATURE: **Paint penetration layers**  
> Available in: [Nightly builds](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/nightly-builds) or Releases greater than **2.4.2**.

When a top or bottom surface is painted with [Color Painting](prepare_color_painting), its color is also printed in the layers under a painted top surface and over a painted bottom surface, so the filament behind the paint doesn't show through. This is the number of layers that take the color, including the surface layer.  
Each layer further from the surface is colored about two line widths narrower than the one before, so the color tapers into the model instead of reaching its walls.

- **0:** uses the [Shell Layers](#shell-layers) count. This is the default, and how painted surfaces were always printed before this setting existed.
- **Lower values:** keep a thick shell for strength while printing fewer layers in the painted color, saving a filament change and its purge on each layer left out.
- **Higher values:** give a deeper, more saturated color, which helps with translucent or light filaments that let the layers behind them show through.

> [!WARNING]
> Keep the value within the shell, which is the larger of [Shell Layers](#shell-layers) and the layers needed to reach [Shell Thickness](#shell-thickness). A larger value also colors the [sparse infill](strength_settings_infill) under or over the painted area, adding filament changes where they can't be seen.
