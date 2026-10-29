# wipe_before_external_loop

> 所在界面：工艺设置 → Quality → Seam
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_seam.md` 的「Wipe Before External」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Wipe Before External

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wipe_before_external_loop`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--wipe-before-external-loop=1`.  
To minimize the visibility of potential over-extrusion at the start of an external perimeter, the de-retraction move is performed slightly inside the model, next to the start of the external perimeter. That way, any potential over-extrusion is hidden from the outside surface.

This is useful when printing with [Outer/Inner](quality_settings_wall_and_surfaces#outerinner) or [Inner/Outer/Inner](quality_settings_wall_and_surfaces#innerouterinner) wall print order, as in these modes it is more likely that an external perimeter is printed immediately after a de-retraction move, which would cause slight extrusion variance at the start of a seam.
