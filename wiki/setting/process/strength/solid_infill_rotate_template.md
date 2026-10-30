# solid_infill_rotate_template

> Location: Process → Strength → Infill
> 本小节同时涵盖：`sparse_infill_rotate_template`（各另有独立文档）。

---

# Infill rotation template metalanguage

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `sparse_infill_rotate_template`, `solid_infill_rotate_template`.  
[Type](../../../general_settings/option_type.md#text): `Text`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--sparse-infill-rotate-template=value` (same pattern for the other variables above).  
This metalanguage provides a way to define the [direction and rotation](../../process/strength/strength_settings_infill.md#direction-and-rotation) of [patterns](../../process/strength/strength_settings_patterns.md) in 3D printing.

- [Basic instructions](#basic-instructions)
- [Quick examples](#quick-examples)
    - [Defined angle](#defined-angle)
    - [Runtime instructions](#runtime-instructions)
    - [Joint sign](#joint-sign)
    - [Counting](#counting)
    - [Length modifier](#length-modifier)
- [Description of instructions and examples](#description-of-instructions-and-examples)
    - [Simple absolute instructions](#simple-absolute-instructions)
    - [Relative instructions](#relative-instructions)
    - [Repetitive, adjusting and one-time instructions](#repetitive-adjusting-and-one-time-instructions)
    - [Range instructions](#range-instructions)
    - [Constant layer number instructions](#constant-layer-number-instructions)
- [Complex template examples](#complex-template-examples)
- [Credits](#credits)
