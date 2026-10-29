# role_based_wipe_speed

> 所在界面：工艺设置 → Quality → Seam
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_seam.md` 的「Role based wipe speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Role based wipe speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `role_based_wipe_speed`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--role-based-wipe-speed=1`.  
Controls the speed of a wipe motion, i.e., how fast the nozzle will move over a printed area to "clean" it before traveling to another area of the model.  
It is recommended to turn this option on, to ensure the nozzle performs the wipe motion with the same speed that the feature was printed with.
