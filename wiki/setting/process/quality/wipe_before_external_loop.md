# wipe_before_external_loop

> Location: Process → Quality → Seam

---

### Wipe Before External

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `wipe_before_external_loop`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--wipe-before-external-loop=1`.  
To minimize the visibility of potential over-extrusion at the start of an external perimeter, the de-retraction move is performed slightly inside the model, next to the start of the external perimeter. That way, any potential over-extrusion is hidden from the outside surface.

This is useful when printing with [Outer/Inner](../../process/quality/quality_settings_wall_and_surfaces.md#outerinner) or [Inner/Outer/Inner](../../process/quality/quality_settings_wall_and_surfaces.md#innerouterinner) wall print order, as in these modes it is more likely that an external perimeter is printed immediately after a de-retraction move, which would cause slight extrusion variance at the start of a seam.
