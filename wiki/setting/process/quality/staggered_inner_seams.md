# staggered_inner_seams

> Location: Process → Quality → Seam

---

### Staggered inner seams

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `staggered_inner_seams`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--staggered-inner-seams=1`.  
As the seam location forms a weak point in the print, staggering the seam on the internal perimeters can help reduce stress points. This setting shifts the seam of each internal wall along the loop, away from the external perimeter seam, by an amount based on the wall's depth, forming a zigzag pattern. This way, the internal and external seams don't all align at the same point, distributing those weak points further away from the seam location, hence making the part stronger. It can also help improve the water tightness of your model.

![seam-staggered-inner](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/seam/seam-staggered-inner.gif?raw=true)
