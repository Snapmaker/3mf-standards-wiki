# spiral_mode

> 所在界面：工艺设置 → Others → Special mode
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_special_mode.md` 的「Spiral vase」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Spiral vase

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `spiral_mode`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--spiral-mode=1`.  
Spiral vase mode transforms a solid model into a single-walled print with solid bottom layers, eliminating seams by continuously spiraling the outer contour.  
This creates a smooth, vase-like appearance.
