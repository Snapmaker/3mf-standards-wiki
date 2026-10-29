# extra_loading_move

> 所在界面：打印机设置 → Multimaterial → Single extruder multi-material parameters
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/multimaterial/printer_multimaterial_semm_parameters.md` 的「Extra loading distance」小节（2026-10-28），英文原文，待本地化校对。

---

## Extra loading distance

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `extra_loading_move`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--extra-loading-move=1`.  
 When set to zero, the distance the filament is moved from parking position during load is exactly the same as it was moved back during unload. When positive, it is loaded further, if negative, the loading move is shorter than unloading.
