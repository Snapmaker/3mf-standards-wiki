# support_multi_bed_types

> Location: Printer → Basic information → Printable space

---

## Support multi bed types

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `support_multi_bed_types`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--support-multi-bed-types=1`.  
Once enabled, you can select the bed type in the drop-down menu, corresponding bed temperature will be set automatically.

![bed_type_selector](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/bed/bed_type_selector.png?raw=true)

This also enabled you to set each bed type in the [filament settings](../../filament/filament/material_temperatures.md#bed).

![bed_type_material_temperature](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/bed/bed_type_material_temperature.png?raw=true)

Orca also support `curr_bed_type` variable in custom G-code.
For example, the following sample G-codes can detect the selected bed type and adjust the G-code offset accordingly for Klipper:

```c++
{if curr_bed_type=="Textured PEI Plate"}
  SET_GCODE_OFFSET Z=-0.05
{else}
  SET_GCODE_OFFSET Z=0.0
{endif}
```

Available bed types are:

- Smooth Cool Plate
- Smooth High Temp Plate
- Textured Cool Plate
- Textured PEI Plate
- Engineering Plate
- Cool Plate (SuperTack)
