# sparse_infill_speed

> 所在界面：工艺设置 → Speed → Other layers speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_other_layers_speed.md` 的「Sparse infill」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Sparse infill

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `sparse_infill_speed`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--sparse-infill-speed=1`.  
Speed of [sparse infill](strength_settings_infill) which is printed faster than solid infill to reduce print time.  
If you are using your [Infill Pattern](strength_settings_infill) as an aesthetic feature, you may want to set it closer to the [outer wall speed](#outer-wall) to get better quality.
