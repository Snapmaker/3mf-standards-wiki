# enable_tower_interface_features

> Location: Process → Multimaterial → Prime tower
> 显隐条件（初步梳理，待校对）：仅 Snapmaker U1 机型显示

---

## Enable tower interface features

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `enable_tower_interface_features`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--enable-tower-interface-features=1`.  
Changes how the prime tower is printed on interface layers, where different materials meet. On these layers the nozzle is heated to the filament's **Interface layer print temperature** (its maximum recommended nozzle temperature when set to -1), and extra filament can be pre-extruded before the purge. These values are set per filament in [Multimaterial Wipe Tower Parameters](../../filament/multimaterial/material_multimaterial.md#multimaterial-wipe-tower-parameters).

The Type 1 tower applies this on the layers where a material category starts or stops being printed on the tower. The Type 2 tower applies it on every layer with a filament change, and also adds the filament's **Interface layer purge length** to the purge.
