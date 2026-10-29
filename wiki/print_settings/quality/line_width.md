# line_width

> 所在界面：工艺设置 → Quality → Line width
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_line_width.md` 的「Line Width」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

# Line Width

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `line_width`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--line-width=20%`.  
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
> This will match only if using the [**Classic** wall generator](quality_settings_wall_generator#classic).  
> [**Arachne**](quality_settings_wall_generator#arachne) will adjust the line width dynamically based on the model's geometry, using these values as a reference.
