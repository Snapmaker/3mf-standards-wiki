# skirt_speed

> 所在界面：工艺设置 → Others → Skirt
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_skirt.md` 的「Speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `skirt_speed`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--skirt-speed=1`.  
Printing speed for the skirt in mm/s. Set to 0 to use the [First layer infill](speed_settings_initial_layer_speed#initial-layer-infill) speed on the first layer and the [Support](speed_settings_other_layers_speed#support) speed on higher layers.  
Slower speeds give a more reliable prime; very fast skirt speeds may not adhere properly and come off, causing problems with the part.
