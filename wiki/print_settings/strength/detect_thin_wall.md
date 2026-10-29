# detect_thin_wall

> 所在界面：工艺设置 → Strength → Walls
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_walls.md` 的「Detect thin wall」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Detect thin wall

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `detect_thin_wall`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--detect-thin-wall=1`.  
By default, walls are printed as closed loops. When a wall is too thin to contain two line widths, enabling "Detect thin walls" prints it as a single extrusion line.  
Thin walls printed this way may have reduced surface quality and strength because they are not closed loops.

> [!TIP]
> It is usually recommended to use the [Arachne wall generator](quality_settings_wall_generator#arachne), which disables "Detect thin walls" because it uses a different approach to wall generation.

- In small details, it can generate features that wouldn't be possible with traditional wall generation methods.  
  ![walls-small-detect-thin-off](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/walls/walls-small-detect-thin-off.png?raw=true)
  ![walls-small-detect-thin-on](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/walls/walls-small-detect-thin-on.png?raw=true)
- In large prints, it can generate defects more easily due to the reduced wall thickness.
  ![walls-big-detect-thin-off-on](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/walls/walls-big-detect-thin-off-on.png?raw=true)
