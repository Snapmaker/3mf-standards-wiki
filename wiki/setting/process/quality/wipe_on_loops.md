# wipe_on_loops

> Location: Process → Quality → Seam

---

### Wipe on loop (inward movement)

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `wipe_on_loops`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--wipe-on-loops=1`.  
When finishing printing an outer wall "loop" (i.e., an extrusion that starts and ends at the same point), move the nozzle slightly inwards towards the part. This only applies when [Wall loops](../../process/strength/strength_settings_walls.md#wall-loops) is greater than 1. That move aims to reduce seam unevenness by tucking in the end of the seam to the part. It also slightly cleans the nozzle before traveling to the next area of the model, reducing stringing.  
The inward move itself is a short, fixed move of about 20% of the nozzle diameter. The wipe and retraction that follow use your printer/material Wipe distance and Retract amount before wipe values.

![seam-wipe-on-loop](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/seam/seam-wipe-on-loop.png?raw=true)

![seam-wipe-on-loops-options](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/seam/seam-wipe-on-loops-options.png?raw=true)
