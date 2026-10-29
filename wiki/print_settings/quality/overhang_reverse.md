# overhang_reverse

> 所在界面：工艺设置 → Quality → Overhangs
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_overhangs.md` 的「Reverse on even」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Reverse on even

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `overhang_reverse`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--overhang-reverse=1`.  
Extrude perimeters that have a part over an overhang in the reverse direction on even layers. This alternating pattern can drastically improve steep overhangs thanks to material squishing direction.

This setting can also help reduce part warping due to the reduction of stresses as they are now distributed in alternating directions. Useful for warp-prone materials, like ABS/ASA, and also for elastic filaments, like TPU and Silk PLA.  
It can also help reduce warping on floating regions over supports.

For this setting to be the most effective, it is recommended to set the [Reverse Threshold](#reverse-threshold) to 0 so that all walls print in alternating directions on even layers irrespective of their overhang degree.
A disadvantage of this setting is that the outer wall may show a texture due to the alternating extrusion direction.

![reverse-odd-texture](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/reverse-odd-texture.png?raw=true)
