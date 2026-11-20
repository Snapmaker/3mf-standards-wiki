# sparse_infill_rotate_template

> Location: Process → Strength → Infill → Infill rotation template metalanguage
> Also in this section: `solid_infill_rotate_template` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `sparse_infill_rotate_template`.  
[Type](../../../general_settings/option_type.md#text): `Text`.  
[Default](../../../general_settings/option_type.md#default-value): `(empty)`.  
[Unit](../../../general_settings/option_type.md#unit): `°`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--sparse-infill-rotate-template=value`.  

This metalanguage provides a way to define the [direction and rotation](../../process/strength/align_infill_direction_to_model.md) of [patterns](../../process/strength/sparse_infill_pattern.md) in 3D printing.

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
