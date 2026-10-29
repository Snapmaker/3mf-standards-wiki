# reduce_infill_retraction

> 所在界面：工艺设置 → Others → G-code output
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_g_code_output.md` 的「Reduce Infill Retraction」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Reduce Infill Retraction

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `reduce_infill_retraction`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--reduce-infill-retraction=1`.  
When enabled, the slicer will skip retractions for travel moves that occur entirely inside infill regions. This reduces the number of retractions and can speed up printing for complex models, but it may increase oozing or stringing inside infill. Slicing time may also increase slightly.

Each retraction adds moves that print nothing, and a travel that skips it skips all of them, keeping only the travel itself:

- The [retraction](printer_extruder_retraction#length) pulls the filament back at the [Retraction speed](printer_extruder_retraction#retraction-speed) before the travel, and the [deretraction](printer_extruder_retraction#deretraction-speed) pushes it back, plus any [Extra length on restart](printer_extruder_retraction#extra-length-on-restart), before the next line starts. With the default 0.8 mm at 30 mm/s, each of the two takes about 27 ms.
- With [Wipe while retracting](printer_extruder_retraction#wipe-while-retracting), the nozzle also moves back along the last line for the [Wipe distance](printer_extruder_retraction#wipe-distance) while it retracts.
- With a [Z-hop](printer_extruder_z_hop#z-hop-height), the nozzle lifts before the travel and lowers after it, on the Z axis, which on most printers is much slower than X and Y.

Tens of milliseconds per travel can add up to minutes over the thousands of infill travels of a large print.

Travels shorter than the [Travel distance threshold](printer_extruder_retraction#travel-distance-threshold) never retract, with or without this option. Infill lines whose ends are next to each other are joined into one path (see [Anchor](strength_settings_infill#anchor)), so there is no travel to retract for between them.

**Recommended** when internal cosmetic quality is not critical and you want fewer retractions.
