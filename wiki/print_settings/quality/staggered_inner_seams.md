# staggered_inner_seams

> 所在界面：工艺设置 → Quality → Seam
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_seam.md` 的「Staggered inner seams」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Staggered inner seams

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `staggered_inner_seams`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--staggered-inner-seams=1`.  
As the seam location forms a weak point in the print, staggering the seam on the internal perimeters can help reduce stress points. This setting shifts the seam of each internal wall along the loop, away from the external perimeter seam, by an amount based on the wall's depth, forming a zigzag pattern. This way, the internal and external seams don't all align at the same point, distributing those weak points further away from the seam location, hence making the part stronger. It can also help improve the water tightness of your model.

![seam-staggered-inner](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/seam/seam-staggered-inner.gif?raw=true)
