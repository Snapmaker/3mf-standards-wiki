# overhang_reverse

> Location: Process → Quality → Overhangs

---

## Reverse on even

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `overhang_reverse`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--overhang-reverse=1`.  
Extrude perimeters that have a part over an overhang in the reverse direction on even layers. This alternating pattern can drastically improve steep overhangs thanks to material squishing direction.

This setting can also help reduce part warping due to the reduction of stresses as they are now distributed in alternating directions. Useful for warp-prone materials, like ABS/ASA, and also for elastic filaments, like TPU and Silk PLA.  
It can also help reduce warping on floating regions over supports.

For this setting to be the most effective, it is recommended to set the [Reverse Threshold](#reverse-threshold) to 0 so that all walls print in alternating directions on even layers irrespective of their overhang degree.
A disadvantage of this setting is that the outer wall may show a texture due to the alternating extrusion direction.

![reverse-odd-texture](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/reverse-odd-texture.png?raw=true)
