# solid_infill_rotate_template

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_infill_rotation_template_metalanguage.md` 的「Infill rotation template metalanguage」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`sparse_infill_rotate_template`（各另有独立文档）。

---

# Infill rotation template metalanguage

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `sparse_infill_rotate_template`, `solid_infill_rotate_template`.  
[Type](option_type#text): `Text`.  
[CLI Example](cli_mode#setting-overrides): `--sparse-infill-rotate-template=value` (same pattern for the other variables above).  
This metalanguage provides a way to define the [direction and rotation](strength_settings_infill#direction-and-rotation) of [patterns](strength_settings_patterns) in 3D printing.

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
