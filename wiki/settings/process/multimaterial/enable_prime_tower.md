# enable_prime_tower

> Location: Process → Multimaterial → Prime tower → Prime Tower

---

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `enable_prime_tower`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `false`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--enable-prime-tower=1`.  

The prime tower can be used to clean up residue on the nozzle and stabilize the chamber pressure inside the nozzle, in order to avoid appearance defects when printing objects.

> [!NOTE]
> Some settings on this page depend on the printer's [Wipe tower type](../../process/multimaterial/wipe_tower_cone_angle.md). Bambu Lab printers always use the Type 1 tower. Wipe Tower Rotation Angle, [Maximal bridging distance](wipe_tower_bridging.md), [Wipe tower purge lines spacing](wipe_tower_extra_spacing.md), [Extra flow for purge](wipe_tower_extra_flow.md), [Maximum wipe tower print speed](wipe_tower_max_purge_speed.md) and [Stabilization cone apex angle](wipe_tower_cone_angle.md) are only shown with the Type 2 tower.
