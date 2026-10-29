# auxiliary_fan

> 所在界面：打印机设置 → Basic information → Accessory
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_accessory.md` 的「Auxiliary Part Cooling Fan」小节（2026-10-28），英文原文，待本地化校对。

---

## Auxiliary Part Cooling Fan

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `auxiliary_fan`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--auxiliary-fan=1`.  
Enable this option if machine has auxiliary part cooling fan.  
The speed will be set for each material in the [material cooling settings](material_cooling#auxiliary-part-cooling-fan).

G-code command:

```gcode
M106 P2 S(0-255)
```

### Auxiliary Fan

OrcaSlicer uses `M106 P#` (Set Fan Speed) / `M107 P#` (Fan Off) to control any fans managed by the slicer.
The `P` parameter indicates the fan index as defined by OrcaSlicer:

- `P0`: part cooling fan (default layer fan)
- `P1` (if present): an additional fan
- `P2`: often used as Aux / CPAP / Booster
- `P3` (and higher): sometimes Exhaust / Enclosure, etc.

With Klipper you can create macros that translate both the OrcaSlicer numeric fan index `P` and **human‑readable names** for your physical fans. This keeps compatibility with generated G‑code (M106 P0 / M106 P2 …) while letting you address fans by name internally.

> [!WARNING]
> Adjust pin names and parameters (power, cycle_time, etc.) to match your hardware.

- [Nozzle type](#nozzle-type)
- [Nozzle HRC](#nozzle-hrc)
- [Auxiliary Part Cooling Fan](#auxiliary-part-cooling-fan)
    - [Auxiliary Fan](#auxiliary-fan)
        - [Simple option (indexes only → fan0, fan2, fan3)](#simple-option-indexes-only--fan0-fan2-fan3)
        - [Advanced option (Index ⇄ Name mapping)](#advanced-option-index--name-mapping)
            - [Quick customization](#quick-customization)
            - [Usage](#usage)
- [Support controlling chamber temperature](#support-controlling-chamber-temperature)
    - [Using Chamber Temperature Variables in Machine G-code](#using-chamber-temperature-variables-in-machine-g-code)
    - [Klipper Chamber Temperature](#klipper-chamber-temperature)
- [Support air filtration](#support-air-filtration)

#### Simple option (indexes only → fan0, fan2, fan3)

This is the original basic example where the `P` index is concatenated (`fan0`, `fan2`, `fan3`). Use it if you don't need custom names:

```ini
# Part cooling fan
[fan_generic fan0]
pin: PA7
cycle_time: 0.01
hardware_pwm: false

# Auxiliary fan (comment out if you don't have it)
[fan_generic fan2]
pin: PA8
cycle_time: 0.01
hardware_pwm: false

# Exhaust / enclosure fan (comment out if you don't have it)
[fan_generic fan3]
pin: PA9
cycle_time: 0.01
hardware_pwm: false

[gcode_macro M106]
gcode:
    {% set fan = 'fan' + (params.P|int if params.P is defined else 0)|string %}
    {% set speed = (params.S|float / 255 if params.S is defined else 1.0) %}
    SET_FAN_SPEED FAN={fan} SPEED={speed}

[gcode_macro M107]
gcode:
    {% set fan = 'fan' + (params.P|int if params.P is defined else 0)|string %}
    {% if params.P is defined %}
    SET_FAN_SPEED FAN={fan} SPEED=0
    {% else %}
    # No P -> turn off typical defined fans
    SET_FAN_SPEED FAN=fan0 SPEED=0
    SET_FAN_SPEED FAN=fan2 SPEED=0
    SET_FAN_SPEED FAN=fan3 SPEED=0
    {% endif %}
```

#### Advanced option (Index ⇄ Name mapping)

Lets you use descriptive names like `CPAP`, `EXHAUST`, etc. Useful if you re‑wire or repurpose fans without changing slicer output. Just keep `fan_map` updated.

```ini
# Example with friendly names + comments showing OrcaSlicer index

[fan_generic CPAP]        # fan 0 OrcaSlicer
pin: PB7
max_power: 0.8
shutdown_speed: 0
kick_start_time: 0.100
cycle_time: 0.005
hardware_pwm: False
off_below: 0.10

[fan_generic EXHAUST]     # fan 3 OrcaSlicer
pin: PE5
#max_power:
#shutdown_speed:
cycle_time: 0.01
hardware_pwm: False
#kick_start_time:
off_below: 0.2

# If you had another (e.g. P2) add here:
# [fan_generic AUX]
# pin: PXn

[gcode_macro M106]
description: "Set fan speed (Orca compatible)"
gcode:
    {% set fan_map = {
        0: "CPAP",      # Orca P0 → CPAP blower
        3: "EXHAUST",   # Orca P3 → Exhaust
        # 2: "AUX",     # Uncomment if you define AUX
    } %}
    {% set p = params.P|int if 'P' in params else 0 %}
    {% set fan = fan_map[p] if p in fan_map else fan_map[0] %}
    {% set speed = (params.S|float / 255 if 'S' in params else 1.0) %}
    SET_FAN_SPEED FAN={fan} SPEED={speed}

[gcode_macro M107]
description: "Turn off fans. No P = all, P# = specific"
gcode:
    {% set fan_map = {
        0: "CPAP",
        3: "EXHAUST",
        # 2: "AUX",
    } %}
    {% if 'P' in params %}
        {% set p = params.P|int %}
        {% if p in fan_map %}
            SET_FAN_SPEED FAN={fan_map[p]} SPEED=0
        {% else %}
            RESPOND PREFIX="warn" MSG="Unknown fan index P{{p}}"
        {% endif %}
    {% else %}
        # No P -> turn off all mapped fans
        {% for f in fan_map.values() %}
            SET_FAN_SPEED FAN={f} SPEED=0
        {% endfor %}
    {% endif %}
```

##### Quick customization

1. Add / remove entries in `fan_map` to reflect the indexes the slicer may use.
2. Keep comments like `# fan X OrcaSlicer` next to each `[fan_generic]` for easy correlation.
3. Tune `max_power`, `off_below`, `cycle_time` according to fan type (CPAP blower vs axial exhaust).

##### Usage

- From OrcaSlicer: `M106 P0 S255` (100% CPAP), `M106 P3 S128` (~50% EXHAUST).
- Turn one off: `M107 P3`. Turn all off: `M107`.
- You can still manually use `SET_FAN_SPEED FAN=CPAP SPEED=0.7` in the Klipper console.

---

Pick the variant that best fits your workflow; the advanced version provides extra clarity and flexibility while remaining fully compatible with standard OrcaSlicer G-code output.
