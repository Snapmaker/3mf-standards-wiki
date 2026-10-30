# slowdown_for_curled_perimeters

> Location: Process → Speed → Overhang speed

---

### Slow down for curled perimeters

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `slowdown_for_curled_perimeters`.  
[Type](../../../general_settings/option_type.md#list-types): `Boolean list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--slowdown-for-curled-perimeters=1`.  
Enable this option to slow down printing in areas where perimeters may have curled upwards.  
For example, additional slowdown will be applied when printing overhangs on sharp corners like the front of the Benchy hull, reducing curling which compounds over multiple layers.

![slow-down-for-curled-perimeters](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/speed/slow-down-for-curled-perimeters.png?raw=true)

It is generally recommended to have this option switched on unless your printer cooling is powerful enough or the print speed is slow enough that perimeter curling does not happen.  
If printing with a high external perimeter speed, this parameter may introduce wall artifacts when slowing down, due to the potentially large variance in print speeds causing the extruder to be unable to keep up with the requested flow change.  
Root cause of these artifacts is most likely PA tuning being slightly off, especially when combined with a high PA smooth time.

> [!TIP]
> When enabling this option:
>
> 1. For Klipper machines: Reduce Pressure Advance smooth time to 0.015 - 0.02 so the extruder reacts quickly to the speed changes.
> 2. Increase the minimum print speeds to limit the magnitude of the slowdown and reduce the variance between fast and slow segments.
> 3. If artifacts still appear, enable [Extrusion rate smoothing](../../process/speed/speed_settings_advanced.md) to further smooth the flow transitions.

> [!NOTE]
> When this option is enabled, overhang perimeters are treated like overhangs, meaning the overhang speed is applied even if the overhanging perimeter is part of a bridge.  
> For example, when the perimeters are 100% overhanging, with no wall supporting them from underneath, the 75% [overhang speed](#speed) will be applied, capped at the external [bridge speed](#bridge-speed).
