# enable_prime_tower

> Location: Process → Multimaterial → Prime tower

---

# Prime Tower

[Mode](../../general_settings/option_mode.md): `Simple`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `enable_prime_tower`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--enable-prime-tower=1`.  
The prime tower can be used to clean up residue on the nozzle and stabilize the chamber pressure inside the nozzle, in order to avoid appearance defects when printing objects.

> [!NOTE]
> Some settings on this page depend on the printer's [Wipe tower type](../../printer/multimaterial/printer_multimaterial_wipe_tower.md). Bambu Lab printers always use the Type 1 tower. [Wipe Tower Rotation Angle](#wipe-tower-rotation-angle), [Maximal bridging distance](#maximal-bridging-distance), [Wipe tower purge lines spacing](#wipe-tower-purge-lines-spacing), [Extra flow for purge](#extra-flow-for-purge), [Maximum wipe tower print speed](#maximum-wipe-tower-print-speed) and [Stabilization cone apex angle](#stabilization-cone-apex-angle) are only shown with the Type 2 tower.
