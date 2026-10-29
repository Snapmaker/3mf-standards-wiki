# wipe_tower_extra_rib_length

> 所在界面：工艺设置 → Multimaterial → Prime tower
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_prime_tower.md` 的「Extra rib length」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅非 BBL 机型显示

---

#### Extra rib length

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wipe_tower_extra_rib_length`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--wipe-tower-extra-rib-length=1`.  
Positive values can increase the size of the rib wall, while negative values can reduce the size. However, the size of the rib wall cannot be smaller than that determined by the purge volume.
