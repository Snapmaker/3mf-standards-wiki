# emit_machine_limits_to_gcode

> 所在界面：打印机设置 → Motion ability → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/motion ability/printer_motion_ability.md` 的「Emit limits to G-code」小节（2026-10-28），英文原文，待本地化校对。

---

## Emit limits to G-code

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `emit_machine_limits_to_gcode`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--emit-machine-limits-to-gcode=1`.  
If enabled, the machine limits will be emitted to G-code file.
This option will be ignored if the G-code flavor is set to Klipper.
