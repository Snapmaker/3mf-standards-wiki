# fan_speedup_overhangs

> 所在界面：打印机设置 → Basic information → Cooling Fan
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_cooling_fan.md` 的「Fan speed-up time」小节（2026-10-28），英文原文，待本地化校对。

---

## Fan speed-up time

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `fan_speedup_time`, `fan_speedup_overhangs`.  
[Type](option_type): `fan_speedup_time` (Float), `fan_speedup_overhangs` (Boolean).  
[CLI Example](cli_mode#setting-overrides): `--fan-speedup-time=1` (`fan_speedup_time` shown; other variables above follow their own type).  
Start the fan this number of seconds earlier than its target start time (you can use fractional seconds). It assumes infinite acceleration for this time estimation, and will only take into account G1 and G0 moves (arc fitting is unsupported).
It won't move fan commands from custom G-code (they act as a sort of 'barrier').
It won't move fan commands into the start G-code if the 'only custom start G-code' is activated.
Use 0 to deactivate.

### Only overhangs

Will only take into account the delay for the cooling of overhangs.
