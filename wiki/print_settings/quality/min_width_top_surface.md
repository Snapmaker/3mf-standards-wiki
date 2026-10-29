# min_width_top_surface

> 所在界面：工艺设置 → Quality → Walls and surfaces
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_wall_and_surfaces.md` 的「Threshold」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Threshold

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `min_width_top_surface`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--min-width-top-surface=20%`.  
If a top surface has to be printed and it's partially covered by another layer, it won't be considered as a top layer where its width is below this value. This can be useful to keep *Only one wall on top surfaces* from triggering on surfaces that should be covered only by walls.  
This value can be in mm or a % of the inner wall line width.

![only-one-wall-threshold](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Wall-Order/only-one-wall-threshold.png?raw=true)

> [!WARNING]
> If enabled, artifacts can be created if you have some thin features on the next layer, like letters. Set this setting to 0 to remove these artifacts.
