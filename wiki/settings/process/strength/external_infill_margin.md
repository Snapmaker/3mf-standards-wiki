# external_infill_margin

> Location: Process → Strength → Infill → Anchor solid infill by X mm
> Status: placeholder — to be completed.

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `external_infill_margin`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float or Percentage`.  
[Default](../../../general_settings/option_type.md#default-value): `(empty)`.  
[Unit](../../../general_settings/option_type.md#unit): `mm or %`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--external-infill-margin=1`.  

This parameter grows the top/bottom/solid layers by the specified mm to anchor them into the sparse infill and support the perimeters above. Can be a % of the width of the perimeters.

A % value is [`line_width`](../quality/line_width.md).

## Notes

Expands the top/bottom/solid infill layers outward by the given millimeters (or a percentage of line width), anchoring solid infill into the sparse infill to better support the outer walls above. Empty means no expansion.

Difference from [`infill_anchor`](infill_anchor.md): the latter controls how far sparse-infill line ends anchor into inner walls; this key controls how far solid infill expands outward.

<!-- TODO: recommended values, impact on top-surface quality -->
