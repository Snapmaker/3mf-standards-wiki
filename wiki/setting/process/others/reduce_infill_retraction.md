# reduce_infill_retraction

> Location: Process → Others → G-code output

---

## Reduce Infill Retraction

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `reduce_infill_retraction`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--reduce-infill-retraction=1`.  
When enabled, the slicer will skip retractions for travel moves that occur entirely inside infill regions. This reduces the number of retractions and can speed up printing for complex models, but it may increase oozing or stringing inside infill. Slicing time may also increase slightly.

Each retraction adds moves that print nothing, and a travel that skips it skips all of them, keeping only the travel itself:

- The [retraction](../../filament/setting_overrides/filament_retraction_length.md) pulls the filament back at the [Retraction speed](../../filament/setting_overrides/filament_retraction_speed.md) before the travel, and the [deretraction](../../printer/extruder/deretraction_speed.md) pushes it back, plus any [Extra length on restart](../../printer/extruder/retract_restart_extra.md), before the next line starts. With the default 0.8 mm at 30 mm/s, each of the two takes about 27 ms.
- With [Wipe while retracting](../../printer/extruder/wipe.md), the nozzle also moves back along the last line for the [Wipe distance](../../filament/setting_overrides/filament_wipe_distance.md) while it retracts.
- With a [Z-hop](../../printer/extruder/z_hop.md), the nozzle lifts before the travel and lowers after it, on the Z axis, which on most printers is much slower than X and Y.

Tens of milliseconds per travel can add up to minutes over the thousands of infill travels of a large print.

Travels shorter than the [Travel distance threshold](../../filament/setting_overrides/filament_retraction_minimum_travel.md) never retract, with or without this option. Infill lines whose ends are next to each other are joined into one path (see [Anchor](../../process/strength/infill_anchor.md)), so there is no travel to retract for between them.

**Recommended** when internal cosmetic quality is not critical and you want fewer retractions.
