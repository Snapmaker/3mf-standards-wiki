# precise_outer_wall

> 所在界面：工艺设置 → Quality → Precision
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_precision.md` 的「Precise wall」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Precise wall

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `precise_outer_wall`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--precise-outer-wall=1`.  
The 'Precise Wall' is a distinctive feature introduced by OrcaSlicer, aimed at improving the dimensional accuracy of prints and minimizing layer inconsistencies by slightly increasing the spacing between the outer wall and the inner wall when printing in [Inner/Outer wall order](quality_settings_wall_and_surfaces#innerouter).
