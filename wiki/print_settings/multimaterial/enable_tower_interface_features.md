# enable_tower_interface_features

> 所在界面：工艺设置 → Multimaterial → Prime tower
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_prime_tower.md` 的「Enable tower interface features」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：仅 Snapmaker U1 机型显示

---

## Enable tower interface features

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `enable_tower_interface_features`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--enable-tower-interface-features=1`.  
Changes how the prime tower is printed on interface layers, where different materials meet. On these layers the nozzle is heated to the filament's **Interface layer print temperature** (its maximum recommended nozzle temperature when set to -1), and extra filament can be pre-extruded before the purge. These values are set per filament in [Multimaterial Wipe Tower Parameters](material_multimaterial#multimaterial-wipe-tower-parameters).

The Type 1 tower applies this on the layers where a material category starts or stops being printed on the tower. The Type 2 tower applies it on every layer with a filament change, and also adds the filament's **Interface layer purge length** to the purge.
