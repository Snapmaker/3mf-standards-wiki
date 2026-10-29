# fan_kickstart

> 所在界面：打印机设置 → Basic information → Cooling Fan
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_cooling_fan.md` 的「Fan kick-start time」小节（2026-10-28），英文原文，待本地化校对。

---

## Fan kick-start time

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `fan_kickstart`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--fan-kickstart=1`.  
Emit a max fan speed command for this amount of seconds before reducing to target speed to kick-start the cooling fan.
This is useful for fans where a low PWM/power may be insufficient to get the fan started spinning from a stop, or to get the fan up to speed faster.
Set to 0 to deactivate.
