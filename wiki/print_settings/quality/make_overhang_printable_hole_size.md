# make_overhang_printable_hole_size

> 所在界面：工艺设置 → Quality → Overhangs
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_overhangs.md` 的「Hole area」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Hole area

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `make_overhang_printable_hole_size`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--make-overhang-printable-hole-size=1`.  
Maximum area of a hole in the base of the model before it's filled by conical material.  
A value of 0 will fill all the holes in the model base.
