# thick_bridges

> 所在界面：工艺设置 → Quality → Bridging
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_bridging.md` 的「Thick bridges」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`thick_internal_bridges`（各另有独立文档）。

---

## Thick bridges

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `thick_bridges`, `thick_internal_bridges`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--thick-bridges=1` (same pattern for the other variables above).  

When enabled, bridge extrusion uses a line height equal to the nozzle diameter.  
![thick-bridges](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/bridging/thick-bridges.png?raw=true)  
This improves the strength and reliability of bridges, allowing you to span longer distances; however, it may produce a rougher surface finish.  
Disabling this option can improve bridge appearance, but it is recommended only for shorter spans or when using large nozzles.  
It's recommended to enable this option for internal bridges, as it increases their reliability when printed over sparse infill.
