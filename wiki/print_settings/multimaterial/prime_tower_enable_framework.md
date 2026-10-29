# prime_tower_enable_framework

> 所在界面：工艺设置 → Multimaterial → Prime tower
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_prime_tower.md` 的「Internal ribs」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Internal ribs

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `prime_tower_enable_framework`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--prime-tower-enable-framework=1`.  
Adds internal ribs to increase the stability of the prime tower. Only used by the Type 1 tower, where each purge section of the tower keeps its full size up to the top instead of shrinking on upper layers that need less purging.
