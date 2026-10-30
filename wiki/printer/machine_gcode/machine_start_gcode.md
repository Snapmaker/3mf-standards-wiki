# machine_start_gcode

> Location: Printer → Machine G-code → Machine start G-code

---

## Machine start G-code

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `machine_start_gcode`.  
[Type](../../general_settings/option_type.md#text): `Text`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--machine-start-gcode=value`.  
This G-code is executed at the beginning of a print job, before any printing starts. It is typically used to prepare the printer for printing, such as homing axes, heating the bed and nozzle, and performing any necessary pre-print checks.

You can also use it for setting up custom notifications with M300 (play beep sound) or use a custom purge sequence:

```gcode
G90 ; use absolute coordinates
M83 ; extruder relative mode
M140 S[bed_temperature_initial_layer_single] ; set final bed temp
M104 S150 ; set temporary nozzle temp to prevent oozing during homing
G4 S10 ; allow partial nozzle warmup
G28 ; home all axis
G1 Z25 F240 ; lift nozzle
G1 X2 Y10 F3000 ; move to front left
M104 S[nozzle_temperature_initial_layer] ; set final nozzle temp
M190 S[bed_temperature_initial_layer_single] ; wait for bed temp to stabilize
M109 S[nozzle_temperature_initial_layer] ; wait for nozzle temp to stabilize
; Start Beep to indicate ready to print
M300 P136 S622
M300 P136 S0
M300 P136 S311
M300 P136 S466
M300 P273 S0
M300 P136 S415
M300 P409 S0
M300 P136 S622
M300 P136 S0
M300 P545 S466
; Purge Line
G1 Z0.28 F240 ; move to a custom layer height for purge
G1 X{first_layer_print_min[0]-15} Y{first_layer_print_min[1]} Z0.8 F6000.0 ; position 15mm left from the lower left of the first layer
G1 X{first_layer_print_min[0]-15} Y{first_layer_print_min[1]+30} E30 F360.0 ; extrude 30mm of filament in the y direction
G92 E0.0 ; reset extruder
G1 E-0.5 F2100 ; small retraction
G1 Y{first_layer_print_min[1]+40} F6000.0 ; move an additional 10mm without extruding
G92 E0.0 ; reset extruder
```
