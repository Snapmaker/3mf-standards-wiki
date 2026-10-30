# max_resonance_avoidance_speed

> Location: Printer → Motion ability → Resonance Avoidance

---

## Resonance Compensation

Resonance Compensations are the methods used to reduce the vibrations of the printer during high-speed movements, which can cause ringing on the surface of the model.

### Resonance Avoidance

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `resonance_avoidance`, `min_resonance_avoidance_speed`, `max_resonance_avoidance_speed`.  
[Type](../../general_settings/option_type.md): `resonance_avoidance` (Boolean), `min_resonance_avoidance_speed` (Float), `max_resonance_avoidance_speed` (Float).  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--resonance-avoidance=1` (`resonance_avoidance` shown; other variables above follow their own type).  
By reducing the speed of the outer wall to avoid the resonance zone of the printer, ringing on the surface of the model are avoided.

> [!TIP]
> Check the [VFA Calibration](../../calibration/vfa_calib.md).

### Input Shaping

[Mode](../../general_settings/option_mode.md): `Expert`.  
[Variables](../../developer_reference/built_in_placeholders_variables.md): `input_shaping_emit`, `input_shaping_freq_x`, `input_shaping_freq_y`, `input_shaping_damp_x`, `input_shaping_damp_y`.  
[Type](../../general_settings/option_type.md): `input_shaping_emit` (Boolean), `input_shaping_freq_x` (Float), `input_shaping_freq_y` (Float), `input_shaping_damp_x` (Float), `input_shaping_damp_y` (Float).  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--input-shaping-emit=1` (`input_shaping_emit` shown; other variables above follow their own type).  
During high-speed movements, vibrations can cause a phenomenon called "ringing," where periodic ripples appear on the print surface. Input Shaping provides an effective solution by counteracting these vibrations, improving print quality and reducing wear on components without needing to significantly lower print speeds.

> [!NOTE]
> Some Printers have built-in accelerometers that can be used to **automatically** measure the resonant frequencies of the printer.  
> If your printer has one, consider using it as it can provide more accurate results in less time and usually is autosaved into the printer firmware.

> [!TIP]
> It's usually recommended to perform [Input Shaping calibration](../../calibration/input_shaping_calib.md) once a year or after any mechanical or structural changes such as relocation, changing the support surface, new belts, motors, frame, etc.

> [!IMPORTANT]
> **RepRap** can only set one frequency for both X and Y axes so you will need to select a frequency that works well for both axes.

![inputshaping_printer](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/InputShaping/inputshaping_printer.png?raw=true)

#### Input Shaping Type

[Mode](../../general_settings/option_mode.md): `Expert`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `input_shaping_type`.  
[Type](../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../general_settings/option_type.md#choice): `Default, MZV, ZV, ZVD, ZVDD, ZVDDD, EI, EI2, 2HUMP_EI, EI3, 3HUMP_EI, DAA, Disable`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--input-shaping-type=Default`.  
The Input Shaping type determines the algorithm used to counteract the vibrations.  
It is usually recommended to use MZV, EI (specially for Delta printers) or ZV as a simple and effective solution.  
Not all Input Shaping types are available in all firmware and their performance may vary depending on the firmware implementation and the printer's mechanics.

##### Default

When "Default" is selected, the firmware's default input shaper will be used.  
Every firmware and even its version may have a different default type but usually are:

- Klipper: MZV
- Marlin: ZV
- RepRap:
    - Version >= 3.4: MZV
    - Version < 3.4: DAA
    - Version < 3.2: DAA (without damping option)

##### Version Table

| Type | Name | [Klipper](https://www.klipper3d.org/Resonance_Compensation.html#technical-details) | [RepRap](https://docs.duet3d.com/User_manual/Reference/Gcodes#m593-configure-input-shaping) | [Marlin 2](https://marlinfw.org/docs/features/ft_motion.html#more-complexity-zv-input-shaper) |
| --- | --- | --- | --- | --- |
| MZV | Modified Zero Vibration | >=0.9.0 | >=3.4 | - |
| ZV | Zero Vibration | >=0.9.0 | = 3.5 | >2.1.2 |
| ZVD | Zero Vibration Derivative | >=0.9.0 | >=3.4 | - |
| ZVDD | Zero Vibration Double Derivative | - | >=3.4 | - |
| ZVDDD | Zero Vibration Triple Derivative | - | >=3.4 | - |
| EI | Extra Insensitive | >=0.9.0 | - | - |
| 2HUMP_EI / EI2 | Two-Hump Extra Insensitive | >=0.9.0 | >=3.4 | - |
| 3HUMP_EI / EI3 | Three-Hump Extra Insensitive | >=0.9.0 | >=3.4 | - |
| [FT_MOTION](https://marlinfw.org/docs/features/ft_motion.html#fixed-time-motion-by-ulendo) | Fixed-Time Motion | - | - | >2.1.3 |
| DAA | Damped Anti-Resonance | - | < 3.4 | - |

###### Fixed-Time Motion

TODO: This calibration test is currently under development. See the [Marlin documentation](https://marlinfw.org/docs/gcode/M493.html) for more information.
