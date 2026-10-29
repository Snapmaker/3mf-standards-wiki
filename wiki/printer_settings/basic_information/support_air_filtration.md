# support_air_filtration

> 所在界面：打印机设置 → Basic information → Accessory
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_accessory.md` 的「Support air filtration」小节（2026-10-28），英文原文，待本地化校对。

---

## Support air filtration

[Mode](option_mode): `Developer`.  
[Variable](built_in_placeholders_variables): `support_air_filtration`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--support-air-filtration=1`.  
Air Filtration/Exhaust Fan Control in OrcaSlicer.  
OrcaSlicer use `M106 P3` command to control air-filtration/exhaust fan.

If you are using Klipper, you can define a `M106` macro to control both the normal part cooling fan, auxiliary fan, and exhaust fan.

Below is a reference configuration for Klipper.

> [!NOTE]
> Don't forget to change the pin name to the actual pin name you are using in the configuration.

```ini
# instead of using [fan], we define the default part cooling fan with [fan_generic] here
# this is the default part cooling fan
[fan_generic fan0]
pin: PA7
cycle_time: 0.01
hardware_pwm: false

# this is the auxiliary fan
# comment out it if you don't have auxiliary fan
[fan_generic fan2]
pin: PA8
cycle_time: 0.01
hardware_pwm: false

# this is the exhaust fan
# comment out it if you don't have exhaust fan
[fan_generic fan3]
pin: PA9
cycle_time: 0.01
hardware_pwm: false

[gcode_macro M106]
gcode:
    {% set fan = 'fan' + (params.P|int if params.P is defined else 0)|string %}
    {% set speed = (params.S|float / 255 if params.S is defined else 1.0) %}
    SET_FAN_SPEED FAN={fan} SPEED={speed}
```
