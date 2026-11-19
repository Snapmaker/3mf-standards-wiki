# chamber_temperature

> Location: Filament → Filament → Print chamber temperature
> Also in this section: `activate_chamber_temp_control` (each documented on its own page).

---

## Print Chamber Temperature

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `chamber_temperature`.  
[Type](../../../general_settings/option_type.md): Integer list.  
[Default](../../../general_settings/option_type.md#default-value): — no static default.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--chamber-temperature=1`.  

> [!TIP]
> Check [Temperature calibration](../../../calibration/temp_calib.md) to find the optimal nozzle temperature for your filament.

Chamber temperature can affect the print quality, especially for high-temperature filaments.  
A heated chamber can help to maintain a consistent temperature throughout the print, reducing the risk of warping and improving layer adhesion. However, it is important to monitor the chamber temperature to ensure that it does not exceed the filament's deformation temperature.

> [!IMPORTANT]
> Low temperature Filaments like PLA can clog the nozzle if the chamber temperature is too high.

This option activates the emitting of an M191 command before the "machine_start_gcode" which sets the chamber temperature and waits until it is reached.  
In addition, it emits an M141 command at the end of the print to turn off the chamber heater, if present.

This option relies on the firmware supporting the M191 and M141 commands either via macros or natively and is usually used when an active chamber heater is installed.

> [!NOTE]
> Check [Support control chamber temperature](../../printer/basic_information/support_chamber_temp_control.md) in your printer settings to enable chamber temperature control.

For high-temperature materials like ABS, ASA, PC, and PA, a higher chamber temperature can help suppress or reduce warping and potentially lead to higher interlayer bonding strength. However, at the same time, a higher chamber temperature will reduce the efficiency of air filtration for ABS and ASA.

For PLA, PETG, TPU, PVA, and other low-temperature materials, this option should be disabled (set to 0) as the chamber temperature should be low to avoid extruder clogging caused by material softening at the heat break.

If enabled, this parameter also sets a G-code variable named chamber_temperature, which can be used to pass the desired chamber temperature to your print start macro, or a heat soak macro like this:

```pwsh
PRINT_START (other variables) CHAMBER_TEMP=[chamber_temperature]
```

This may be useful if your printer does not support M141/M191 commands, or if you desire to handle heat soaking in the print start macro if no active chamber heater is installed.

## Temperature Reference (U1 Presets)

The following table lists the values configured in the U1 filament presets shipped with this fork (`Generic @U1` and `Snapmaker @U1` families).  
Numbers in parentheses are the nozzle temperature ranges defined in the presets.  
Actual optimal temperatures still vary between filament brands — always follow the manufacturer's recommendations and run calibrations for best results.

| Material | Nozzle Temp (°C) | Bed Temp (°C) | Chamber Temp (°C) |
| --- | --- | --- | --- |
| PLA | 220 (190-240) | 65 | 0 |
| PETG | 245-255 (220-270) | 70-80 | 0 |
| ABS | 265-280 (240-280) | 90-100 | 60 (Snapmaker ABS) / 0 (Generic ABS) |
| ASA | 260-280 (240-280) | 90-100 | 0 |
| PA (Nylon) | 260 (240-280) | 100 | 60 |
| PC | 280 (260-290) | 100 | 0 |
| TPU | 215-240 (200-250) | 35 | 0 |

> [!NOTE]
> **How the chamber is controlled on U1**
> The U1 machine presets do not enable `support_chamber_temp_control`, so the M191/M141 path above is not used on U1 by default. The U1 start G-code instead manages the chamber through purifier macros (`SET_PURIFIER_MODE` with a target around 42-45 °C, then `WAIT_CHAMBER_TEMP`). The mode is chosen automatically from the filaments used in the print: a low-temperature filament with a `temperature_vitrification` of 50 °C or below triggers strong cooling, one of 70 °C or below (and above 50 °C) triggers weak cooling, and otherwise the chamber is kept warm.
