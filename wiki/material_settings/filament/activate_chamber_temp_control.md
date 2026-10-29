# activate_chamber_temp_control

> 所在界面：耗材设置 → Filament → Print chamber temperature
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_temperatures.md` 的「Print Chamber Temperature」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`chamber_temperature`（各另有独立文档）。

---

## Print Chamber Temperature

[Mode](option_mode): `Simple`.  
[Variables](built_in_placeholders_variables): `activate_chamber_temp_control`, `chamber_temperature`, `chamber_minimal_temperature`.  
[Type](option_type): `activate_chamber_temp_control` (Boolean list), `chamber_temperature` (Integer list), `chamber_minimal_temperature` (Integer list).  
[CLI Example](cli_mode#setting-overrides): `--activate-chamber-temp-control=1` (`activate_chamber_temp_control` shown; other variables above follow their own type).  
Chamber temperature can affect the print quality, especially for high-temperature filaments.  
A heated chamber can help to maintain a consistent temperature throughout the print, reducing the risk of warping and improving layer adhesion. However, it is important to monitor the chamber temperature to ensure that it does not exceed the filament's deformation temperature.

> [!IMPORTANT]
> Low temperature Filaments like PLA can clog the nozzle if the chamber temperature is too high.

This option activates the emitting of an M191 command before the "machine_start_gcode" which sets the chamber temperature and waits until it is reached.  
In addition, it emits an M141 command at the end of the print to turn off the chamber heater, if present.

This option relies on the firmware supporting the M191 and M141 commands either via macros or natively and is usually used when an active chamber heater is installed.

> [!NOTE]
> Check [Support control chamber temperature](printer_basic_information_accessory#support-controlling-chamber-temperature) in your printer settings to enable chamber temperature control.

For high-temperature materials like ABS, ASA, PC, and PA, a higher chamber temperature can help suppress or reduce warping and potentially lead to higher interlayer bonding strength. However, at the same time, a higher chamber temperature will reduce the efficiency of air filtration for ABS and ASA.

For PLA, PETG, TPU, PVA, and other low-temperature materials, this option should be disabled (set to 0) as the chamber temperature should be low to avoid extruder clogging caused by material softening at the heat break.

If enabled, this parameter also sets a G-code variable named chamber_temperature, which can be used to pass the desired chamber temperature to your print start macro, or a heat soak macro like this:

```pwsh
PRINT_START (other variables) CHAMBER_TEMP=[chamber_temperature]
```

This may be useful if your printer does not support M141/M191 commands, or if you desire to handle heat soaking in the print start macro if no active chamber heater is installed.
