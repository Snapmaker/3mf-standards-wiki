# line_width

> Location: Process → Quality → Line width

---

# Line Width

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `line_width`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float or Percentage`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--line-width=20%`.  
These settings define how wide each extruded line of filament will be.  
Line width can be configured in two ways:

- Fixed value in millimeters (mm)
- Percentage of the nozzle diameter

> [!TIP]
> Using percentages allows the slicer to automatically adjust the line width when the nozzle size changes, helping maintain consistent print quality across different nozzle sizes.

A good starting point is setting the line width to **100% of the nozzle diameter**. Values below this may lead to poor adhesion, while values above **150%** can cause **over-extrusion**, resulting in blobs or poor surface quality.  
However, slightly wider lines generally improve **layer bonding** and **print strength**, especially for internal features like walls and infill.

> [!NOTE]
> **Line width is the width of the line as laid on the layer.** Orca calculates the extruded volume from the line width and layer height, so a 100% line width gives a line as wide as the nozzle, and higher values squish the line wider than the nozzle opening.  
> You can read more on the flow math here: [Flow Math](https://manual.slic3r.org/advanced/flow-math).

> [!IMPORTANT]
> This will match only if using the [**Classic** wall generator](../../process/quality/quality_settings_wall_generator.md#classic).  
> [**Arachne**](../../process/quality/quality_settings_wall_generator.md#arachne) will adjust the line width dynamically based on the model's geometry, using these values as a reference.
