# spiral_mode_max_xy_smoothing

> 所在界面：工艺设置 → Others → Special mode
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_special_mode.md` 的「Max XY Smoothing」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

#### Max XY Smoothing

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `spiral_mode_max_xy_smoothing`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--spiral-mode-max-xy-smoothing=20%`.  
Maximum distance to move points in XY to achieve a smooth spiral. If expressed as a percentage, it is calculated relative to the nozzle diameter.  
Higher values allow more smoothing but may distort the model slightly.
