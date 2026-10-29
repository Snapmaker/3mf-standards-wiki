# infill_combination_max_layer_height

> 所在界面：工艺设置 → Strength → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/strength/strength_settings_advanced.md` 的「Max layer height」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Max layer height

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `infill_combination_max_layer_height`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--infill-combination-max-layer-height=20%`.  
Maximum layer height for the combined sparse infill.  
Set it to 0 or 100% to use the nozzle diameter (for maximum reduction in print time), or to a value of ~80% to maximize sparse infill strength.

The number of layers over which infill is combined is derived by dividing this value by the layer height and rounding down to a whole number.

Use either absolute mm values (e.g., 0.32mm for a 0.4mm nozzle) or percentages (e.g., 80%). This value must not be larger than the nozzle diameter.
