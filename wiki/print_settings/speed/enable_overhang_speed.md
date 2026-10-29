# enable_overhang_speed

> 所在界面：工艺设置 → Speed → Overhang speed
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/speed/speed_settings_overhang_speed.md` 的「Slow down for overhang」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Slow down for overhang

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `enable_overhang_speed`.  
[Type](option_type#list-types): `Boolean list`.  
[CLI Example](cli_mode#setting-overrides): `--enable-overhang-speed=1`.  
Enable this option to slow printing down for different overhang degrees.
This can help improve print quality and reduce issues like sagging.
