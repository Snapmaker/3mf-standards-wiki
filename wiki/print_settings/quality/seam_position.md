# seam_position

> 所在界面：工艺设置 → Quality → Seam
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_seam.md` 的「Seam Position」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Seam Position

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `seam_position`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `nearest, aligned, aligned_back, back, random`.  
[CLI Example](cli_mode#setting-overrides): `--seam-position=nearest`.  
Controlling the position of seams can help improve the appearance and strength of the final print.

Typically, [Aligned Back](#aligned-back), [Aligned](#aligned), or [Back](#back) work the best, especially in combination with [seam painting](prepare_seam_painting) or [Precise Seam](prepare_precise_seam) modifiers.  
However, as seams create weak points and slight surface "bulges" or "divots", [random](#random) seam placement may be optimal for parts that need higher strength as that weak point is spread to different locations between layers (e.g., a pin meant to fit through a hole).
