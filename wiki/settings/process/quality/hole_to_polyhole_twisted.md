# hole_to_polyhole_twisted

> Location: Process → Quality → Precision
> Also in this section: `hole_to_polyhole`, `hole_to_polyhole_threshold` (each documented on its own page).

---

## Polyholes

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `hole_to_polyhole_twisted`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `true`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--hole-to-polyhole-twisted=1`.  
A polyhole is a technique used in FFF 3D printing to improve the accuracy of circular holes. Instead of modeling a perfect circle, the hole is represented as a polygon with a reduced number of flat sides. This simplification forces the slicer to treat each segment as a straight line, which prints more reliably. By carefully choosing the number of sides and ensuring the polygon sits on the outer boundary of the hole, you can produce openings that more closely match the intended diameter.

![PolyHoles](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/PolyHoles.png?raw=true)

- Original implementation: [SuperSlicer Polyholes](https://github.com/supermerill/SuperSlicer/wiki/Polyholes)
- Idea and mathematics: [Hydraraptor](https://hydraraptor.blogspot.com/2011/02/polyholes.html)
