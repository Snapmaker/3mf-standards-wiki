# enable_tower_interface_cooldown_during_tower

> 所在界面：工艺设置 → Multimaterial → Prime tower
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_prime_tower.md` 的「Cool down from interface boost during prime tower」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅 Snapmaker U1 机型显示

---

### Cool down from interface boost during prime tower

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `enable_tower_interface_cooldown_during_tower`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--enable-tower-interface-cooldown-during-tower=1`.  
Only shown when [Enable tower interface features](#enable-tower-interface-features) is enabled, and only used by the Type 2 tower. After heating to the interface temperature, the nozzle is set back to its print temperature at the start of the purge, so it cools down while the tower is printed. When disabled, the print temperature is restored only after the purge is finished.
