# spiral_mode_smooth

> 所在界面：工艺设置 → Others → Special mode
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_special_mode.md` 的「Smooth Spiral」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Smooth Spiral

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `spiral_mode_smooth`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--spiral-mode-smooth=1`.  
When enabled, Smooth Spiral smooths out X and Y moves as well, resulting in no visible seams even on non-vertical walls.  
This produces the smoothest possible spiral print.

> [!NOTE]
> If you are using absolute E distances, the smoothing may not work as expected.
