# detect_thin_wall

> Location: Process → Strength → Walls

---

## Detect thin wall

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `detect_thin_wall`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--detect-thin-wall=1`.  
By default, walls are printed as closed loops. When a wall is too thin to contain two line widths, enabling "Detect thin walls" prints it as a single extrusion line.  
Thin walls printed this way may have reduced surface quality and strength because they are not closed loops.

> [!TIP]
> It is usually recommended to use the [Arachne wall generator](../../process/quality/quality_settings_wall_generator.md#arachne), which disables "Detect thin walls" because it uses a different approach to wall generation.

- In small details, it can generate features that wouldn't be possible with traditional wall generation methods.  
  ![walls-small-detect-thin-off](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/walls/walls-small-detect-thin-off.png?raw=true)
  ![walls-small-detect-thin-on](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/walls/walls-small-detect-thin-on.png?raw=true)
- In large prints, it can generate defects more easily due to the reduced wall thickness.
  ![walls-big-detect-thin-off-on](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/walls/walls-big-detect-thin-off-on.png?raw=true)
