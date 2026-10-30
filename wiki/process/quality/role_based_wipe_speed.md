# role_based_wipe_speed

> Location: Process → Quality → Seam

---

### Role based wipe speed

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `role_based_wipe_speed`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--role-based-wipe-speed=1`.  
Controls the speed of a wipe motion, i.e., how fast the nozzle will move over a printed area to "clean" it before traveling to another area of the model.  
It is recommended to turn this option on, to ensure the nozzle performs the wipe motion with the same speed that the feature was printed with.
