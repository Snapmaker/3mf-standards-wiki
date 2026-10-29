# wipe_speed

> 所在界面：工艺设置 → Quality → Seam
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_seam.md` 的「Wipe speed」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Wipe speed

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wipe_speed`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--wipe-speed=20%`.  
If [Role based wipe speed](#role-based-wipe-speed) is disabled, this sets the wipe speed, either as an absolute value or as a percentage of the travel speed.
