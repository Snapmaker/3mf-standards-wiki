# seam_position

> Location: Process → Quality → Seam

---

## Seam Position

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `seam_position`.  
[Type](../../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../../general_settings/option_type.md#choice): `nearest, aligned, aligned_back, back, random`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--seam-position=nearest`.  
Controlling the position of seams can help improve the appearance and strength of the final print.

Typically, [Aligned Back](#aligned-back), [Aligned](#aligned), or [Back](#back) work the best, especially in combination with [seam painting](../../../print_prepare/prepare_seam_painting.md) or [Precise Seam](../../../print_prepare/prepare_precise_seam.md) modifiers.  
However, as seams create weak points and slight surface "bulges" or "divots", [random](#random) seam placement may be optimal for parts that need higher strength as that weak point is spread to different locations between layers (e.g., a pin meant to fit through a hole).
