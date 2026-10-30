# ironing_inset

> Location: Process → Quality → Ironing

---

## Inset

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `ironing_inset`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--ironing-inset=1`.  
The distance to keep from the edges, which can help prevent over-extrusion at the edges of the surface being ironed.

![ironing-inset](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/ironing/ironing-inset.png?raw=true)

If this value is set to 0, an inset of half the nozzle diameter is used, so the [ironing pattern](#pattern) stays slightly inside the outer boundaries of the top surface being ironed.
