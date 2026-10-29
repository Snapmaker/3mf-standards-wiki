# wall_loops

> 所在界面：工艺设置 → Strength → Walls
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_walls.md` 的「Wall loops」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Wall loops

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `wall_loops`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--wall-loops=1`.  
"Wall loops" is the number of walls printed on each layer.  
Increasing the wall loops will:

- Enhance:
    - Layer adhesion
    - Strength
    - Rigidity
- Reduce infill ghosting
- Increase print time
