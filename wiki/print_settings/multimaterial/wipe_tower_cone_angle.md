# wipe_tower_cone_angle

> 所在界面：工艺设置 → Multimaterial → Prime tower
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_prime_tower.md` 的「Stabilization cone apex angle」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅非 BBL 机型显示

---

#### Stabilization cone apex angle

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wipe_tower_cone_angle`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--wipe-tower-cone-angle=1`.  
Angle at the apex of the cone that is used to stabilize the wipe tower. A larger angle means a wider base.
