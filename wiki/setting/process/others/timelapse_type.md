# timelapse_type

> Location: Process → Others → Special mode
> 显隐条件（初步梳理，待校对）：仅 BBL 系机型显示

---

## Timelapse

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `timelapse_type`.  
[Type](../../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../../general_settings/option_type.md#choice): `0, 1`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--timelapse-type=0`.  
Selects how the printer's camera takes the snapshots for a timelapse video. A snapshot is taken after each layer, and the snapshots are combined into a video when the print finishes. Recording itself is turned on with the **Timelapse** option of the print dialog when sending the job to the printer.

This option is only shown for Bambu Lab printers. The moves and camera commands for each snapshot come from the printer's [Timelapse G-code](../../printer/machine_gcode/printer_machine_gcode.md#timelapse-g-code), which is inserted once per layer. On other printers, add your own snapshot commands to that G-code.

- **Traditional**: The snapshot is taken without a prime tower. Whether the toolhead stays where it is or moves out of the way for the snapshot depends on the printer's Timelapse G-code.
- **Smooth**: After each layer, the toolhead moves to the excess chute and the snapshot is taken there. The next layer then starts by printing the prime tower, which wipes off any filament that leaked from the nozzle during the snapshot before the model is printed.

> [!NOTE]
> Smooth mode requires a [prime tower](../../process/multimaterial/multimaterial_settings_prime_tower.md), which is printed on every layer, even when the plate uses a single filament. Without it, the model may show flaws.
>
> - Selecting Smooth while the prime tower is disabled offers to enable it, and disabling the prime tower while Smooth is selected asks for confirmation.
> - Selecting Smooth turns off [No sparse layers](../../process/multimaterial/multimaterial_settings_prime_tower.md#no-sparse-layers), and enabling No sparse layers switches timelapse back to Traditional.
> - Smooth is not supported with the [By Object](#by-object) print sequence when the plate has more than one object.

[Spiral vase](#spiral-vase) mode requires Traditional. On printers with an i3 structure, such as the Bambu Lab A1 and A1 mini, no timelapse video is generated in spiral vase mode, and Traditional timelapse is not supported with the By Object print sequence.
