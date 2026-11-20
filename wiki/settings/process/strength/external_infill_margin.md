# external_infill_margin

> Location: Process → Strength → Infill
> Status: placeholder — to be completed.

## Basic information

- Label: Anchor solid infill by X mm
- Mode: Advanced
- Type: Float or Percentage, unit mm or % (% relative to [`line_width`](../quality/line_width.md)), min 0, max 50
- Default: (empty, i.e. no expansion)

> Tooltip: This parameter grows the top/bottom/solid layers by the specified mm to anchor them into the sparse infill and support the perimeters above. Can be a %% of the width of the perimeters.

## Notes

Expands the top/bottom/solid infill layers outward by the given millimeters (or a percentage of line width), anchoring solid infill into the sparse infill to better support the outer walls above. Empty means no expansion.

Difference from [`infill_anchor`](infill_anchor.md): the latter controls how far sparse-infill line ends anchor into inner walls; this key controls how far solid infill expands outward.

<!-- TODO: recommended values, impact on top-surface quality -->
