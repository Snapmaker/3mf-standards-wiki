# wipe_tower_extra_flow

> 所在界面：工艺设置 → Multimaterial → Prime tower
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_prime_tower.md` 的「Extra flow for purge」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅非 BBL 机型显示

---

## Extra flow for purge

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wipe_tower_extra_flow`.  
[Type](option_type#integer-float-percentage): `Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--wipe-tower-extra-flow=20%`.  
Extra flow used for the purging lines on the wipe tower. This makes the purging lines thicker than they normally would be. The spacing is adjusted automatically.
