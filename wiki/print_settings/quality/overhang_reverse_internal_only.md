# overhang_reverse_internal_only

> 所在界面：工艺设置 → Quality → Overhangs
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_overhangs.md` 的「Reverse internal only」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Reverse internal only

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `overhang_reverse_internal_only`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--overhang-reverse-internal-only=1`.  
A simple way to reduce the texture on the outer wall is to only reverse the internal walls.
This will still provide almost all of the benefits of alternating extrusion direction on even layers (if using [inner/outer](quality_settings_wall_and_surfaces#innerouter)), but the outer wall will be printed in the same direction, resulting in a smoother surface finish.
