# min_width_top_surface

> Location: Process → Quality → Walls and surfaces

---

### Threshold

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `min_width_top_surface`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float or Percentage`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--min-width-top-surface=20%`.  
If a top surface has to be printed and it's partially covered by another layer, it won't be considered as a top layer where its width is below this value. This can be useful to keep *Only one wall on top surfaces* from triggering on surfaces that should be covered only by walls.  
This value can be in mm or a % of the inner wall line width.

![only-one-wall-threshold](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/only-one-wall-threshold.png?raw=true)

> [!WARNING]
> If enabled, artifacts can be created if you have some thin features on the next layer, like letters. Set this setting to 0 to remove these artifacts.
