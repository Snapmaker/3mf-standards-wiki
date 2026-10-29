# support_multi_bed_types

> 所在界面：打印机设置 → Basic information → Printable space
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_printable_space.md` 的「Support multi bed types」小节（2026-10-28），英文原文，待本地化校对。

---

## Support multi bed types

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `support_multi_bed_types`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--support-multi-bed-types=1`.  
Once enabled, you can select the bed type in the drop-down menu, corresponding bed temperature will be set automatically.

![bed_type_selector](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/bed/bed_type_selector.png?raw=true)

This also enabled you to set each bed type in the [filament settings](material_temperatures#bed).

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
