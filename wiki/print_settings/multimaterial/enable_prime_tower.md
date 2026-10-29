# enable_prime_tower

> 所在界面：工艺设置 → Multimaterial → Prime tower
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/multimaterial/multimaterial_settings_prime_tower.md` 的「Prime Tower」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

# Prime Tower

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `enable_prime_tower`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--enable-prime-tower=1`.  
The prime tower can be used to clean up residue on the nozzle and stabilize the chamber pressure inside the nozzle, in order to avoid appearance defects when printing objects.

> [!NOTE]
> Some settings on this page depend on the printer's [Wipe tower type](printer_multimaterial_wipe_tower). Bambu Lab printers always use the Type 1 tower. [Wipe Tower Rotation Angle](#wipe-tower-rotation-angle), [Maximal bridging distance](#maximal-bridging-distance), [Wipe tower purge lines spacing](#wipe-tower-purge-lines-spacing), [Extra flow for purge](#extra-flow-for-purge), [Maximum wipe tower print speed](#maximum-wipe-tower-print-speed) and [Stabilization cone apex angle](#stabilization-cone-apex-angle) are only shown with the Type 2 tower.
