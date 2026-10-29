# wipe_tower_wall_type

> 所在界面：工艺设置 → Multimaterial → Prime tower
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_prime_tower.md` 的「Wall type」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅非 BBL 机型显示

---

## Wall type

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wipe_tower_wall_type`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `rectangle, cone, rib`.  
[CLI Example](cli_mode#setting-overrides): `--wipe-tower-wall-type=rectangle`.  
Wipe tower outer wall type.
