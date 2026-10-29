# sparse_infill_pattern

> 所在界面：工艺设置 → Strength → Infill
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_infill.md` 的「Sparse Infill Pattern」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Sparse Infill Pattern

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `sparse_infill_pattern`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `rectilinear, alignedrectilinear, zigzag, crosszag, lockedzag, line, grid, triangles, tri-hexagon, cubic, adaptivecubic, quartercubic, supportcubic, lightning, honeycomb, 3dhoneycomb, lateral-honeycomb, lateral-lattice, crosshatch, tpmsd, tpmsfk, gyroid, concentric, hilbertcurve, archimedeanchords, octagramspiral`.  
[CLI Example](cli_mode#setting-overrides): `--sparse-infill-pattern=rectilinear`.  
> [!TIP]
> See [Infill Patterns Wiki List](strength_settings_patterns) with **detailed specifications**, including their strengths and weaknesses.
