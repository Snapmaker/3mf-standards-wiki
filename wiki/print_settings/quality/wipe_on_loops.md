# wipe_on_loops

> 所在界面：工艺设置 → Quality → Seam
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_seam.md` 的「Wipe on loop (inward movement)」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Wipe on loop (inward movement)

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wipe_on_loops`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--wipe-on-loops=1`.  
When finishing printing an outer wall "loop" (i.e., an extrusion that starts and ends at the same point), move the nozzle slightly inwards towards the part. This only applies when [Wall loops](strength_settings_walls#wall-loops) is greater than 1. That move aims to reduce seam unevenness by tucking in the end of the seam to the part. It also slightly cleans the nozzle before traveling to the next area of the model, reducing stringing.  
The inward move itself is a short, fixed move of about 20% of the nozzle diameter. The wipe and retraction that follow use your printer/material Wipe distance and Retract amount before wipe values.

![seam-wipe-on-loop](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/seam/seam-wipe-on-loop.png?raw=true)

![seam-wipe-on-loops-options](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/seam/seam-wipe-on-loops-options.png?raw=true)
